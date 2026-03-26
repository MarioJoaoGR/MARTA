
import pytest
from dataclasses_json.utils import _NoArgs

def test_edge_case():
    no_args_iterator = _NoArgs()
    with pytest.raises(StopIteration):
        next(iter(no_args_iterator))
