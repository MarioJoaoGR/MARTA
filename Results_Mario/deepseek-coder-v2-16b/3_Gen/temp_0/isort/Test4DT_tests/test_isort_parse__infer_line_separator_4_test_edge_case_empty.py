
import pytest


def _infer_line_separator(contents: str) -> str:
    if "\r\n" in contents:
        return "\r\n"
    if "\r" in contents:
        return "\r"
    return "\n"

@pytest.mark.parametrize("input_string, expected", [
    ("", "\n"),  # Edge case with empty string input
])
def test_edge_case_empty(input_string, expected):
    assert _infer_line_separator(input_string) == expected
