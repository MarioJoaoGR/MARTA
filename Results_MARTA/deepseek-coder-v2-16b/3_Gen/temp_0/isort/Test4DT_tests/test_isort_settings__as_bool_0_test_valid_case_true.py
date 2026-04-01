
# Import necessary modules
import pytest

from isort import settings as isort_settings


def test_valid_case_true():
    # Test cases for valid true values
    assert isort_settings._as_bool('true') == True
    assert isort_settings._as_bool('True') == True
    assert isort_settings._as_bool('TRUE') == True
    assert isort_settings._as_bool('yes') == True
    assert isort_settings._as_bool('Yes') == True
    assert isort_settings._as_bool('YES') == True
    assert isort_settings._as_bool('on') == True
    assert isort_settings._as_bool('On') == True
    assert isort_settings._as_bool('ON') == True
    assert isort_settings._as_bool('1') == True
    
    # Test cases for valid false values
    assert isort_settings._as_bool('false') == False
    assert isort_settings._as_bool('False') == False
    assert isort_settings._as_bool('FALSE') == False
    assert isort_settings._as_bool('no') == False
    assert isort_settings._as_bool('No') == False
    assert isort_settings._as_bool('NO') == False
    assert isort_settings._as_bool('off') == False
    assert isort_settings._as_bool('Off') == False
    assert isort_settings._as_bool('OFF') == False
    assert isort_settings._as_bool('0') == False
    
    # Test case for invalid value
    with pytest.raises(ValueError) as excinfo:
        isort_settings._as_bool('maybe')
    assert str(excinfo.value) == "invalid truth value maybe"
