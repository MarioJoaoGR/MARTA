
import pytest

def _infer_line_separator(contents: str) -> str:
    if "\r\n" in contents:
        return "\r\n"
    if "\r" in contents:
        return "\r"
    return "\n"

@pytest.mark.parametrize("input_string, expected", [
    ("", "\n"),  # Test with empty string
    ("Hello\r\nWorld", "\r\n"),  # Test with \r\n separator
    ("Hello\rWorld", "\r"),  # Test with \r separator
    ("Hello\nWorld", "\n")  # Test with \n separator
])
def test_edge_case_empty(input_string, expected):
    assert _infer_line_separator(input_string) == expected
