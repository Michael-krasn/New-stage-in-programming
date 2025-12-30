import pandas as pd

from src.reports import spending_by_category


def test_spending_by_category():
    data = {
        "operation_date": pd.to_datetime(["2021-12-20", "2021-12-21"]),
        "category": ["Фастфуд", "Фастфуд"],
        "operation_amount": [-100, -50],
    }
    df = pd.DataFrame(data)
    result = spending_by_category(df, "Фастфуд", "2021-12-22")
    assert result.iloc[0]["operation_amount"] == -150