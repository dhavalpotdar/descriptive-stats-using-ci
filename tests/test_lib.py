import numpy as np
from src.lib.functions import load_crime_data, calculate_mean, calculate_quartiles, calculate_standard_deviation


def test_load_crime_data():
    df = load_crime_data()
    assert df.shape[0] == 798242
    assert df.shape[1] == 28

def test_calculate_mean():
    test_arr = np.array([1, 2, 3, 4, 5])
    assert calculate_mean(test_arr) == 3

def test_calculate_quartiles():
    test_arr = np.array([1, 2, 3, 4, 5])
    first, median, third = calculate_quartiles(test_arr)
    assert first == 2
    assert median == 3
    assert third == 4

def test_calculate_standard_deviation():
    test_arr = np.array([1, 2, 3, 4, 5])
    assert np.round(calculate_standard_deviation(test_arr), 2) == 1.41

