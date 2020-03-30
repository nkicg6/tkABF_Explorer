# plotting helper functions

def _check_len_equals(x,y):
    """raises assertion error if len(x) != len(y)"""
    assert len(x) == len(y)

def _check_is_not_num_or_string(x):
    """raises assertion error is type is not list"""
    assert not isinstance(x, (str, float, int, type(None)))
    for item in x:
        print(item)
        assert not isinstance(item, (str,float,int, type(None)))


def validate_data(m):
    """verify that the map passed in has appropriate dimensions"""
    m = m.copy()
    must_equal = ["y1", "y2", "sweep_label", ]
    must_be_len_1 = ["x", "x_label", "y_label", "y2_label", "fontsize", "linewidth"]
    assert len(m["y1"]) == len(m["y2"]), f"problem with input data {m} in function `validate_data`"
    return m
