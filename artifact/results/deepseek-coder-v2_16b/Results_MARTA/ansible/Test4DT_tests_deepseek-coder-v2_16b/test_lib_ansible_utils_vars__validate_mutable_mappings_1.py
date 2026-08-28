
import pytest
from ansible.utils.vars import _validate_mutable_mappings
from collections.abc import MutableMapping
from ansible.errors import AnsibleError
from json import dumps
from pprint import pformat



def test_non_dictionary_input():
    with pytest.raises(AnsibleError):
        a = "not a dictionary"
        b = 42
        _validate_mutable_mappings(a, b)