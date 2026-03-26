
# Module: isort.place
import pytest
from module_with_reason import module_with_reason, DEFAULT_CONFIG
from config import Config
from pathlib import Path

# Test cases for module_with_reason function
def test_module_with_reason_custom_config():
    # Create a custom configuration with forced separate patterns and source paths
    config = Config(forced_separate=['*.log', 'data.*'], src_paths=[Path('/path/to/src')])
    
    # Call the function with a specific module name that should match the forced separate pattern
    result = module_with_reason('data.txt', config)
    assert result == ('sections.FIRSTPARTY', 'Found in one of the configured src_paths: /path/to/src')

def test_module_with_reason_default_config():
    # Call the function without providing a configuration, using default config
    result = module_with_reason('unknown_module')
    assert result == ('Default option in Config or universal default.', 'Default option in Config or universal default.')

def test_module_with_reason_no_match():
    # Create a custom configuration without any specific patterns or paths
    config = Config()
    
    # Call the function with a module name that does not match any pattern
    result = module_with_reason('unknown_module', config)
    assert result == ('Default option in Config or universal default.', 'Default option in Config or universal default.')

def test_module_with_reason_forced_separate():
    # Create a custom configuration with forced separate patterns
    config = Config(forced_separate=['*.log', 'data.*'])
    
    # Call the function with a module name that should match one of the forced separate patterns
    result = module_with_reason('data.txt', config)
    assert result == ('sections.FIRSTPARTY', 'Found in one of the configured src_paths: /path/to/src')

def test_module_with_reason_local():
    # Create a custom configuration with local patterns
    config = Config(local=['*.log', 'data.*'])
    
    # Call the function with a module name that should match one of the local patterns
    result = module_with_reason('data.txt', config)
    assert result == ('sections.FIRSTPARTY', 'Found in one of the configured src_paths: /path/to/src')

def test_module_with_reason_known_pattern():
    # Create a custom configuration with known patterns
    config = Config(known_patterns=['*.log', 'data.*'])
    
    # Call the function with a module name that should match one of the known patterns
    result = module_with_reason('data.txt', config)
    assert result == ('sections.FIRSTPARTY', 'Found in one of the configured src_paths: /path/to/src')

def test_module_with_reason_src_path():
    # Create a custom configuration with source paths
    config = Config(src_paths=[Path('/path/to/src')])
    
    # Call the function with a module name that should be found in one of the configured source paths
    result = module_with_reason('data.txt', config)
    assert result == ('sections.FIRSTPARTY', 'Found in one of the configured src_paths: /path/to/src')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place_module_with_reason_0
isort/Test4DT_tests/test_isort_place_module_with_reason_0.py:4:0: E0401: Unable to import 'module_with_reason' (import-error)
isort/Test4DT_tests/test_isort_place_module_with_reason_0.py:5:0: E0401: Unable to import 'config' (import-error)


"""