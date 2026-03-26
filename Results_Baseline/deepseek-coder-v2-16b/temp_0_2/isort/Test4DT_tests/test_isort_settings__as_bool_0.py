# Module: isort.settings
import pytest

from isort.settings import _as_bool


# Test case 1: Convert 'true' to True
def test_as_bool_true():
    assert _as_bool('true') == True

# Test case 2: Convert 'false' to False
def test_as_bool_false():
    assert _as_bool('false') == False

# Test case 3: Convert 'True' (case-insensitive) to True
def test_as_bool_true_case_insensitive():
    assert _as_bool('True') == True

# Test case 4: Convert 'False' (case-insensitive) to False
def test_as_bool_false_case_insensitive():
    assert _as_bool('False') == False

# Test case 5: Attempt to convert an invalid string, which will raise a ValueError
def test_as_bool_invalid_value():
    with pytest.raises(ValueError) as e:
        _as_bool('maybe')
    assert str(e.value) == "invalid truth value maybe"
