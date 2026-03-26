
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_input():
    no_args = _NoArgs()
    assert len(no_args) == 0, "Expected length of _NoArgs to be 0"
