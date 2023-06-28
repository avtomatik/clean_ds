import re

from pandas import DataFrame


def trim_string(string: str, fill: str = ' ') -> str:
    return fill.join(filter(bool, re.split(r'\W', string))).lower()


def trim_columns(df: DataFrame) -> DataFrame:
    df.columns = map(lambda _: trim_string(_, fill='_'), df.columns)
    return df
