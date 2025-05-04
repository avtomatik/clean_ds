#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  4 11:48:10 2025

@author: alexandermikhailov
"""


import pandas as pd
from string_utils import trim_string


def normalize_column_names(
    df: pd.DataFrame,
    filler: str = '_'
) -> pd.DataFrame:
    """Clean column names using a specified filler character."""
    df.columns = [trim_string(col, fill=filler) for col in df.columns]
    return df
