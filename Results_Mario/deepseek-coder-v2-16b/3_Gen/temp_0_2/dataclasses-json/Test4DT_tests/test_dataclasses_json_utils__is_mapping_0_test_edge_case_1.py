
import pytest
from dataclasses_json.utils import _is_mapping
from collections.abc import Mapping
from typing import Type

def test_edge_case_1():
    class MyDict(dict): pass
    assert _is_mapping(MyDict) == True, "Expected MyDict to be a mapping"
    
    class MyList(list): pass
    assert _is_mapping(MyList) == False, "Expected MyList not to be a mapping"
    
    assert _is_mapping(dict) == True, "Expected dict to be a mapping"
