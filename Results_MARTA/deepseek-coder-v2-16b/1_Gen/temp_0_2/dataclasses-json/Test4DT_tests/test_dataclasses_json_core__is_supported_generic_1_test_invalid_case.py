
import pytest
from typing import List, Union, Optional
from dataclasses_json.core import _is_supported_generic, _NO_ARGS

def test_invalid_case():
    # Test when type_ is str
    assert not _is_supported_generic(str)
