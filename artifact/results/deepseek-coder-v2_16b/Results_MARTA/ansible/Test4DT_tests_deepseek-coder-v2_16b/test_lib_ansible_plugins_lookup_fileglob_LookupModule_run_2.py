
import pytest
from ansible.plugins.lookup.fileglob import LookupModule
import os
import glob
from unittest.mock import patch, MagicMock

@pytest.fixture(scope="module")
def lookup_module():
    return LookupModule()

# Test for valid input with default role path

# Test for valid input with specified role path via kwargs

# Test for valid input with specified role path via variables
def test_valid_input_with_specified_role_path_variables(lookup_module):
    terms = ['example.txt']
    variables = {'ansible_search_path': '/some/custom/path'}
    result = lookup_module.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) == 0, f"Expected no files to be found, but got {result}"

# Test for valid input with specified role path via both kwargs and variables
def test_valid_input_with_combined_role_path(lookup_module):
    terms = ['example.txt']
    variables = {'ansible_search_path': '/some/custom/path'}
    kwargs = {'ansible_search_path': '/another/custom/path'}
    result = lookup_module.run(terms, variables=variables, **kwargs)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) == 0, f"Expected no files to be found, but got {result}"