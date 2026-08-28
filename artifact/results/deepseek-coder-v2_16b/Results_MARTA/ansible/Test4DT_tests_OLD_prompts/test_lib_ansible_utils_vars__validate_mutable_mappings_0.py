
import pytest
from ansible.errors import AnsibleError
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping
from json import dumps
from ansible.module_utils._text import to_native



def test_validate_mutable_mappings_non_mapping():
    class NonMapping:
        pass
    
    non_map = NonMapping()
    
    with pytest.raises(AnsibleError):
        _validate_mutable_mappings({'key1': 'value1'}, non_map)

def test_validate_mutable_mappings_none():
    with pytest.raises(AnsibleError):
        _validate_mutable_mappings(None, None)