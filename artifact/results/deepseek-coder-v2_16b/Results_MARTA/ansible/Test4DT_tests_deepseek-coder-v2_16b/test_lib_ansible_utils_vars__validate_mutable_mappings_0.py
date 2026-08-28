
import pytest
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping
from ansible.errors import AnsibleError
from json import dumps
from ansible.module_utils._text import to_native


def test_validate_mutable_mappings_with_invalid_types():
    with pytest.raises(AnsibleError):
        _validate_mutable_mappings('not a dictionary', 42)

def test_validate_mutable_mappings_with_non_dict_objects():
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    with pytest.raises(AnsibleError):
        _validate_mutable_mappings(dict1, "not a dictionary")

