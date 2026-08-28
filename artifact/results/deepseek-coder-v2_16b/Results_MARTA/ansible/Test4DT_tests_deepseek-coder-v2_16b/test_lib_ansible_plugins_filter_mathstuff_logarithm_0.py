
import pytest
from ansible.errors import AnsibleFilterTypeError
import math
from ansible.plugins.filter.mathstuff import logarithm

def test_logarithm_default_base():
    assert logarithm(10) == math.log(10)  # Default base is math.e, so this computes the natural logarithm of 10

def test_logarithm_common_base():
    assert logarithm(10, 10) == math.log10(10)  # Computes the common logarithm (base 10) of 10

def test_logarithm_custom_base():
    assert logarithm(8, 2) == math.log(8, 2)  # Computes the logarithm (base 2) of 8
