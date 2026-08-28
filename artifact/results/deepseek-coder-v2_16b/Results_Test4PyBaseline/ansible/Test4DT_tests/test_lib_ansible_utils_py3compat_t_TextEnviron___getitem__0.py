# Module: ansible.utils.py3compat
import os
import sys
from ansible.utils.py3compat import _TextEnviron

def test__TextEnviron_default_settings():
    text_env = _TextEnviron()
    assert isinstance(text_env['PATH'], str), "Expected a string value for 'PATH'"

def test__TextEnviron_custom_environment_dictionary_and_specific_encoding():
    custom_env = {'VAR1': 'value1', 'VAR2': 'value2'}
    text_env = _TextEnviron(env=custom_env, encoding='utf-8')
    assert isinstance(text_env['VAR1'], str), "Expected a string value for 'VAR1'"
    assert text_env.encoding == 'utf-8', "Expected the specified encoding to be 'utf-8'"

def test__TextEnviron_using_os_environ_and_default_encoding():
    text_env = _TextEnviron(env=os.environ)
    assert isinstance(text_env['PATH'], str), "Expected a string value for 'PATH'"
    expected_encoding = sys.getfilesystemencoding()
    assert text_env.encoding == expected_encoding, f"Expected the default encoding to be {expected_encoding}"

def test__TextEnviron_using_sys_getfilesystemencoding_and_specific_encoding():
    text_env = _TextEnviron(encoding=sys.getfilesystemencoding())
    assert isinstance(text_env['LANG'], str), "Expected a string value for 'LANG'"
    expected_encoding = sys.getfilesystemencoding()
    assert text_env.encoding == expected_encoding, f"Expected the specified encoding to be {expected_encoding}"
