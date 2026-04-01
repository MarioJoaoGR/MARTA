
import pytest
from io import StringIO
from pathlib import Path
from typing import Any, Iterator
from isort.api import Config, DEFAULT_CONFIG, ImportKey, find_imports_in_code
from isort.identify import Import

@pytest.mark.parametrize("code", [
    "import os\nimport sys\nprint('Hello, World!')",
    "from math import pi\nimport sys"
])
def test_valid_input(code):
    imports = list(find_imports_in_code(code))
    assert len(imports) == 2  # Assuming each import statement is unique and not aliased
    for imp in imports:
        assert isinstance(imp, Import)
