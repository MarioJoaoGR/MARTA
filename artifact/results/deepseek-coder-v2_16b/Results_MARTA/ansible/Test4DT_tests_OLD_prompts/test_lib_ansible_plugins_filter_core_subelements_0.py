
import pytest
from ansible.plugins.filter.core import subelements
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError




def test_error_case_1():
    obj = 'not a dictionary or list'
    with pytest.raises(AnsibleFilterError) as e:
        subelements(obj, 'groups')
    assert str(e.value) == "obj must be a list of dicts or a nested dict"