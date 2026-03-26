# Module: dataclasses_json.utils
import pytest
from typing import List, Union
from collections.abc import Collection
from dataclasses_json.utils import _is_nonstr_collection, _get_type_origin, _issubclass_safe

# Test cases for _is_nonstr_collection function

def test_is_nonstr_collection_list():
    from typing import List
    assert _is_nonstr_collection(List[int]) == True

def test_is_nonstr_collection_union():
    from typing import Union
    assert _is_nonstr_collection(Union[int, str]) == False

def test_is_nonstr_collection_custom_class():
    class MyCollection: pass
    assert _is_nonstr_collection(MyCollection) == False  # Assuming MyCollection does not subclass Collection or is a subclass of str

# Helper functions for testing (assuming these are defined elsewhere in the module)
def test_get_type_origin():
    from typing import List
    origin = _get_type_origin(List[int])
    assert origin == list

def test_issubclass_safe():
    class Base: pass
    class SubClass(Base): pass
    assert _issubclass_safe(SubClass, Base) == True
    assert _issubclass_safe(int, Base) == False

# Additional edge cases can be added to cover more scenarios and potential issues
