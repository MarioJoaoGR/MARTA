
from dataclasses_json.utils import _NoArgs

def test_edge_case_none():
    no_args = _NoArgs()
    assert len(no_args) == 0
