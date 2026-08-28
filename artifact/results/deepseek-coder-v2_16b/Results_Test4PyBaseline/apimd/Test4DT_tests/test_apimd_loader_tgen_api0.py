
import pytest
from apimd.loader import gen_api
from unittest.mock import patch, mock_open
import sys
from os.path import join

# Test cases for the gen_api function

def test_gen_api_default():
    result = gen_api({'Module One': 'module1', 'Module Two': 'module2'})
    assert isinstance(result, list), "Expected a list of strings"