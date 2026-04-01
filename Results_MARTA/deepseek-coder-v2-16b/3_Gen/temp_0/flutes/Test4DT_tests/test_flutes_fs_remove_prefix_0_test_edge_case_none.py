
import pytest

def remove_prefix(s: str, prefix: str, fully_match: bool = True) -> str:
    length = min(len(s), len(prefix))
    prefix_len = next((idx for idx in range(length) if s[idx] != prefix[idx]), length)
    if not fully_match or prefix_len == len(prefix):
        return s[prefix_len:]
    return s

def test_edge_case_none():
    with pytest.raises(TypeError):
        remove_prefix(None, "http")
