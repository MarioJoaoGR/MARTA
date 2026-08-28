
import os
import sys
from ansible.utils.py3compat import _TextEnviron

def test__TextEnviron_getitem_existing_env():
    # Set up a mock environment variable
    os.environ['TEST_VAR'] = 'test_value'
    text_env = _TextEnviron()
    
    # Test retrieving an existing environment variable
    assert text_env['TEST_VAR'] == 'test_value', "Expected the value of TEST_VAR to be 'test_value'"

def test__TextEnviron_getitem_non_existent_env():
    # Ensure os.environ is empty for this test
    original_environ = os.environ.copy()
    os.environ.clear()
    text_env = _TextEnviron()
    
    # Test retrieving a non-existent environment variable, expecting an exception
    try:
        value = text_env['NON_EXISTENT_VAR']
        assert False, "Expected KeyError for non-existent environment variable"
    except KeyError as e:
        assert str(e) == "'NON_EXISTENT_VAR'", "Expected the exception message to be about NON_EXISTENT_VAR"
    finally:
        os.environ.clear()
        os.environ.update(original_environ)

def test__TextEnviron_getitem_undefined_env():
    # Create an _TextEnviron instance with no environment variables set
    text_env = _TextEnviron()
    
    # Test retrieving a non-existent environment variable, expecting it to be undefined
    try:
        value = text_env['NON_EXISTENT_VAR']
        assert False, "Expected KeyError for non-existent environment variable"
    except KeyError as e:
        assert str(e) == "'NON_EXISTENT_VAR'", "Expected the exception message to be about NON_EXISTENT_VAR"

def test__TextEnviron_getitem_cache():
    # Set up a mock environment variable
    os.environ['CACHE_VAR'] = 'cache_value'
    text_env = _TextEnviron()
    
    # First access should populate the cache
    assert text_env['CACHE_VAR'] == 'cache_value', "Expected the value of CACHE_VAR to be 'cache_value'"
    
    # Second access should return from the cache
    assert text_env['CACHE_VAR'] == 'cache_value', "Expected the cached value for CACHE_VAR to be 'cache_value'"

def test__TextEnviron_getitem_passthru():
    # Set up a mock environment variable with non-standard encoding
    os.environ['PASSTHRU_VAR'] = '\x80'  # Invalid byte sequence for utf-8, should pass through
    text_env = _TextEnviron()
    
    # Test retrieving an environment variable with invalid bytes, expecting it to passthru
    assert text_env['PASSTHRU_VAR'] == '\x80', "Expected the value of PASSTHRU_VAR to be '\\x80'"
