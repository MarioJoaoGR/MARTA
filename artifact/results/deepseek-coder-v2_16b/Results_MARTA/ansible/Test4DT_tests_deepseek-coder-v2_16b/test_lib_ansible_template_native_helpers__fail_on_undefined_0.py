
import pytest
from ansible.template.native_helpers import _fail_on_undefined, StrictUndefined
from collections.abc import Mapping, Sequence

def is_sequence(value):
    return isinstance(value, Sequence)



def test_defined_values():
    defined_data = {'a': 1, 'b': 2}
    assert _fail_on_undefined(defined_data) == defined_data