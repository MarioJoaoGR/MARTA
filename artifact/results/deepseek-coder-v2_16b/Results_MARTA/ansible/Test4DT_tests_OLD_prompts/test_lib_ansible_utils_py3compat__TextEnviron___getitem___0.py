
import pytest
from ansible.utils.py3compat import PY3, to_text
import os
import sys

class _TextEnviron:
    """
    Utility class to return text strings from the environment instead of byte strings.
    
    Mimics the behaviour of os.environ on Python3.

    Parameters:
        env (dict): A dictionary representing the environment variables. If None, defaults to os.environ.
        encoding (str): The encoding to use when converting byte strings to text strings. If None, it uses sys.getfilesystemencoding().

    Attributes:
        encoding (str): The encoding used for conversion between byte and text strings.

    Methods:
        __getitem__(self, key): Retrieves the value of the specified environment variable as a text string. It caches the decoded values to handle any changes during runtime.

    Examples:
        >>> import os
        >>> from my_module import _TextEnviron
        >>> env = {'KEY': b'value'}
        >>> text_env = _TextEnviron(env=env)
        >>> print(text_env['KEY'])  # Outputs 'value' as a string
        
        >>> os.environ['ANOTHER_KEY'] = b'another_value'
        >>> another_text_env = _TextEnviron()
        >>> print(another_text_env['ANOTHER_KEY'])  # Outputs 'another_value' as a string

    Note:
        This class is designed to work with environment variables that are initially provided as byte strings. It converts these byte strings to text strings using the specified encoding, caching the results for efficiency when the same values are accessed multiple times during runtime.
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

    def __getitem__(self, key):
        value = self._raw_environ[key]
        if PY3:
            return value
        # Cache keys off of the undecoded values to handle any environment variables which change
        # during a run
        if value not in self._value_cache:
            self._value_cache[value] = to_text(value, encoding=self.encoding,
                                               nonstring='passthru', errors='surrogate_or_strict')
        return self._value_cache[value]

def test_invalid_inputs():
    with pytest.raises(KeyError):
        text_env = _TextEnviron()
        text_env['INVALID_KEY']
    
    # Test accessing environment variable using an invalid type (e.g., int)
    with pytest.raises(TypeError):
        text_env = _TextEnviron()
        text_env[123]  # Using an integer instead of a string key
