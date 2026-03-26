
import pytest
from typing import List, Tuple, Set, Dict
from dataclasses_json.utils import _is_nonstr_collection, _get_type_origin, _issubclass_safe

def test_valid_input_dict():
    assert _is_nonstr_collection(List[int]) == True
    assert _is_nonstr_collection(Tuple[int, ...]) == True
    assert _is_nonstr_collection(Set[int]) == True
    assert _is_nonstr_collection(Dict[int, str]) == True
    assert _is_nonstr_collection(str) == False
