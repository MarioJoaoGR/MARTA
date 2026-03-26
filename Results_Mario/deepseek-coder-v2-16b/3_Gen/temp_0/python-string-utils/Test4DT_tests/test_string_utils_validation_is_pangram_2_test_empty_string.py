
import pytest
from string_utils.validation import is_pangram

def test_empty_string():
    assert not is_pangram('')
    assert not is_pangram('     ')
    assert not is_pangram('   \t\n  ')
