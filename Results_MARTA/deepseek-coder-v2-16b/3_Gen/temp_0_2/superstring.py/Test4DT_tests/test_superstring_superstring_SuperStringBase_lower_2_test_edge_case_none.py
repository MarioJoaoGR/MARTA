
from unittest.mock import patch
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

class TestSuperStringBase:
    
    @patch('superstring.superstring.SuperStringBase.length', return_value=SUPERSTRING_MINIMAL_LENGTH - 1)
    def test_edge_case_none(self, mock_length):
        s = SuperStringBase()
        with pytest.raises(AttributeError):
            lower_str = s.lower()
