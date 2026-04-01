
import pytest
from pymonet.semigroups import Max

def test_valid_case():
    max_monoid = Max(value=-float('inf'))
    assert str(max_monoid) == 'Max[value=-inf]'
