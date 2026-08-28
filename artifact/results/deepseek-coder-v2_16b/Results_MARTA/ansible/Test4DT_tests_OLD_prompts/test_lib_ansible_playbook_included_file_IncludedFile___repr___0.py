
import pytest
from ansible.playbook.included_file import IncludedFile



def test_with_is_role():
    included_file = IncludedFile("example_file.txt", {'arg1': 'value1'}, {'var1': 'value1'}, 'task1', is_role=True)
    assert hasattr(included_file, '_is_role')  # Ensure _is_role is present when set to True