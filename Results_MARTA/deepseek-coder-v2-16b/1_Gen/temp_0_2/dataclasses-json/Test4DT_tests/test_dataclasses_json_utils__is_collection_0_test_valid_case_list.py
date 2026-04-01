
import pytest
from typing import List, Collection
from dataclasses_json.utils import _is_collection, _get_type_origin

def test_valid_case_list():
    my_list = List[int]
    assert _is_collection(my_list) == True
