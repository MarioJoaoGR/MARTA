
import pytest
from ansible.utils.collection_loader._collection_finder import is_python_identifier

def test_valid_case_lowercase():
    assert is_python_identifier("my_variable")  # True


def test_edge_case_none():
    with pytest.raises(TypeError):
        is_python_identifier(None)  # Should raise TypeError