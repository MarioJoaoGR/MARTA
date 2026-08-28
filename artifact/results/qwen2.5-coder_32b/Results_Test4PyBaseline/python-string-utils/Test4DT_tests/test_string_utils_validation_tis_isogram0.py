
import pytest
from string_utils.validation import is_isogram

def test_is_isogram_valid_isograms():
    assert is_isogram('dermatoglyphics'), "Test failed for 'dermatoglyphics'"
    assert is_isogram('isogram'), "Test failed for 'isogram'"
    assert is_isogram('lumberjacks'), "Test failed for 'lumberjacks'"
    assert is_isogram('background'), "Test failed for 'background'"
    assert is_isogram('downstream'), "Test failed for 'downstream'"

def test_is_isogram_invalid_isograms():
    assert not is_isogram('hello'), "Test failed for 'hello'"