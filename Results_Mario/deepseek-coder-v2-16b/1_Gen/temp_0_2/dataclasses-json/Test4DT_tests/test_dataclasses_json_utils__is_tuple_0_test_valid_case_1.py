
from dataclasses_json.utils import _is_tuple
import typing

def test_valid_case_1():
    my_tuple = typing.Tuple[int, str]
    assert _is_tuple(my_tuple) == True
