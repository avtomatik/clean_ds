#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:47:36 2022

@author: Alexander Mikhailov

Chain-Weighted Real GDP Calculation
"""

import numpy as np
import pandas as pd


def generate_data(length: int) -> pd.DataFrame:
    """Generate synthetic GDP-related data."""
    data = {
        'period': [1 + i for i in range(length)],
        'price_a': [20 + i for i in range(length)],
        'price_b': [60 - i for i in range(length)],
        'quantity_a': [75 + i for i in range(length)],
        'quantity_b': [25 + 5 * i for i in range(length)],
    }
    df = pd.DataFrame(data).set_index('period')
    return df


def calculate_nominal_gdp(df: pd.DataFrame) -> pd.Series:
    """Calculate nominal GDP using current year prices."""
    return df['price_a'] * df['quantity_a'] + df['price_b'] * df['quantity_b']


def calculate_adjacent_year_gdp(df: pd.DataFrame, shift: int) -> pd.Series:
    """Calculate GDP weighted by prices from adjacent years."""
    return (
        df['price_a'].shift(shift) * df['quantity_a'] +
        df['price_b'].shift(shift) * df['quantity_b']
    )


def calculate_real_growth_rates(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate growth rates using various price weights."""
    df['gr_a'] = df['gdp_n'] / df['gdp_a'].shift(1) - 1
    df['gr_b'] = df['gdp_b'] / df['gdp_n'].shift(1) - 1
    df['gr_c'] = np.sqrt((1 + df['gr_a']) * (1 + df['gr_b'])) - 1
    return df


def calculate_chain_weighted_gdp(df: pd.DataFrame, base_index: int) -> pd.DataFrame:
    """Calculate chain-weighted real GDP from growth rates."""
    df['gr_c_cum'] = (1 + df['gr_c'].fillna(0)).cumprod()
    base_nominal = df['gdp_n'].iloc[base_index]
    base_cum_growth = df['gr_c_cum'].iloc[base_index]
    df['gdp_r'] = df['gr_c_cum'] * base_nominal / base_cum_growth
    return df


def main():
    pd.options.display.max_columns = 10
    year_base = 1
    length = 3

    df = generate_data(length)
    df['gdp_n'] = calculate_nominal_gdp(df)
    df['gdp_a'] = calculate_adjacent_year_gdp(df, shift=-1)
    df['gdp_b'] = calculate_adjacent_year_gdp(df, shift=1)

    df = calculate_real_growth_rates(df)
    df = calculate_chain_weighted_gdp(df, base_index=year_base)

    # Final selected columns
    final_df = df[['price_a', 'price_b',
                   'quantity_a', 'quantity_b', 'gdp_n', 'gdp_r']]
    print(final_df)


if __name__ == '__main__':
    main()
