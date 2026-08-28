
import pytest
from ansible.utils.collection_loader._collection_finder import is_python_identifier

def test_valid_identifiers():
    assert is_python_identifier("my_variable") == True
    assert is_python_identifier("_underscore") == True
