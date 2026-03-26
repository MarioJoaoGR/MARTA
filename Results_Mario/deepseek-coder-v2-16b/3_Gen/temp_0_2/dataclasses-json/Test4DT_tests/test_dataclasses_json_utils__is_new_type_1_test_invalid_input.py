
import pytest
import inspect
from dataclasses_json.utils import _is_new_type

def test_invalid_input():
    type_ = None
    assert not _is_new_type(type_)
