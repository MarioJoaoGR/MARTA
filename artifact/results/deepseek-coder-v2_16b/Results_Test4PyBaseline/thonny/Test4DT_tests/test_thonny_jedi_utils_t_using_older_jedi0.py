# Module: thonny.jedi_utils
import pytest
import jedi
from thonny.jedi_utils import _using_older_jedi

# Test cases for _using_older_jedi function
def test_using_older_jedi_true():
    # Mock the jedi module to have a version in the older range
    jedi_mock = type('MockJedi', (object,), {'__version__': '0.13'})()
    assert _using_older_jedi(jedi_mock) is True

def test_using_older_jedi_false():
    # Mock the jedi module to have a version not in the older range
    jedi_mock = type('MockJedi', (object,), {'__version__': '0.18'})()
    assert _using_older_jedi(jedi_mock) is False

def test_using_older_jedi_edge():
    # Edge case: Mock the jedi module to have an exact match version in the older range
    jedi_mock = type('MockJedi', (object,), {'__version__': '0.17'})()
    assert _using_older_jedi(jedi_mock) is True

def test_using_older_jedi_invalid():
    # Edge case: Mock the jedi module to have an invalid version format
    jedi_mock = type('MockJedi', (object,), {'__version__': '1.0'})()
    assert _using_older_jedi(jedi_mock) is False
