# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:49:26 2022

@author: Alexander Mikhailov
"""


import dask.dataframe as dd
import numpy as np
import pandas as pd
# =============================================================================
# Start Here
# =============================================================================
import seaborn as sns
from sklearn.datasets import load_iris


def olympics():
    return
    # =========================================================================
    # theolympicsguy@gmail.com
    # =========================================================================
    oo = pd.read_csv('..\\data\\olympics_medals_country_wise.csv')


# =============================================================================
# Brett Vanderblock
# =============================================================================
# =============================================================================
# TODO: https://www.databricks.com/: Databricks community edition: to sign up
# =============================================================================
iris = load_iris()
iris = pd.concat(
    [
        pd.DataFrame(
            data=iris.data,
            columns=("sepal length", "sepal width",
                     "petal length", "petal width")
        ),
        pd.DataFrame(data=iris.target, columns=("species",))
    ],
    axis=1
)
# # =============================================================================
# # Boxplot
# # =============================================================================
# iris.boxplot()

# =============================================================================
# Correlation Matrix
# =============================================================================
# =============================================================================
# Another Implementation
# =============================================================================
# iris.corr().style.background_gradient(cmap='RdYlGn', axis=None)
sns.heatmap(iris.corr(), annot=True)

# =============================================================================
# colors = {
#     "versicolor": "red",
#     "setosa": "green",
#     "virginica": "blue",
# }
# iris["colors"] = iris["species"].map(colors)
# iris.plot.scatter(x="sepal_width", y="sepal_length", color=iris["colors"])
# =============================================================================


def showcase_dask_dataframe():
    # =========================================================================
    # Dask DataFrame
    # =========================================================================

    df = dd.read_csv(
        '..\\data\\olympics_medals_country_wise.csv',
        thousands=','
    )
    print(df.head())


showcase_dask_dataframe()
# =============================================================================
# from pandas_profiling import ProfileReport
# import geopandas
# import plotly.express as px
# =============================================================================


# import databricks.koalas as ks
# from pyspark.sql import SparkSession


# =============================================================================
# pdf = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
# pdf.head()
#
# kdf = ks.from_pandas(pdf)
# kdf.head()
# =============================================================================


# =============================================================================
# pandas.plotting.scatter_matrix
# =============================================================================
