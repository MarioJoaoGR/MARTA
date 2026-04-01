
from typing import Any, Dict

import pytest

from isort._vendored.tomli._parser import ParseFloat, loads


def test_invalid_input_raises_error():
    malformed_toml = 'invalid toml'
    with pytest.raises(Exception) as e:
        loads(malformed_toml)
    assert str(e.value).startswith("Expected "), f"Unexpected error message: {str(e.value)}"
