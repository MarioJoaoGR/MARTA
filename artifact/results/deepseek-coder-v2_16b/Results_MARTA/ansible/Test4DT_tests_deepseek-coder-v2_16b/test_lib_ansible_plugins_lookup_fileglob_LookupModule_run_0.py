
import pytest
import os
import glob
from ansible.plugins.lookup import fileglob

@pytest.fixture(scope="module")
def valid_instance():
    terms = ['example.txt']
    variables = {}
    lookup_module = fileglob.LookupModule()
    return lookup_module, terms, variables

@pytest.fixture(scope="module")
def missing_lines_instance():
    terms = ['non_existent_file.txt']
    variables = {'ansible_search_path': []}
    lookup_module = fileglob.LookupModule()
    return lookup_module, terms, variables

@pytest.fixture(scope="module")
def invalid_input_instance():
    terms = [None]
    variables = {}
    lookup_module = fileglob.LookupModule()
    return lookup_module, terms, variables

def test_valid_input(valid_instance):
    lookup_module, terms, variables = valid_instance
    result = lookup_module.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) > 0, "Expected at least one file path to be found"
    for path in result:
        assert os.path.isfile(path), f"Expected {path} to be a valid file"

def test_missing_lines(missing_lines_instance):
    lookup_module, terms, variables = missing_lines_instance
    result = lookup_module.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) == 0, "Expected no files to be found for non-existent term"

def test_invalid_input(invalid_input_instance):
    lookup_module, terms, variables = invalid_input_instance
    result = lookup_module.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) == 0, "Expected no files to be found for invalid input term"
