
import pytest
from ansible.utils.vars import load_options_vars

# Test case for when the version is provided as '2.9'
def test_load_options_vars_with_version():
    result = load_options_vars('2.9')
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert 'ansible_version' in result, "Expected the result to contain 'ansible_version' key."
    assert result['ansible_version'] == '2.9', f"Expected 'ansible_version' to be '2.9' but got {result['ansible_version']}."
    for attr in ['check', 'diff', 'forks', 'inventory', 'skip_tags', 'subset', 'tags', 'verbosity']:
        assert result.get(attr) is None, f"Expected '{attr}' to be None but it was not."

# Test case for when the version is provided as None
def test_load_options_vars_with_none():
    result = load_options_vars(None)
    assert isinstance(result, dict), "Expected a dictionary but got something else."
    assert 'ansible_version' in result, "Expected the result to contain 'ansible_version' key."