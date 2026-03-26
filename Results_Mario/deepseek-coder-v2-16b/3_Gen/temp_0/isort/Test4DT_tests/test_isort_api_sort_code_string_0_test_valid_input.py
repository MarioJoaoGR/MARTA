
import pytest
from io import StringIO
from isort.api import sort_code_string, DEFAULT_CONFIG
from pathlib import Path
from typing import Any, TextIO

@pytest.mark.parametrize("code", [
    "import os\nimport sys",  # Simple case with two imports
    "import sys\nimport os",  # Reversed order of imports
    "import os\nimport math\nimport sys",  # Three imports in random order
    "import os\nimport os\nimport sys"  # Duplicate imports
])
def test_valid_input(code):
    result = sort_code_string(code)
    assert isinstance(result, str), "The function should return a string."
    assert "import os" in result and "import sys" in result, "Imports are not correctly sorted."
