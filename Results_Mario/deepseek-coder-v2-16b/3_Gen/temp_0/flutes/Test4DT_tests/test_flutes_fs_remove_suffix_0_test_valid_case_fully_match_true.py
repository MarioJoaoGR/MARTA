
import pytest
from flutes.fs import remove_suffix

def test_valid_case_fully_match_true():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "fix", fully_match=False) == "bug"
