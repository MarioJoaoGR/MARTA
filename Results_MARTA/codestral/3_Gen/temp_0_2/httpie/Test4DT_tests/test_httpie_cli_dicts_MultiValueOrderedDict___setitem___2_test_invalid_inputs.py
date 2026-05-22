
import pytest
from collections import OrderedDict
from unittest.mock import patch

class MultiValueOrderedDict(OrderedDict):
    """Multi-value dict for URL parameters and form data."""
    def __setitem__(self, key, value):
        assert not isinstance(value, list)
        if key not in self:
            super().__setitem__(key, value)
        else:
            if not isinstance(self[key], list):
                super().__setitem__(key, [self[key]])
            self[key].append(value)

def test_invalid_inputs():
    mvod = MultiValueOrderedDict()
    
    with pytest.raises(AssertionError):
        mvod['test_key'] = ['invalid', 'input']
