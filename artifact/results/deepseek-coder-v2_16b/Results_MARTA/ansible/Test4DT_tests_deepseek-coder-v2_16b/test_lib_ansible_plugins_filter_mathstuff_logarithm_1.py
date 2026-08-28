
import pytest
from ansible.plugins.filter import mathstuff
import math

# Test for logarithm function with default base (natural logarithm)
def test_logarithm_default_base():
    assert mathstuff.logarithm(10) == math.log(10)

# Test for logarithm function with specified base 10 (common logarithm)
def test_logarithm_specified_base_10():
    assert mathstuff.logarithm(10, 10) == math.log10(10)

# Test for logarithm function with a custom base
def test_logarithm_custom_base():
    assert mathstuff.logarithm(8, 2) == math.log(8, 2)

# Test for invalid input (negative number) which should raise AnsibleFilterTypeError