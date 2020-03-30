# test plotting.py functions
from . import context
import pytest
from tkabf_explorer import plotting


#{"x":[], "y1":[[]], "x_label":"x", "y1_label":"y", "y2":[[]], "y2_label":"y",
#"fontsize":16, "sweep_label":[], "linewidth":4, "y2_color":"black"}


def test_check_len_equals():
    x = [1,2,3]
    y = [1,2,3]
    y_short = [1]
    y_empty = []
    y_with_list = [[1,3,2]]
    assert 1==2

def test_check_is_not_num_or_string():
    x = 1
    x1 = []
    x2 = [[1,2,3], []]
    x3 = [[1,2,3], 1]
    x4 = [[1,2,3], "string"]
    assert 1==2

def test_must_be_num_or_string():
    assert 1==2

def test_subarrays_must_be_equal():
    assert 1==2

def test_check_dim_x_dim_each_y_arr():
    assert 1==2

def test_validate_data_len_and_type():
    assert 1==2

def test_validate_plot_data():
    """integration test of all other functions"""
    assert 1==2
