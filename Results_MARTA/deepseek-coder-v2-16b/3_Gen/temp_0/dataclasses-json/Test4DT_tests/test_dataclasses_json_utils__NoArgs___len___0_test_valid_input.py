
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_input():
    instance = _NoArgs()
    assert len(instance) == 0, "The length of an instance of _NoArgs should always be 0"
