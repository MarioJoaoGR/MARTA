
import pytest
from dataclasses_json.utils import _is_tuple
from typing import Tuple

def test_valid_case_happy_path():
    # Define a tuple type
    my_tuple = Tuple[int, str]
    
    # Test the function with the defined tuple
    assert _is_tuple(my_tuple) is True
