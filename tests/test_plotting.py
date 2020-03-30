# test plotting.py functions
from . import context
import pytest
from tkabf_explorer import plotting


{"x":[], # type: numpy array or list; length must be == to the length of each y1 and y2 sub-array
 "y1":[[]], # type: list of numpy arrays; number of sub arrays must equal number of sub arrays for y2. Length of x, y1 (each subarray), y2 (each subarray) must be equal
 "x_label":"x", # type: string
 "y1_label":"y", # type: string
 "y2":[[]], # type: list of numpy arrays; see constraints on y1
 "y2_label":"y", # type: string
"fontsize":16, # type: int
 "sweep_label":[], # type: list of strings; length of list of strings must be == to length of arrays in y1 and y2
 "linewidth":4, # type: int
 "y2_color":"black" # type: string
}


def test_check_len_equals():
    x = [1,2,3]
    y = [1,2,3]
    y_short = [1]
    y_empty = []
    y_with_list = [[1,3,2]]
    plotting._check_len_equals(x,y) #should pass
    plotting._check_len_equals(y_empty,y_empty)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(x,y_short)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(x,y_with_list)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(y_short,y_with_list)

def test_check_is_not_num_or_string():
    x = 1
    x1 = []
    x2 = "string"
    x3 = [[1,2,3], [1]]
    x4 = None
    plotting._check_is_not_num_or_string(x1)
    plotting._check_is_not_num_or_string(x3)
    with pytest.raises(AssertionError):
        plotting._check_is_not_num_or_string(x)
    with pytest.raises(AssertionError):
        plotting._check_is_not_num_or_string(x2)
    with pytest.raises(AssertionError):
        plotting._check_is_not_num_or_string(x4)


def test_must_be_num_or_string():
    test_1 = {"x_label":[],
              "y1_label":[],
              "y2_label":[],
              "fontsize":[],
              "linewidth":[]}
    test_pass = {"x_label":"string",
                 "y1_label":"string",
                 "y2_label":"string",
                 "fontsize":1,
                 "linewidth":3}
    missing_key = {"x_label":"string",
                   "y2_label":"string",
                   "fontsize":1,
                   "linewidth":3}
    plotting._must_be_num_or_string(test_pass)
    with pytest.raises(KeyError):
        plotting._must_be_num_or_string(missing_key)
    with pytest.raises(AssertionError):
        plotting._must_be_num_or_string(test_1)


def test_subarrays_must_be_equal():
    test1 = {"y1":[],"y2":[]}
    test2 = {"y1":[[1,2,3]],"y2":[[1,2,3]]}
    test3 = {"y1":[[1,2]],"y2":[[1,2,3]]}
    test4 = {"y1":[[]],"y2":[[1,2,3]]}
    test5 = {"yy1":[[]],"y2":[[1,2,3]]}
    plotting._subarrays_must_be_equal(test1)
    plotting._subarrays_must_be_equal(test2)
    with pytest.raises(AssertionError):
        plotting._subarrays_must_be_equal(test3)
    with pytest.raises(AssertionError):
        plotting._subarrays_must_be_equal(test4)
    with pytest.raises(KeyError):
        plotting._subarrays_must_be_equal(test5)

def test_check_dim_x_dim_each_y_arr():
    test1 = {"x":[],"y1":[],"y2":[]}
    test2 = {"x":[1, 2, 3],"y1":[[1,2,3]],"y2":[[1,2,3]]}
    test3 = {"x":[1, 2, 3],"y1":[[1,2,3],[1,2,3]],"y2":[[1,2,3]]}
    test4 = {"x":[1, 2, 3],"y1":[[1,2,3],[1,3]],"y2":[[1,2,3],[1,2,3]]}
    plotting._check_dim_x_dim_each_y_arr(test1)
    plotting._check_dim_x_dim_each_y_arr(test2)
    with pytest.raises(AssertionError):
        plotting._check_dim_x_dim_each_y_arr(test3) # should fail
    with pytest.raises(AssertionError):
        plotting._check_dim_x_dim_each_y_arr(test4)

def test_validate_plot_data():
    """integration test of all other functions"""
    pass1 = {"x":[],
             "y1":[],
             "x_label":"x",
             "y1_label":"y",
             "y2":[],
             "y2_label":"y",
             "fontsize":16,
             "sweep_label":[],
             "linewidth":4,
             "y2_color":"black"}
    pass2 = {"x":[1,2,3],
             "y1":[[1,2,3],[1,2,3]],
             "x_label":"x",
             "y1_label":"y",
             "y2":[[1,2,3],[1,2,3]],
             "y2_label":"y",
             "fontsize":16,
             "sweep_label":["sweep1", "sweep2"],
             "linewidth":4,
             "y2_color":"black"}
    fail1 = {"x":[1,2,3],
             "y1":[[1,2,3]],
             "x_label":"x",
             "y1_label":"y",
             "y2":[[1,2,3]],
             "y2_label":"y",
             "fontsize":16,
             "sweep_label":[],
             "linewidth":4,
             "y2_color":"black"}
    fail2 = {"x":[1,2,3],
             "y1":[[1,2,3],[1,2,3]],
             "x_label":"x",
             "y1_label":"y",
             "y2":[[1,2,3],[1,2]],
             "y2_label":"y",
             "fontsize":16,
             "sweep_label":["sweep1", "sweep2"],
             "linewidth":4,
             "y2_color":"black"}
    plotting.validate_plot_data(pass1)
    plotting.validate_plot_data(pass2)
    with pytest.raises(AssertionError):
        plotting.validate_plot_data(fail1)
    with pytest.raises(AssertionError):
        plotting.validate_plot_data(fail2)
