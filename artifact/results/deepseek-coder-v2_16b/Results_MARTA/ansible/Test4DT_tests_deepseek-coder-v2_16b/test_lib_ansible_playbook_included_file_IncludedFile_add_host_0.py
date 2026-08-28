
import pytest
from ansible.playbook.included_file import IncludedFile

# Test adding a valid host to the included file
def test_valid_input():
    included_file = IncludedFile('example.txt', {'arg1': 'value1'}, {'var1': 'value1'}, 'task1')
    included_file.add_host('server1')
    assert 'server1' in included_file._hosts

# Test raising ValueError when adding an existing host
def test_error_case():
    included_file = IncludedFile('example.txt', {'arg1': 'value1'}, {'var1': 'value1'}, 'task1')
    included_file.add_host('server1')
    with pytest.raises(ValueError):
        included_file.add_host('server1')

# Test adding an invalid host type to raise TypeError
def test_invalid_input():
    included_file = IncludedFile('example.txt', {'arg1': 'value1'}, {'var1': 'value1'}, 'task1')
    with pytest.raises(TypeError):
        included_file.add_host(12345)  # Adding an integer instead of a string host
