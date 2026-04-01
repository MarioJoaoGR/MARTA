
import io
from flutes.io import _ProgressBufferedReader, BarFn
import pytest

@pytest.mark.parametrize("buffer_size", [1024, 2048])
def test_invalid_input(buffer_size):
    raw = io.BytesIO()
    with pytest.raises(TypeError) as excinfo:
        reader = _ProgressBufferedReader(raw, buffer_size=buffer_size)
    assert "missing 1 required positional argument" in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ProgressBufferedReader_readline_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_io__ProgressBufferedReader_readline_0_test_invalid_input.py:10:17: E1125: Missing mandatory keyword argument 'bar_fn' in constructor call (missing-kwoa)


"""