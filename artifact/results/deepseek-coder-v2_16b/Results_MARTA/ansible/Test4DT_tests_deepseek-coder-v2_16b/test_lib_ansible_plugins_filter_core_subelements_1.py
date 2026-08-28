
import pytest
from ansible.plugins.filter.core import subelements
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError

# Test for valid nested dotted accessor

# Test for valid list of accessors

# Test for skipping missing keys

# Test for invalid object type
def test_invalid_object_type():
    obj = "not a dictionary or list"
    with pytest.raises(AnsibleFilterError):
        subelements(obj, 'groups')

# Test for invalid subelements type
def test_invalid_subelements_type():
    obj = {"users": [{"name": "eve", "groups": ["wheel"], "authorized": ["/tmp/eve/onekey.pub"]}]}
    with pytest.raises(AnsibleFilterTypeError):
        subelements(obj, 12345)