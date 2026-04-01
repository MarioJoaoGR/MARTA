
import pytest
import urllib.request
from flutes.network import _download
import os

@pytest.mark.parametrize("url, filename, path", [
    (12345, "file.zip", "/path/to/save"),
    ("http://example.com/file.zip", 12345, "/path/to/save"),
    ("http://example.com/file.zip", "", "/path/to/save"),
])
def test_invalid_inputs(url, filename, path):
    with pytest.raises(TypeError) as excinfo:
        _download(url, filename, path)
    assert str(excinfo.value) == "filename must be a string"

@pytest.mark.parametrize("url, filename, path", [
    (12345, "file.zip", "/path/to/save"),
    ("http://example.com/file.zip", 12345, "/path/to/save"),
    ("http://example.com/file.zip", "file.zip", 12345),
])
def test_invalid_inputs(url, filename, path):
    with pytest.raises(TypeError) as excinfo:
        _download(url, filename, path)
    assert str(excinfo.value) == "path must be a string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network__download_2_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_network__download_2_test_invalid_inputs.py:22:0: E0102: function already defined line 12 (function-redefined)


"""