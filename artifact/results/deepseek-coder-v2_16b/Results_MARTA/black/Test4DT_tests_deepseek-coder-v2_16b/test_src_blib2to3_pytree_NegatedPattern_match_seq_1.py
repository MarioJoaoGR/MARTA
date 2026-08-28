
import pytest
from blib2to3.pytree import NegatedPattern
import re


def test_invalid_case():
    with pytest.raises(AssertionError):
        NegatedPattern(content="not a BasePattern")