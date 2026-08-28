
import pytest
from ansible.cli.doc import DocCLI

# Test valid input scenario
def test_valid_input():
    # Setup a real instance of DocCLI with minimal args, version_added set to '2.9' and version_added_collection set to 'ansible.builtin'
    doc_cli = DocCLI(args=['--minimal'])
    doc_cli.version_added = '2.9'
    doc_cli.version_added_collection = 'ansible.builtin'
    
    # Call the method under test
    result = DocCLI._format_version_added('2.9', 'ansible.builtin')
    
    # Assert the expected output
    assert result == 'version 2.9 of ansible-core'

# Test edge case with None input scenario
def test_edge_case_none():
    # Setup a real instance of DocCLI with minimal args, version_added set to None
    doc_cli = DocCLI(args=['--minimal'])
    doc_cli.version_added = None
    
    # Call the method under test
    result = DocCLI._format_version_added(None)
    
    # Assert the expected output
    assert result == ''

# Test invalid input causing ValueError scenario
def test_invalid_input():
    # Setup a real instance of DocCLI with minimal args, version_added set to None
    doc_cli = DocCLI(args=['--minimal'])
    
    # Call the method under test and expect it to raise ValueError
    with pytest.raises(ValueError):
        DocCLI._format_version_added('invalid_input')
