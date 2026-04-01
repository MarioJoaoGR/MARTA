
import pytest
from dataclasses import dataclass, is_dataclass
from typing import get_type_hints, Generic, TypeVar
from dataclasses_json.utils import _is_generic_dataclass, _get_type_origin

@pytest.mark.skip(reason="This test should be implemented to check if a non-generic dataclass is incorrectly recognized as generic.")
def test_invalid_case_non_generic_dataclass():
    class MyDataClass: pass
    
    my_data_class = MyDataClass()
    
    # Check if _is_generic_dataclass correctly identifies a non-generic dataclass
    assert not _is_generic_dataclass(MyDataClass)
