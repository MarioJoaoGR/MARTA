
from io import StringIO
from unittest.mock import patch

import pytest

from isort.parse import DEFAULT_CONFIG, Config, ParsedContent, file_contents


# Test 1: Parsing a Python file with default configurations
def test_file_contents_default_config():
    contents = "import os\nfrom math import sqrt"
    parsed = file_contents(contents)
    assert isinstance(parsed, ParsedContent)