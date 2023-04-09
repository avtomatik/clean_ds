#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 15:26:09 2023

@author: green-machine
"""

import os
from pathlib import PosixPath
from typing import Union

import pandas as pd
from pandas import DataFrame

from thesis.src.lib.collect import combine_usa_general


def read_frugal(io: Union[str, PosixPath], call: callable) -> DataFrame:
    """


    Parameters
    ----------
    io : Union[str, PosixPath]
        DESCRIPTION.
    call : callable
        Some Collect Function.

    Returns
    -------
    DataFrame
        DESCRIPTION.

    """
    if not os.path.exists(io):
        call().to_excel(io)
    return pd.read_excel(io, index_col=0)


read_frugal('temporary_dataset.xlsx', combine_usa_general)
