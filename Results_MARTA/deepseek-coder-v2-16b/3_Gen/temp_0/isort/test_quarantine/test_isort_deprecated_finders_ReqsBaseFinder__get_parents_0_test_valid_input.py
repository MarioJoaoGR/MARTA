
import pytest
from isort.deprecated.finders import ReqsBaseFinder
from unittest.mock import MagicMock

def test_valid_input():
    # Create a mock Config object
    config = MagicMock()
    
    # Instantiate the finder with the mock config and path
    finder = ReqsBaseFinder(config=config, path=".")
    
    # Assert that the finder is not enabled initially
    assert not finder.enabled
    
    # Mock the _load_mapping method to return a dictionary
    finder._load_mapping = MagicMock(return_value={"file1": "content", "file2": "content"})
    
    # Call the _get_parents method to trigger the loading of names and mapping
    parents = list(finder._get_parents("initial/starting/directory"))
    
    # Assert that the finder is now enabled after calling _get_parents
    assert finder.enabled
    
    # Assert that the mapping and names are loaded correctly
    assert finder.mapping == {"file1": "content", "file2": "content"}
    assert finder.names == ["file1", "file2"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_ReqsBaseFinder__get_parents_0_test_valid_input.py:11:13: E0110: Abstract class 'ReqsBaseFinder' with abstract methods instantiated (abstract-class-instantiated)


"""