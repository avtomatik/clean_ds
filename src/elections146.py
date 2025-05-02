# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:23:22 2021

@author: Alexander Mikhailov
"""

import pandas as pd

from samples import ELECTION_RESULTS


def get_election_results(data: dict[str, float]) -> pd.DataFrame:
    df = pd.DataFrame(list(data.items()), columns=['party', 'percentage'])
    df['corrected'] = df['percentage'].div(df['percentage'].sum())
    return df


if __name__ == '__main__':
    print(get_election_results(ELECTION_RESULTS))
