import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_pacf

def plot_time_series(df, columns, acc=False, pacf=False):
    """
    Plots time series data, with options for decomposition and PACF plots.

    Parameters:
    - df (pandas.DataFrame): The dataframe containing the time series data.
    - columns (list): List of column names in df to be plotted.
    - acc (bool, optional): If True, plots decomposition plots for each column. Defaults to False.
    - pacf (bool, optional): If True, plots PACF plot for each column. Defaults to 36 lags. Defaults to False.

    Returns:
    - Plots of time series data, decomposition, and/or PACF based on input flags.
    """
    sns.set_style("darkgrid")

    # plot each column on the same time plot
    plt.figure(figsize=(10, 6))
    for column in columns:
        plt.plot(df.index, df[column], label=column)
    plt.title('Time Series Plot')
    plt.legend()
    plt.show()

    # if acc is true, plot decomposition plots for each column
    if acc:
        for column in columns:
            result = seasonal_decompose(df[column], model='additive', period=1)
            result.plot()
            plt.suptitle(f'Decomposition Plot for {column}', y=1.05)
            plt.tight_layout()
            plt.show()

    # if pacf is true, plot pacf for each column
    if pacf:
        for column in columns:
            plt.figure(figsize=(10, 6))
            plot_pacf(df[column], lags=36)
            plt.title(f'PACF for {column}')
            plt.show()
