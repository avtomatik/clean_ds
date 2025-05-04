#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 19:43:32 2025

@author: alexandermikhailov
"""


from pathlib import Path
from typing import Callable, Union

import pandas as pd


def load_or_create_csv(
    filepath: Union[str, Path],
    data_func: Callable[[], pd.DataFrame]
) -> pd.DataFrame:
    """
    Loads a CSV file, or creates and saves it using a fallback function.
    """
    path = Path(filepath)
    if not path.exists():
        df = data_func()
        df.to_csv(path)
    return pd.read_csv(path, index_col=0)
