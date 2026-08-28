
import pytest
from unittest.mock import patch, MagicMock
from io import BytesIO
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec
import os
import types
from sanic.utils import load_module_from_file_location, import_string

# Test for valid input (file path)

# Test for valid input (byte object)

# Test for invalid file path
def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        load_module_from_file_location("non_existent_path/to/module.py")

# Test for invalid byte object