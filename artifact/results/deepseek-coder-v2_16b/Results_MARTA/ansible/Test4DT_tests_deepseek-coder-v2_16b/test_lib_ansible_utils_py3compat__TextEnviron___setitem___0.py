
import os
import sys
from unittest import mock
import pytest
from ansible.utils.py3compat import to_bytes

class _TextEnviron:
    """
    Utility class to return text strings from the environment instead of byte strings.
    
    Mimics the behaviour of os.environ on Python3.

    Parameters:
        env (dict): A dictionary representing the environment variables. If None, defaults to os.environ.
        encoding (str): The encoding to use for decoding byte strings from the environment. If None, it uses sys.getfilesystemencoding().

    Attributes:
        encoding (str): The encoding used for decoding values from the environment.
        _raw_environ (dict): A dictionary containing the raw environment variables.
        _value_cache (dict): A cache to store decoded environment variable values for efficiency.

    Examples:
        # Create an instance using default environment and system encoding
        text_env = _TextEnviron()
        
        # Create an instance with a specified dictionary of environment variables
        custom_env = _TextEnviron(env={'VAR1': 'value1', 'VAR2': 'value2'})
        
        # Create an instance with a specified encoding
        utf8_env = _TextEnviron(encoding='utf-8')
    
    """
    def __init__(self, env=None, encoding=None):
        if env is None:
            env = os.environ
        self._raw_environ = env
        self._value_cache = {}
        # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
        # instead of utf-8
        if encoding is None:
            # Since we're trying to mimic Python3's os.environ, use sys.getfilesystemencoding()
            # instead of utf-8
            self.encoding = sys.getfilesystemencoding()
        else:
            self.encoding = encoding

    def __setitem__(self, key, value):
        """
        Set an environment variable in the raw environment dictionary using a given key and value.

        Parameters:
            key (str): The key to set in the environment dictionary.
            value (str): The value to associate with the key in the environment dictionary.

        Returns:
            None
        """
        self._raw_environ[key] = to_bytes(value, encoding=self.encoding, nonstring='strict', errors='surrogate_or_strict')

# Test cases for _TextEnviron class

def test_valid_inputs():
    # Create a mock environment dictionary with valid key-value pairs
    env = {'VALID_KEY': 'valid_value'}
    text_env = _TextEnviron(env=env)
    
    # Test if the environment variable is set correctly
    assert text_env['VALID_KEY'] == b'valid_value'

def test_edge_cases():
    # Create an instance with None as input
    text_env = _TextEnviron()
    
    # Test setting a non-string value should raise TypeError
    with pytest.raises(TypeError):
        text_env['NON_STRING'] = 123

def test_invalid_inputs():
    # Create an instance with minimal args
    text_env = _TextEnviron()
    
    # Test setting a None value should raise TypeError
    with pytest.raises(TypeError):
        text_env['NONE_KEY'] = None
