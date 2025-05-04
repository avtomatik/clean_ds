# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:49:26 2022

@author: Alexander Mikhailov
"""


import dask.dataframe as dd
import databricks.koalas as ks
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

from config import DATA_DIR

# =============================================================================
# import geopandas
# import plotly.express as px
# from pandas_profiling import ProfileReport
# from pyspark.sql import SparkSession
# =============================================================================


# =============================================================================
# Source: theolympicsguy@gmail.com
# =============================================================================
FILE_NAME = 'olympics_medals_country_wise.csv'
FILE_PATH = DATA_DIR / FILE_NAME


def load_with_dask(file_path: str) -> dd.DataFrame:
    """Load a large CSV file using Dask."""
    df = dd.read_csv(file_path, thousands=',')
    return df


def create_sample_dataframe() -> pd.DataFrame:
    """Create a sample pandas DataFrame for testing."""
    return pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))


def convert_to_koalas(df: pd.DataFrame) -> ks.DataFrame:
    """Convert a pandas DataFrame to a Koalas DataFrame."""
    return ks.from_pandas(df)


def plot_scatter_matrix(df: pd.DataFrame, title: str = 'Scatter Matrix') -> None:
    """Plot a scatter matrix of numerical values in the DataFrame."""
    scatter_matrix(df, alpha=0.8, figsize=(8, 6), diagonal='hist')
    plt.suptitle(title)
    plt.tight_layout()
    plt.show()


def main():
    # Showcase reading a large CSV file using Dask
    dask_df = load_with_dask(FILE_PATH)
    print('Preview of Dask DataFrame:')
    print(dask_df.head())

    # Create a random DataFrame and convert to Koalas
    pdf = create_sample_dataframe()
    print('Sample pandas DataFrame:')
    print(pdf.head())

# =============================================================================
# TODO: https://www.databricks.com/: Databricks community edition: to sign up
# =============================================================================
    kdf = convert_to_koalas(pdf)
    print('Converted Koalas DataFrame:')
    print(kdf.head())

    # Plot scatter matrix for exploratory visualization
    plot_scatter_matrix(pdf, title='Sample Data Scatter Matrix')


if __name__ == '__main__':
    main()
