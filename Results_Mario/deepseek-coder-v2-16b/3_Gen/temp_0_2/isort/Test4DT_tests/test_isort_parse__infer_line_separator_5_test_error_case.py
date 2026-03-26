
import pytest
from isort.parse import _infer_line_separator

def test_infer_line_separator():
    assert _infer_line_separator("Hello\r\nWorld") == "\r\n"
    assert _infer_line_separator("Hello\rWorld") == "\r"
    assert _infer_line_separator("Hello\nWorld") == "\n"
