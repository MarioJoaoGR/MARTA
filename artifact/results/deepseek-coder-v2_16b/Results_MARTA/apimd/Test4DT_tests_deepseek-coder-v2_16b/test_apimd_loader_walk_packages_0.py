
import pytest
from apimd.loader import loader
from os.path import isdir, join
from pkgutil import walk_packages
from unittest.mock import patch, MagicMock
import sys

# Test for edge case where root and pwd are None
def test_edge_case():
    with pytest.raises(TypeError):
        result = loader(None, None, False, 1, False)

# Test to check if API documentation is generated correctly for a valid input

# Test to check if the function raises NotImplementedError when called