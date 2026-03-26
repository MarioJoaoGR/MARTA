
import pytest
from io import StringIO
from pathlib import Path
from typing import Any, TextIO
from isort.api import sort_code_string, Config, DEFAULT_CONFIG

def test_invalid_input():
    with pytest.raises(TypeError):
        code = 12345
        result = sort_code_string(code=code)
