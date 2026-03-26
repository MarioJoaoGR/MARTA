
import pytest
from dataclasses_json.utils import _NoArgs

def test_invalid_input():
    no_args = _NoArgs()
    assert not bool(no_args), "Expected instance of _NoArgs to evaluate to False in boolean context"
