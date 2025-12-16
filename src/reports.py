import logging
from datetime import datetime, timedelta
from functools import wraps
from typing import Callable, Optional

import pandas as pd

logging.basicConfig(level=logging.INFO)


def report_writer(filename: Optional[str] = None):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            name = filename or f"{func.__name__}_{datetime.now():%Y%m%d_%H%M%S}.xlsx"
            result.to_excel(name, index=False)
            logging.info(f"Report saved to {name}")
            return result

        return wrapper

    return decorator


def _date_border(date: Optional[str]) -> tuple[datetime, datetime]:
    end = datetime.strptime(date, "%Y-%m-%d") if date else datetime.now()
    start = end - timedelta(days=90)
    return start, end


@report_writer()
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[str] = None
) -> pd.DataFrame:
    start, end = _date_border(date)
    df = transactions[
        (transactions["operation_date"].between(start, end))
        & (transactions["category"] == category)
        & (transactions["operation_amount"] < 0)
    ]
    return df.groupby("category", as_index=False)["operation_amount"].sum()


@report_writer()
def spending_by_weekday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    start, end = _date_border(date)
    df = transactions[
        (transactions["operation_date"].between(start, end))
        & (transactions["operation_amount"] < 0)
    ].copy()
    df["weekday"] = df["operation_date"].dt.day_name()
    return df.groupby("weekday", as_index=False)["operation_amount"].mean()


@report_writer()
def spending_by_workday(
    transactions: pd.DataFrame, date: Optional[str] = None
) -> pd.DataFrame:
    start, end = _date_border(date)
    df = transactions[
        (transactions["operation_date"].between(start, end))
        & (transactions["operation_amount"] < 0)
    ].copy()
    df["day_type"] = df["operation_date"].dt.weekday < 5
    return df.groupby("day_type", as_index=False)["operation_amount"].mean()
