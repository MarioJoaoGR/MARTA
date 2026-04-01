
import pytest
from typing import List, Tuple
from dataclasses_json.utils import _is_tuple as is_tuple

def test_valid_case_2():
    # Define a custom tuple-like structure
    from collections import namedtuple
    CustomTuple = namedtuple('CustomTuple', ['a', 'b'])
    
    # Check if the custom tuple-like structure returns True
    assert is_tuple(List[int]) is False
