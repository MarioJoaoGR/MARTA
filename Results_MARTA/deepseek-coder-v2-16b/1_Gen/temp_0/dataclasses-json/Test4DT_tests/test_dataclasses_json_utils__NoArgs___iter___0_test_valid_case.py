
import pytest
from dataclasses_json.utils import _NoArgs

def test_valid_case():
    no_args = _NoArgs()
    iterator = iter(no_args)
    with pytest.raises(StopIteration):
        next(iterator)
