"""
Top level script.
"""
# ruff: noqa: E402
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append('/workspaces/descriptive-stats-using-ci/src') 
from src.lib.functions import (
    load_crime_data,
    calculate_standard_deviation,
    calculate_mean,
    calculate_quartiles,
    pretty_hist_plot,
)





def format_desc_stats(data_dict):
    output = pd.DataFrame.from_dict(
    data_dict,
    orient="index",
    columns=[
        "Mean",
        "Std. Deviation",
        "25th Percentile",
        "Median",
        "75th Percentile",
    ])
    return output

if __name__ == "__main__":
    df = load_crime_data()

    # subset numeric variables
    victim_ages = df["Vict Age"].values
    crime_times = df["TIME OCC"].values

    victim_ages_clean = df["Vict Age"][(df["Vict Age"] > 0) & (df["Vict Age"] < 95)]

    data_dict = {
        "Victim Age": [
            calculate_mean(victim_ages_clean),
            calculate_standard_deviation(victim_ages_clean),
            calculate_quartiles(victim_ages_clean)[0],
            calculate_quartiles(victim_ages_clean)[1],
            calculate_quartiles(victim_ages_clean)[2],
        ],
        "Crime Times": [
            calculate_mean(crime_times),
            calculate_standard_deviation(crime_times),
            calculate_quartiles(crime_times)[0],
            calculate_quartiles(crime_times)[1],
            calculate_quartiles(crime_times)[2],
        ],
    }

    output_df = format_desc_stats(data_dict=data_dict)

    with open("/workspaces/descriptive-stats-using-ci/outputs/DESC_STATS.md", "w") as f:
        # Writing data to a file
        f.write("\n")
        f.writelines(output_df.to_markdown())

    # plot
    pretty_hist_plot(
        series=victim_ages_clean,
        title="Distribution of Ages of Victims",
        xlab="Age",
        ylab="Count of Incidents",
    )
    plt.savefig("outputs/figure.png")
