# plotting helper functions
import numpy as np
import pyabf


def _check_len_equals(x, y):
    """raises assertion error if len(x) != len(y)"""
    assert len(x) == len(y)


def _check_is_not_num_or_string(x):
    """raises assertion error is type is not expected. Type should be numpy array or list.
    Can be an empty list."""
    assert not isinstance(x, (str, float, int, type(None)))


def _must_be_num_or_string(m):
    """These keys must be an int, float or string, cannot be a container (list, tuple, numpy array, etc.)"""
    must_be_num_or_string = ["x_label", "y1_label", "y2_label", "fontsize", "linewidth"]
    try:
        for i in must_be_num_or_string:
            assert isinstance(m[i], (str, float, int))
    except KeyError as e:
        print("`_must_be_num_or_string` missing key! Error is: {e}")
        raise (KeyError("Missing key in `_must_be_num_or_string`"))


def _subarrays_must_be_equal(m):
    """each sub-array in y1 and y2 must have the same length as the others"""
    must_equal = ["y1", "y2"]  # , "sweep_label", ]
    try:
        for i in must_equal:
            for ind, arr in enumerate(m["y1"]):
                _check_len_equals(m["y1"][ind], m[i][ind])
    except KeyError as e:
        print("`_subarrays_must_be_equal` missing key! Error is: {e}")
        raise (KeyError("Missing key in `_subarrays_must_be_equal"))


def _check_dim_x_dim_each_y_arr(m):
    """length of the x array must equal the length of EACH sub array in y1 and y2"""
    try:
        assert len(m["y1"]) == len(m["y2"])
        for i in m["y1"]:
            _check_len_equals(m["x"], i)
            for i in m["y2"]:
                _check_len_equals(m["x"], i)
    except AssertionError as e:
        print(f"error with data {m}")
        raise (AssertionError)


def validate_plot_data(m):
    """integration test of other fns"""
    not_num_or_string = ["y1", "y2"]
    assert len(m["y1"]) == len(m["sweep_label"])
    assert len(m["y2"]) == len(m["sweep_label"])
    for i in not_num_or_string:
        _check_is_not_num_or_string(m[i])
    _subarrays_must_be_equal(m)
    _must_be_num_or_string(m)
    _check_dim_x_dim_each_y_arr(m)


def _make_string_label(base, suffix):
    b = base.replace(".abf", "")
    label = f"{suffix} {b}"
    return label


def _calculate_mean_sweeps(abf):
    acc = []
    for sweep in abf.sweepList:
        abf.setSweep(sweep)
        acc.append(abf.sweepY)
    return np.asarray(acc).mean(axis=0)


def build_plot_map(current_meta_dict, current_plot_options):
    # current_meta_dict is a field in TkAbfExplorer
    # current_plot_options is a field in PlotFrame
    abf = pyabf.ABF(current_meta_dict["file_path"])
    abf.setSweep(sweepNumber=current_meta_dict["sweep"], channel=0)
    print(f">>> current_meta_dict from `build_plot_map` is {current_meta_dict}")
    current_plot_options["x"] = abf.sweepX
    current_plot_options["x_label"] = abf.sweepLabelX
    current_plot_options["y1_label"] = abf.sweepLabelY
    if current_meta_dict["plot_mean_state"] == True:
        current_plot_options["sweep_label"].append(
            _make_string_label(current_meta_dict["file_name"], "mean of all sweeps")
        )
        current_plot_options["y1"].append(_calculate_mean_sweeps(abf))
    if current_meta_dict["plot_mean_state"] == False:
        current_plot_options["sweep_label"].append(
            _make_string_label(
                current_meta_dict["file_name"], f"sweep {current_meta_dict['sweep']}"
            )
        )
        current_plot_options["y1"].append(abf.sweepY)
    if current_meta_dict["bottom_plot"] == "c":
        current_plot_options["y2"].append(abf.sweepC)
        current_plot_options["y2_label"] = "command waveform"
    if current_meta_dict["bottom_plot"] == 1:
        abf.setSweep(sweepNumber=current_meta_dict["sweep"], channel=1)
        current_plot_options["y2"].append(abf.sweepY)
        current_plot_options["y2_label"] = "channel 1"
    try:
        validate_plot_data(current_plot_options)
    except Exception as e:
        print(f"[ERROR in `plotting.validate_plot_data`]: Exception:\n\n {e}\n\n")
        raise IndexError("inequal length axis")
    return current_plot_options
