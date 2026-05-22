
import pytest
from httpie.utils import JsonDictPreservingDuplicateKeys
from unittest.mock import patch

def test_invalid_input():
    with patch('httpie.utils.JsonDictPreservingDuplicateKeys.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            items = 'not an iterable'
            JsonDictPreservingDuplicateKeys(items)
