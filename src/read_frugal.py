#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:26:09 2023

@author: green-machine
"""

from pathlib import PosixPath
from typing import Union

import pandas as pd
from pandas import DataFrame
from thesis.src.lib.combine import combine_usa_general


def read_frugal(filepath_or_buffer: Union[str, PosixPath], func: callable) -> DataFrame:
    """


    Parameters
    ----------
    io : Union[str, PosixPath]
        DESCRIPTION.
    func : callable
        Some Collect Function.

    Returns
    -------
    DataFrame
        DESCRIPTION.

    """
    if not filepath_or_buffer.exists():
        func().to_csv(filepath_or_buffer)
    kwargs = {
        'filepath_or_buffer': filepath_or_buffer,
        'index_col': 0,
    }
    return pd.read_csv(**kwargs)


read_frugal('temporary_dataset.csv', combine_usa_general)
