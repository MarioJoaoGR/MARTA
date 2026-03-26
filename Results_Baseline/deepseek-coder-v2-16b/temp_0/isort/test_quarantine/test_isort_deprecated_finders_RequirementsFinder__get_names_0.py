
import os
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch

import pytest

from isort.deprecated.finders import RequirementsFinder


# Test initialization of RequirementsFinder
def test_requirements_finder_initialization():
    finder = RequirementsFinder(config=None)  # Adding the missing 'config' parameter
    assert hasattr(finder, 'exts')
    assert hasattr(finder, 'enabled')

# Test _get_names with a mock parse_requirements function
@patch('isort.deprecated.finders.parse_requirements', return_value={'package1': None, 'package2': None})
def test_get_names(_mock_parse_requirements):
    finder = RequirementsFinder(config=None)  # Adding the missing 'config' parameter
    names_iterator = finder._get_names('path/to/somefile')