
from isort._vendored.tomli._parser import NestedDict
import pytest

def test_edge_case():
    nd = NestedDict()
    assert nd.dict == {}
