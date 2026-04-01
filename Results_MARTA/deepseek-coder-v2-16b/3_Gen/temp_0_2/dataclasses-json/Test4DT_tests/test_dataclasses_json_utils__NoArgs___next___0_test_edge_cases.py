
import pytest
from dataclasses_json.utils import _NoArgs

def test_edge_cases():
    no_args = _NoArgs()
    with pytest.raises(StopIteration):
        next(no_args)
