
import pytest
from string_utils.validation import is_pangram  # Assuming the module is named string_utils and contains a validation submodule

def test_not_pangram():
    assert not is_pangram('hello world')
