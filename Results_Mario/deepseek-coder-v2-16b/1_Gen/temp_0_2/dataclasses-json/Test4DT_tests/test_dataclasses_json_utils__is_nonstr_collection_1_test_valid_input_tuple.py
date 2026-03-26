
import pytest
from typing import Tuple, List, Set, Dict
from dataclasses_json.utils import _is_nonstr_collection, _get_type_origin, _issubclass_safe

def test_valid_input_tuple():
    assert _is_nonstr_collection(Tuple[int, ...]) == True
