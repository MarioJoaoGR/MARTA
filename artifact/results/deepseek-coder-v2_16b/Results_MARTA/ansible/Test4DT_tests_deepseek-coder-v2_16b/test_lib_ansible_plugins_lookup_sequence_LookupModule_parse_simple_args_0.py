
import pytest
from ansible.plugins.lookup.sequence import LookupModule

def test_valid_simple_args():
    lookup_module = LookupModule()
    term = "5-8"
    assert lookup_module.parse_simple_args(term) is True
    assert lookup_module.start == 5
    assert lookup_module.end == 8
    assert getattr(lookup_module, 'stride', None) is None


