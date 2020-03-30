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
    plotting._check_len_equals(x,y)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(x,y_short)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(x,y_empty)
    with pytest.raises(AssertionError):
        plotting._check_len_equals(x,y_with_list)

def test_check_is_not_num_or_string():
    x = 1
    x1 = []
    x2 = [[1,2,3], []]
    x3 = [[1,2,3], 1]
    x4 = [[1,2,3], "string"]
    plotting._check_is_not_num_or_string(x1)
    plotting._check_is_not_num_or_string(x2)
    with pytest.raises(AssertionError):
        plotting._check_is_not_num_or_string(x)
    with pytest.raises(AssertionError):
        plotting._check_is_not_num_or_string(x3)


def test_validate_data():
    x = [1,2,3]
    y1 = [4,5,6]
    y1_1 = [5,6,7]
    y2 = [1.5,2.5,3.5]
    y2_1 = [i*0.1 for i in y2]
    labels = ["one" , "two"]
    test_map1 = {'x':x, "y1":[y1,y1_1],"y2":[y2,y2_1], "sweep_label":labels}
    test_map2 = {'x':x, "y1":[],"y2":[y2,y2_1], "sweep_label":labels}
    test_map3 = {'x':x, "y1":[y1],"y2":[y2,y2_1]}
    test_map4 = {'x':x, "y1":["on"],"y2":[y2,y2_1], "sweep_label":labels}
    assert test_map1 == plotting.validate_data(test_map1)
    with pytest.raises(AssertionError):
        plotting.validate_data(test_map2)
    with pytest.raises(AssertionError):
        plotting.validate_data(test_map3)
    with pytest.raises(AssertionError):
        plotting.validate_data(test_map4)
