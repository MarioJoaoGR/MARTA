# Module: dataclasses_json.utils
# test_dataclasses_json_utils.py
from dataclasses_json.utils import _NoArgs

def test_no_args():
    no_args = _NoArgs()
    assert not bool(no_args), "Expected _NoArgs to evaluate to False in boolean context"
