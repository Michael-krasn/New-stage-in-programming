import pandas as pd


def load_transactions(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    df.columns = [
        "operation_date",
        "payment_date",
        "card_number",
        "status",
        "operation_amount",
        "operation_currency",
        "payment_amount",
        "payment_currency",
        "category",
        "mcc",
        "description",
        "cashback",
        "rounding",
        "total_amount",
    ]
    df["operation_date"] = pd.to_datetime(df["operation_date"], dayfirst=True)
    df["operation_amount"] = (
        df["operation_amount"].astype(str).str.replace(",", ".").astype(float)
    )
    return df
