"""
Top level script.
"""
from lib.functions import load_crime_data, calculate_standard_deviation, calculate_mean, calculate_quartiles, pretty_hist_plot

if __name__ == "__main__":
    df = load_crime_data()

    # subset numeric variables
    victim_ages = df['Vict Age'].values
    crime_times = df['TIME OCC'].values

    victim_ages_clean = df['Vict Age'][(df['Vict Age'] > 0) & (df['Vict Age'] < 95)]

    data_dict = {
        
    }
