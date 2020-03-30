# plotting helper functions

def _check_len_equals(x,y):
    """raises assertion error if len(x) != len(y)"""
    assert len(x) == len(y)

def _check_is_not_num_or_string(x):
    """raises assertion error is type is not expected. Type should be numpy array or list.
    Can be an empty list."""
    assert not isinstance(x, (str, float, int, type(None)))

def _must_be_num_or_string(m):
    """These keys must be an int, float or string, cannot be a container (list, tuple, numpy array, etc.)"""
    must_be_num_or_string = ["x_label", "y_label", "y2_label", "fontsize", "linewidth"]
    for i in must_be_num_or_string:
        assert isinstance(m[i], (str, float, int))

def _subarrays_must_be_equal(m):
    """each sub-array in y1 and y2 must have the same length as the others"""
    must_equal = ["y1", "y2"]#, "sweep_label", ]
    for i in must_equal:
        for ind,arr in enumerate(m['y1']):
            _check_len_equals(m['y1'][ind], m[i][ind])

def _check_dim_x_dim_each_y_arr(m):
    """length of the x array must equal the length of EACH sub array in y1 and y2"""
    for i in m['y1']:
        _check_len_equals(m['x'], i)
    for i in m['y2']:
        _check_len_equals(m['x'], i)

def _validate_data_len_and_type(m):
    """verify that the map passed in has appropriate dimensions and types"""
    m = m.copy()
    not_num_or_string = ['x', 'y1', 'y2']
    for i in not_num_or_string:
        _check_is_not_num_or_string(m[i])
    _subarrays_must_be_equal(m)
    _must_be_num_or_string(m)
    _check_dim_x_dim_each_y_arr(m)

def validate_plot_data():
    """integration test. This will be used"""
    pass
