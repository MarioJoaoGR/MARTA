
import pytest
from isort.parse import _infer_line_separator

def test_valid_input_crlf():
    assert _infer_line_separator("Hello\r\nWorld") == "\r\n"
    assert _infer_line_separator("Hello\rWorld") == "\r"
    assert _infer_line_separator("Hello\nWorld") == "\n"
    assert _infer_line_separator("HelloWorld") == "\n"
