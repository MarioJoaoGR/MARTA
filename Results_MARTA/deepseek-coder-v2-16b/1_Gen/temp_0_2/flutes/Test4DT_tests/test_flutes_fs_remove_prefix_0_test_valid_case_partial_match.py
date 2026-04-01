
import pytest
from flutes.fs import remove_prefix

def test_valid_case_partial_match():
    assert remove_prefix("preface", "pre", fully_match=False) == "face"
    assert remove_prefix("https://github.com/huzecong/flutes", "https://", fully_match=False) == "github.com/huzecong/flutes"
