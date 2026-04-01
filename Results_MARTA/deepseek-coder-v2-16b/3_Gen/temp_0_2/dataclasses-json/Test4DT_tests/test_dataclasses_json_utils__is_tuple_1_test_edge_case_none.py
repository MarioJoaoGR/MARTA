
import pytest
from dataclasses_json.utils import _is_tuple
from typing import Tuple

def test_edge_case_none():
    # Test when type is None
    assert not _is_tuple(None)
