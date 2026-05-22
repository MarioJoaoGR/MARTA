
import pytest
from unittest.mock import patch
from httpie.cli.dicts import MultiValueOrderedDict

def test_invalid_input():
    mvod = MultiValueOrderedDict()
    
    with pytest.raises(AssertionError):
        mvod['key'] = [1, 2, 3]
