
import pytest

def _infer_line_separator(contents: str) -> str:
    if "\r\n" in contents:
        return "\r\n"
    if "\r" in contents:
        return "\r"
    return "\n"

def test_edge_case_none():
    with pytest.raises(TypeError):
        _infer_line_separator(None)
