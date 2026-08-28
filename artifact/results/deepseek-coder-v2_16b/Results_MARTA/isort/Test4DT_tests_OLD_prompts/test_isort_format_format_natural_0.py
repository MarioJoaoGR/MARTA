
import pytest
from unittest.mock import patch
from isort.format import format_natural



@patch('isort.format.format_natural')
def test_format_natural_mocked(mock_format_natural):
    mock_format_natural.return_value = 'import math'
    assert format_natural("math") == 'import math'

@patch('isort.format.format_natural')
def test_format_natural_with_from_import(mock_format_natural):
    mock_format_natural.return_value = 'from math import sin'
    assert format_natural("from math import sin") == 'from math import sin'

@patch('isort.format.format_natural')
def test_format_natural_with_alias(mock_format_natural):
    mock_format_natural.return_value = 'import numpy as np'
    assert format_natural("numpy as np") == 'import numpy as np'

@patch('isort.format.format_natural')
def test_format_natural_with_complex_import(mock_format_natural):
    mock_format_natural.return_value = 'from os.path import join'
    assert format_natural("os.path.join") == 'from os.path import join'