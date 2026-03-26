
import pytest
from collections import abc
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe

def test_invalid_input():
    # Arrange
    invalid_type = []
    
    # Act & Assert
    assert not _is_mapping(invalid_type), f"Expected _is_mapping({invalid_type}) to be False, but it returned True."
