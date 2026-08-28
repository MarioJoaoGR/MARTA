# Module: ansible.utils.collection_loader._collection_finder
# test_collection_loader.py
from ansible.utils.collection_loader._collection_finder import import_module
import pytest
import sys

@pytest.mark.parametrize("module_name, expected", [
    ('math', sys.modules['math']),  # Test importing a standard library module
    ('os', sys.modules['os']),      # Test importing another standard library module
    ('collections', sys.modules['collections'])  # Another standard library module
])
def test_import_module(module_name, expected):
    """
    Test the import_module function with various module names and check if they are correctly imported.
    
    Args:
        module_name (str): The name of the module to import.
        expected: The expected result after importing the module.
    """
    assert import_module(module_name) == expected
