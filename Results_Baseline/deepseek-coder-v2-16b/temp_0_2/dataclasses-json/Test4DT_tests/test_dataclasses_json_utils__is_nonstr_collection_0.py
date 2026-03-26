# Module: dataclasses_json.utils
# Import the function using its provided module name.
from dataclasses_json.utils import _is_nonstr_collection
from typing import List, Union, Collection
import pytest

# Test cases for _is_nonstr_collection function
def test_is_nonstr_collection_list():
    assert _is_nonstr_collection(List[int]) == True

def test_is_nonstr_collection_union():
    mixed_types = Union[int, str]
    assert _is_nonstr_collection(mixed_types) == False

def test_is_nonstr_collection_custom_class():
    class MyCollection: pass
    assert _is_nonstr_collection(MyCollection) == False

# Additional edge cases to consider
def test_is_nonstr_collection_string():
    # Check if a string is considered a non-string collection
    assert _is_nonstr_collection(str) == False

def test_is_nonstr_collection_none_type():
    # Check with None type, which should not be a non-string collection
    assert _is_nonstr_collection(None) == False

def test_is_nonstr_collection_primitive_type():
    # Check with primitive types like int and float to ensure they are not considered collections
    assert _is_nonstr_collection(int) == False
    assert _is_nonstr_collection(float) == False

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
