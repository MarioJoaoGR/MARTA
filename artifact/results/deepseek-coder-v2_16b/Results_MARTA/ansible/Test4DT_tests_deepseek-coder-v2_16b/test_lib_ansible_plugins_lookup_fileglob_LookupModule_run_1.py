
import pytest
from ansible.plugins.lookup import fileglob
import os
import glob

@pytest.fixture(scope="module")
def lookup_module():
    return fileglob.LookupModule()


def test_invalid_input(lookup_module):
    terms = ['nonexistent.txt']
    variables = {'ansible_search_path': ['/path/to/search1', '/path/to/search2']}
    result = lookup_module.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file paths"
    assert len(result) == 0, "No files should be found for an invalid term"