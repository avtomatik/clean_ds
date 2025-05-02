# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:49:26 2022

@author: Alexander Mikhailov
"""


import dask.dataframe as dd
import databricks.koalas as ks
import numpy as np
import pandas as pd

from config import DATA_PATH

# =============================================================================
# Source: theolympicsguy@gmail.com
# =============================================================================
FILE_NAME = 'olympics_medals_country_wise.csv'


file_path = DATA_PATH.joinpath(FILE_NAME)


def showcase_dask_dataframe():
    # =========================================================================
    # Dask DataFrame
    # =========================================================================
    df = dd.read_csv(file_path, thousands=',')
    print(df.head())


showcase_dask_dataframe()
# =============================================================================
# from pandas_profiling import ProfileReport
# import geopandas
# import plotly.express as px
# =============================================================================


# =============================================================================
# from pyspark.sql import SparkSession
# =============================================================================


pdf = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
pdf.head()

# =============================================================================
# TODO: https://www.databricks.com/: Databricks community edition: to sign up
# =============================================================================
kdf = ks.from_pandas(pdf)
kdf.head()


# =============================================================================
# pandas.plotting.scatter_matrix
# =============================================================================
