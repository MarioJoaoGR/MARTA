
import pytest
from pysnooper.tracer import get_path_and_source_from_frame
import inspect


def test_current_frame():
    frame = inspect.currentframe()
    path_and_source = get_path_and_source_from_frame(frame)
    assert isinstance(path_and_source, tuple), "Expected a tuple"
    file_name, source = path_and_source
    assert isinstance(file_name, str), "File name should be a string"
    assert isinstance(source, list), "Source should be a list of strings"
    assert len(source) > 0, "Source list should not be empty"

def test_specific_frame():
    def some_function():
        return get_path_and_source_from_frame(inspect.currentframe())
    
    path_and_source = some_function()
    assert isinstance(path_and_source, tuple), "Expected a tuple"
    file_name, source = path_and_source
    assert isinstance(file_name, str), "File name should be a string"
    assert isinstance(source, list), "Source should be a list of strings"
    assert len(source) > 0, "Source list should not be empty"