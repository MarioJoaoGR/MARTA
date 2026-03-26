
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_case():
    no_args = _NoArgs()
    assert len(no_args) == 0, "Expected length to be 0 for an instance of _NoArgs"
