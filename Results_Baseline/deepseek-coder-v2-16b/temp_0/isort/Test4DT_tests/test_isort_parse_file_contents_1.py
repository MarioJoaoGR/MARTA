
from io import StringIO
from unittest.mock import patch

import pytest

from isort.parse import DEFAULT_CONFIG, Config, ParsedContent, file_contents


# Test 2: Handling files with no imports and commented-out imports
def test_file_contents_no_imports():
    contents = "This is a sample line without any imports."
    parsed = file_contents(contents)
    assert isinstance(parsed, ParsedContent)
    assert len(parsed.lines_without_imports) == 1

# Test 3: Handling files with only commented-out imports
def test_file_contents_commented_out_imports():
    contents = "# This is a commented out import\n# from math import sqrt"
    parsed = file_contents(contents)
    assert isinstance(parsed, ParsedContent)
    assert len(parsed.lines_without_imports) == 2

# Test 4: Handling files with non-standard line separators
def test_file_contents_non_standard_line_separator():
    contents = "import os\nfrom math import sqrt"
    parsed = file_contents(contents, config=Config(line_ending="\r"))
    assert isinstance(parsed, ParsedContent)