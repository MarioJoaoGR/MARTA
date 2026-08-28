
import math
from ansible.plugins.filter.mathstuff import logarithm
import pytest
from unittest.mock import patch
from ansible.errors import AnsibleFilterTypeError

def test_logarithm_basic():
    with patch('ansible.plugins.filter.mathstuff.math.log', return_value=1.0):
        assert logarithm(10) == 1.0

