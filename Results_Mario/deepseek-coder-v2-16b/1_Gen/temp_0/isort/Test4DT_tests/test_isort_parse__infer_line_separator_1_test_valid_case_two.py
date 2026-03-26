
import pytest
from isort.parse import _infer_line_separator

def test_valid_case_two():
    assert _infer_line_separator("Line 1\r\nLine 2\r\nLine 3") == "\r\n"
    assert _infer_line_separator("Line 1\rLine 2\rLine 3") == "\r"
    assert _infer_line_separator("Line 1\nLine 2\nLine 3") == "\n"
