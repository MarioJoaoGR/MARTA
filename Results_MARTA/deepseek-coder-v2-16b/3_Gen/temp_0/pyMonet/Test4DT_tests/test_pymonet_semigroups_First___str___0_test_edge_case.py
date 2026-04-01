
# Assuming the directory structure and import paths are correct, this should work if 'pymonet.semigroups' is properly defined elsewhere.
import pytest
from pymonet.semigroups import First  # Adjust the import path as necessary based on actual project structure

def test_str_representation():
    first = First(5)
    assert str(first) == 'Fist[value=5]'
