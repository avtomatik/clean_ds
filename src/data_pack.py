#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:51:24 2022

@author: Alexander Mikhailov
"""

import os
from pathlib import Path

import pandas as pd
from pandas import DataFrame

from thesis.src.lib.push import push_data_frame_to_csv_zip


def transform(df: DataFrame) -> DataFrame:
    df.insert(1, 'desc', df.columns[1])
    df.columns = ('period', 'desc', 'value')
    return df.set_index(df.columns[0])


def main(
    path_src: str = '/media/green-machine/KINGSTON',
    path_export: str = '/home/green-machine/Downloads',
    file_names: tuple[str] = (
        'dataset_usa_0000_public_debt.txt',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
    ),
    archive_name: str = 'dataset_usa_misc'
):
    df = pd.concat(
        map(
            lambda _: pd.read_csv(Path(path_src).joinpath(_)).pipe(transform), file_names
        )
    )

    os.chdir(path_export)
    df.pipe(push_data_frame_to_csv_zip, archive_name)


if __name__ == '__main__':
    main()
