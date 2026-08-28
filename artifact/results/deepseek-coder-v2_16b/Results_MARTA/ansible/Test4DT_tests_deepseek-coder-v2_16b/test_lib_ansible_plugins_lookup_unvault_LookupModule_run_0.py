
import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.lookup import unvault

# Fixture to create an instance of LookupModule for each test
@pytest.fixture
def lm():
    return unvault()

# Test scenario 1: Valid input
def test_valid_input(lm):
    terms = ['file1', 'file2']
    variables = {'search_path': '/path/to/search'}
    result = lm.run(terms, variables=variables)
    assert isinstance(result, list), "Expected a list of file contents"
    assert len(result) == 2, "Expected two files to be found"
    # Further assertions on the content of the files can be added here

# Test scenario 2: Edge case with None and empty lists as inputs
def test_edge_case(lm):
    terms = []
    variables = {}
    with pytest.raises(AnsibleParserError) as excinfo:
        lm.run(terms, variables=variables)
    assert "no matching files" in str(excinfo.value), "Expected an error about no matching files"

# Test scenario 3: Invalid input causing errors (e.g., file not found)
def test_invalid_input(lm):
    terms = ['nonexistentfile']
    variables = {'search_path': '/non/existent/path'}
    with pytest.raises(AnsibleParserError) as excinfo:
        lm.run(terms, variables=variables)
    assert "Unable to find file" in str(excinfo.value), "Expected an error about the nonexistent file"
