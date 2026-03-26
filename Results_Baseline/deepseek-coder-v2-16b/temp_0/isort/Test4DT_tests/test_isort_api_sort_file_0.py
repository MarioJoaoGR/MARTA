
# Module: isort.api
# test_isort.api.py
import io
import shutil
import sys
from pathlib import Path
from unittest.mock import patch

from isort.api import (DEFAULT_CONFIG, Config,  # Corrected the import and typo
                       sort_file)


def test_sort_file_basic():
    with open("test_file.py", "w") as f:
        f.write("import os\nimport sys\nprint('Hello, World!')")
    assert sort_file("test_file.py") is True
    with open("test_file.py", "r") as f:
        content = f.read()
        assert "import os" in content
        assert "import sys" in content
        assert "print('Hello, World!')" in content
    Path("test_file.py").unlink()

def test_sort_file_with_extension():
    with open("config.cfg", "w") as f:
        f.write("import os\nimport sys\nprint('Hello, World!')")
    assert sort_file("config.cfg", extension=".cfg") is True
    with open("config.cfg", "r") as f:
        content = f.read()
        assert "import os" in content
        assert "import sys" in content
        assert "print('Hello, World!')" in content
    Path("config.cfg").unlink()

def test_sort_file_using_default_configuration():
    with open("test_file.py", "w") as f:
        f.write("import os\nimport sys\nprint('Hello, World!')")