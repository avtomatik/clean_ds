#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:43:32 2025

@author: alexandermikhailov
"""


from pathlib import Path
from typing import Callable, Union

import pandas as pd

from funcs.strings import trim_string


def trim_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = map(lambda _: trim_string(_, fill='_'), df.columns)
    return df


def load_or_create_csv(
    filepath: Union[str, Path],
    func: Callable[[], pd.DataFrame]
) -> pd.DataFrame:
    """
    Loads a CSV file into a pd.DataFrame. If the file does not exist, it
    creates the file using the provided data collection function and saves it
    as a CSV.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path to the CSV file.
    func : Callable[[], pd.DataFrame]
        A function that returns a pd.DataFrame to be saved if the file does not
        exist.

    Returns
    -------
    pd.DataFrame
        Loaded data from the CSV file.
    """
    path = Path(filepath)
    if not path.exists():
        func().to_csv(path)
    return pd.read_csv(path, index_col=0)
