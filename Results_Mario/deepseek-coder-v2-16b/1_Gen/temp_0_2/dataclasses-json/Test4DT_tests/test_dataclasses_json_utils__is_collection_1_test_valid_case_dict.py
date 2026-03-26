
import pytest
from typing import Dict

def test_valid_case_dict():
    from dataclasses_json.utils import _is_collection
    
    class MyCustomDict(Dict[str, int]):
        pass
    
    assert _is_collection(MyCustomDict) is True
