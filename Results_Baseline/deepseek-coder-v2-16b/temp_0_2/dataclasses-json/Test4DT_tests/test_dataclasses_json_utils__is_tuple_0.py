# Module: dataclasses_json.utils
import pytest
from typing import List, Tuple
from dataclasses_json.utils import _is_tuple

# Test cases for _is_tuple function
def test_is_tuple_builtin():
    assert not _is_tuple(list), "Expected False as list is not a subclass of Tuple"

def test_is_tuple_generic():
    from typing import List
    assert not _is_tuple(List[int]), "Expected False as List[int] is not a subclass of Tuple"

def test_is_tuple_specific():
    from typing import Tuple
    assert _is_tuple(Tuple[int, str]), "Expected True as Tuple[int, str] is a subclass of Tuple"
