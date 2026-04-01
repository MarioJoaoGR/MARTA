
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_input():
    no_args = _NoArgs()
    assert not bool(no_args), "The __bool__ method should return False"
