
import pytest
from ansible.plugins.filter.core import subelements
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError




def test_invalid_object_type():
    obj = "not a dictionary or list"
    with pytest.raises(AnsibleFilterError):
        subelements(obj, 'groups')

def test_invalid_subelements_type():
    obj = {"users": [{"name": "eve", "groups": ["wheel"], "authorized": ["/tmp/eve/onekey.pub"]}]}
    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, 12345)