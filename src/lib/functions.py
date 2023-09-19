import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


def load_crime_data():

    if not os.path.exists("data/"):
        os.makedirs("data/")
        pass

    FILENAME = \
        "/workspaces/descriptive-stats-using-ci/data/Crime_Data_from_2020_to_Present.csv"
    # DATALINK = (
    #     r"https://data.lacity.org/api/views/2nrs-mtv8/rows.csv?accessType=DOWNLOAD"
    # )

    # if not os.path.isfile(FILENAME):
    #     df = pd.read_csv(DATALINK)
    #     df.to_csv(FILENAME, index=None)
    # else:
    #     df = pd.read_csv(FILENAME)

    df = pd.read_csv(FILENAME)

    return df


def calculate_standard_deviation(arr):
    if len(arr) < 2:
        return None

    mean = sum(arr) / len(arr)
    variance = sum((x - mean) ** 2 for x in arr) / (len(arr))
    standard_deviation = math.sqrt(variance)
    return np.round(standard_deviation, 2)


def calculate_mean(arr):
    if len(arr) == 0:
        return None  # Handle the case of an empty array

    total = sum(arr)
    mean = total / len(arr)
    return np.round(mean, 2)


def calculate_quartiles(arr):
    # Sort the array in ascending order
    sorted_arr = sorted(arr)

    # Calculate the median (Q2)
    median = np.median(sorted_arr)

    q1 = np.percentile(sorted_arr, 25)
    q3 = np.percentile(sorted_arr, 75)

    return np.round(q1, 2), np.round(median, 2), np.round(q3, 2)


def pretty_hist_plot(series, title, xlab, ylab):
    sns.set_style("darkgrid")

    # specify the bins
    bins = np.arange(0, series.max() + 1, 1)

    # plot
    plt.figure(figsize=(8, 6))
    plt.hist(x=series, bins=bins)

    # label
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
