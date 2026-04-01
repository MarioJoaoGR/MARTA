
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_case():
    no_args = _NoArgs()
    assert not no_args, "Expected _NoArgs to evaluate to False"
