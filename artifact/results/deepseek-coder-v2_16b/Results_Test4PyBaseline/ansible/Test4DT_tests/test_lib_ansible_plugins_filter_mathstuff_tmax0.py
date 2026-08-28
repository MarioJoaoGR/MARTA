# Module: ansible.plugins.filter.mathstuff
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterError

# Mock HAS_MIN_MAX and do_max for testing purposes
HAS_MIN_MAX = True
def do_max(environment, a, **kwargs):
    return max(a)

@pytest.fixture
def environment():
    return {'a': 1, 'b': 2}

def test_max_with_list_of_integers(environment):
    result = mathstuff.max(environment, [3, 4, 5])
    assert result == 5

def test_max_with_single_integer(environment):
    result = mathstuff.max(environment, 7)
    assert result == 7

def test_max_with_unsupported_keyword():
    with pytest.raises(AnsibleFilterError) as excinfo:
        mathstuff.max({}, [], keyword=True)
    assert str(excinfo.value) == "Ansible's max filter does not support any keyword arguments. You need Jinja2 2.10 or later that provides their version of the filter."
