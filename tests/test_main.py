import sys
import numpy as np

sys.path.append("/workspaces/descriptive-stats-using-ci/src")
from src.main import format_desc_stats


def test_format_desc_stats():
    data_dict = {"Numerical Column": [np.nan, np.nan, np.nan, np.nan, np.nan]}

    output = format_desc_stats(data_dict=data_dict)
    # make sure function is generating all 5 statistics
    assert output.shape[1] == 5
