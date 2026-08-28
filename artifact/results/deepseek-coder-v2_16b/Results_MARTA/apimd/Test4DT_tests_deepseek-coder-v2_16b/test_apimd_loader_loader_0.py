
import pytest
from apimd.loader import loader
from os.path import isfile
from pkgutil import walk_packages
from unittest.mock import patch, MagicMock

# Test for edge case where root and pwd are None
def test_edge_case():
    with pytest.raises(TypeError):
        result = loader(None, None, False, 1, False)
