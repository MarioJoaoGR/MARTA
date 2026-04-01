
import pytest
from io import StringIO
from isort.api import check_code_string, Config, DEFAULT_CONFIG
from pathlib import Path
from typing import Any, TextIO

@pytest.mark.parametrize("code", [
    "import os\nimport sys",  # Simple valid code string
    "import os\n# comment\nimport sys",  # Code with a comment
    "import os\n# isort: off\nimport sys",  # Code with isort skip directive
])
def test_valid_input(code):
    result = check_code_string(code=code)
    assert isinstance(result, bool), "The function should return a boolean value."
