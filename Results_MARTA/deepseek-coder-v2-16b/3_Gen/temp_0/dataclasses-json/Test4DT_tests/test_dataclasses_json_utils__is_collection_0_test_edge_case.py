
import pytest
from typing import Collection
from dataclasses_json.utils import _is_collection, _get_type_origin, _issubclass_safe

def test_edge_case():
    # Test when input is None
    assert not _is_collection(None)
