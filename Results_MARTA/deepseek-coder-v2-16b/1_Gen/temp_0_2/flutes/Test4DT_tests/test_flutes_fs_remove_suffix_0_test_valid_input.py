
import pytest
from flutes.fs import remove_suffix

def test_valid_input():
    assert remove_suffix("https://github.com/huzecong/flutes", "/flutes") == "https://github.com/huzecong"
    assert remove_suffix("bugfix", "suffix", fully_match=False) == "bug"
