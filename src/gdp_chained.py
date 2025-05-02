#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:47:36 2022

@author: Alexander Mikhailov
"""

"""
Chain-Weighted GDP
"""


import numpy as np
import pandas as pd

pd.options.display.max_columns = 10

# =============================================================================
# period[1] = 2
# =============================================================================
year_base = 1
# =============================================================================
# series length
# =============================================================================
length = 3

data = {
    'period': [1 + _ for _ in range(length)],
    'price_a': [20 + _ for _ in range(length)],
    'price_b': [60 - _ for _ in range(length)],
    'quantity_a': [75 + _ for _ in range(length)],
    'quantity_b': [25 + 5 * _ for _ in range(length)],
}

df = pd.DataFrame.from_dict(data)
df.set_index(df.columns[0], inplace=True)
# =============================================================================
# GDP Weighted Current Year`s Prices, i. e. Nominal GDP
# =============================================================================
df['gdp_n'] = df.iloc[:, 0].mul(df.iloc[:, 2]).add(
    df.iloc[:, 1].mul(df.iloc[:, 3]))
# =============================================================================
# GDP Weighted Next Year`s Prices
# =============================================================================
df['gdp_a'] = df.iloc[:, 0].shift(-1).mul(df.iloc[:, 2]
                                          ).add(df.iloc[:, 1].shift(-1).mul(df.iloc[:, 3]))
# =============================================================================
# GDP Weighted Last Year`s Prices
# =============================================================================
df['gdp_b'] = df.iloc[:, 0].shift(1).mul(df.iloc[:, 2]).add(
    df.iloc[:, 1].shift(1).mul(df.iloc[:, 3]))
# =============================================================================
# Real Growth Rate, Weight = Current Year`s Prices
# =============================================================================
df['gr_a'] = df.iloc[:, 4].div(df.iloc[:, 5].shift(1)).sub(1)
# =============================================================================
# Real Growth Rate, Weight = Last Year`s Prices
# =============================================================================
df['gr_b'] = df.iloc[:, 6].div(df.iloc[:, 4].shift(1)).sub(1)
# =============================================================================
# Real Growth Rate, Weight = Last Year`s Prices
# =============================================================================
df['gr_c'] = np.sqrt(df.iloc[:, 7].mul(df.iloc[:, 8])).fillna(0)
# =============================================================================
# Real Growth Rate Chain Weighted
# =============================================================================
df['gr_c_cum'] = df.iloc[:, 9].add(1).cumprod()
# =============================================================================
# Chain-Weighted Real GDP, Base Year = 'year_base'
# =============================================================================
df['gdp_r'] = df.iloc[:, 10].mul(df.iloc[year_base, 4]).div(df.iloc[year_base, 10])
df = df.iloc[:, [0, 1, 2, 3, 4, 11]]
