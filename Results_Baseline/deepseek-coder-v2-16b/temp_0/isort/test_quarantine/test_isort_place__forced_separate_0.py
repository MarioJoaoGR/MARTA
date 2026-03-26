
# Module: Test4DT_tests.test_isort_place__forced_separate_0
import pytest
from isort.settings import Config
from isort._forced_separate import _forced_separate  # Corrected the import statement
from fnmatch import fnmatch

# Test cases for _forced_separate function

def test_basic_usage():
    config = Config()
    config.forced_separate = ["*.log", "backup.*"]
    
    result = _forced_separate("example.log", config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')

def test_no_match():
    another_config = Config()
    another_config.forced_separate = ["*.txt"]
    
    result = _forced_separate("example", another_config)
    assert result is None

def test_different_configuration():
    custom_config = Config()
    custom_config.forced_separate = ["*.py"]
    
    result = _forced_separate("module.py", custom_config)
    assert result == ('*.py', 'Matched forced_separate (*).py config value.')

def test_wildcard_match():
    config = Config()
    config.forced_separate = ["*.log"]
    
    result = _forced_separate("example.log", config)
    assert result == ('*.log', 'Matched forced_separate (*).log config value.')

def test_case_insensitive_match():
    config = Config()
    config.forced_separate = ["*.Log"]
    
    result = _forced_separate("Example.log", config)
    assert result == ('*.Log', 'Matched forced_separate (*).Log config value.')

def test_no_match_with_different_extension():
    config = Config()
    config.forced_separate = ["*.txt"]
    
    result = _forced_separate("example.log", config)
    assert result is None

def test_empty_config():
    config = Config()
    config.forced_separate = []
    
    result = _forced_separate("example.log", config)
    assert result is None

def test_nonexistent_pattern():
    config = Config()
    config.forced_separate = ["*.doesnotexist"]
    
    result = _forced_separate("example.log", config)
    assert result is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_0
isort/Test4DT_tests/test_isort_place__forced_separate_0.py:5:0: E0401: Unable to import 'isort._forced_separate' (import-error)
isort/Test4DT_tests/test_isort_place__forced_separate_0.py:5:0: E0611: No name '_forced_separate' in module 'isort' (no-name-in-module)


"""