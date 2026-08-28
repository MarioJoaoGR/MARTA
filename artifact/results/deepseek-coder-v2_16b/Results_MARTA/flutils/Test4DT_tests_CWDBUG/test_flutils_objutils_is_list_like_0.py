
import pytest
from flutils.objutils import is_list_like

# Test scenarios
def test_valid_case_list():
    real_instance = [1, 2, 3]
    assert is_list_like(real_instance) == True

def test_valid_case_iterator():
    real_instance = reversed([1, 2, 4])
    assert is_list_like(real_instance) == True

def test_invalid_case_string():
    invalid_input = 'hello'
    assert is_list_like(invalid_input) == False
