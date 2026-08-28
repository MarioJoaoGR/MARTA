
import pytest
from ansible.plugins.filter.mathstuff import power
from ansible.errors import AnsibleFilterTypeError
import math
from unittest.mock import patch

def test_valid_inputs():
    with patch('ansible.plugins.filter.mathstuff.power', return_value=8.0):
        assert power(2, 3) == 8.0
        assert power(4, 0.5) == 2.0

def test_invalid_inputs():
    with pytest.raises(AnsibleFilterTypeError):
        power('a', 'b')
