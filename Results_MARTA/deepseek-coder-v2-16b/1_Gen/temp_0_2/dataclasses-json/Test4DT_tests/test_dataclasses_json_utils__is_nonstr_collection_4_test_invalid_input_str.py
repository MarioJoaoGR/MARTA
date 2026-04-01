
import pytest
from dataclasses_json.utils import _is_nonstr_collection

def test_invalid_input_str():
    # Test if a string is identified as a non-string collection
    assert not _is_nonstr_collection(str)  # str should return False
