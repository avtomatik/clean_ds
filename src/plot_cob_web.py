#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:17:06 2022

@author: Alexander Mikhailov
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame


def main(
    path: str = '/media/green-machine/KINGSTON',
    file_name: str = 'dataset_usa_0025_p_r.txt'
) -> None:
    """
    Draws cobweb plot or Verhulst diagram for Given Dataset

    Parameters
    ----------
    path : str, optional
        DESCRIPTION. The default is '/media/green-machine/KINGSTON'.
    file_name : str, optional
        DESCRIPTION. The default is 'dataset_usa_0025_p_r.txt'.

    Prerequisite:
        ================== =================================
        _df.iloc[:, 0]      Period
        _df.iloc[:, 1]      Series
        ================== =================================
    Returns
    -------
    None
    """
    kwargs = {
        'filepath_or_buffer': Path(path).joinpath(file_name),
        'index_col': 0,
    }
    _df = pd.read_csv(**kwargs)
    # =========================================================================
    # Dataset Preprocessing
    # =========================================================================
    _df = _df.div(_df.iloc[0, :])
    df = DataFrame(
        data=[
            _df.iloc[_ // 2, 0] for _ in range(1, 2 * _df.shape[0])
        ],
        columns=['calc']
    )
    df = pd.concat(
        [
            df,
            df.shift(-1)
        ],
        axis=1,
    ).dropna(axis=0)
    x_lin = np.linspace(_df.min(), _df.max(), 100)
    # =========================================================================
    # Plotting
    # =========================================================================
    plt.figure()
    plt.plot(
        df.iloc[:, 0],
        df.iloc[:, 1],
        label='Series',
        lw=.5
    )
    plt.plot(x_lin, x_lin, label='$Y_{t} = Y_{1+t}$', color='k', lw=.5)
    plt.xlabel('$Y_{t}$')
    plt.ylabel('$Y_{1+t}$')
    plt.title('Cobweb Plot')
    plt.grid()
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
