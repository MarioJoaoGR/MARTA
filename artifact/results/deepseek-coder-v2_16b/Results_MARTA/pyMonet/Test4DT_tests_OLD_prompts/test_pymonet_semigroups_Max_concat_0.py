
import pytest
from unittest.mock import patch
from pymonet.semigroups import Max


def test_normal_case():
    max1 = Max(5)
    max2 = Max(3)
    result = max1.concat(max2)
    assert result.value == 5

def test_same_values():
    max1 = Max(3)
    max2 = Max(3)
    result = max1.concat(max2)
    assert result.value == 3