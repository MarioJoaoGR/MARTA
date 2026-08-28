
import pytest
from unittest.mock import patch
from thefuck.rules.dirty_unzip import match

@pytest.mark.parametrize("command", [
    {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']},
    {'script_parts': ['unzip', 'example.zip']},
    {'script_parts': ['unzip', '-l', 'example']}
])
def test_match(command):
    with patch('thefuck.rules.dirty_unzip._is_bad_zip', return_value=False):
        assert match(command) == (command['script_parts'][1] != 'example' and '-d' not in command['script_parts'])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_match[command0] _____________________________

command = {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']}

    @pytest.mark.parametrize("command", [
        {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']},
        {'script_parts': ['unzip', 'example.zip']},
        {'script_parts': ['unzip', '-l', 'example']}
    ])
    def test_match(command):
        with patch('thefuck.rules.dirty_unzip._is_bad_zip', return_value=False):
>           assert match(command) == (command['script_parts'][1] != 'example' and '-d' not in command['script_parts'])

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/decorator.py:235: in fun
    return caller(func, *(extras + args), **kw)
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:191: in _for_app
    if is_app(command, *app_names, **kwargs):
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:34: in wrapper
    memo[key] = fn(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']}
app_names = ('unzip',), kwargs = {}, at_least = 0

    @memoize
    def is_app(command, *app_names, **kwargs):
        """Returns `True` if command is call to one of passed app names."""
    
        at_least = kwargs.pop('at_least', 0)
        if kwargs:
            raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))
    
>       if len(command.script_parts) > at_least:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:182: AttributeError
_____________________________ test_match[command1] _____________________________

command = {'script_parts': ['unzip', 'example.zip']}

    @pytest.mark.parametrize("command", [
        {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']},
        {'script_parts': ['unzip', 'example.zip']},
        {'script_parts': ['unzip', '-l', 'example']}
    ])
    def test_match(command):
        with patch('thefuck.rules.dirty_unzip._is_bad_zip', return_value=False):
>           assert match(command) == (command['script_parts'][1] != 'example' and '-d' not in command['script_parts'])

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/decorator.py:235: in fun
    return caller(func, *(extras + args), **kw)
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:191: in _for_app
    if is_app(command, *app_names, **kwargs):
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:34: in wrapper
    memo[key] = fn(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', 'example.zip']}, app_names = ('unzip',)
kwargs = {}, at_least = 0

    @memoize
    def is_app(command, *app_names, **kwargs):
        """Returns `True` if command is call to one of passed app names."""
    
        at_least = kwargs.pop('at_least', 0)
        if kwargs:
            raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))
    
>       if len(command.script_parts) > at_least:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:182: AttributeError
_____________________________ test_match[command2] _____________________________

command = {'script_parts': ['unzip', '-l', 'example']}

    @pytest.mark.parametrize("command", [
        {'script_parts': ['unzip', '-d', '/path/to/extract', 'archive.zip']},
        {'script_parts': ['unzip', 'example.zip']},
        {'script_parts': ['unzip', '-l', 'example']}
    ])
    def test_match(command):
        with patch('thefuck.rules.dirty_unzip._is_bad_zip', return_value=False):
>           assert match(command) == (command['script_parts'][1] != 'example' and '-d' not in command['script_parts'])

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/decorator.py:235: in fun
    return caller(func, *(extras + args), **kw)
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:191: in _for_app
    if is_app(command, *app_names, **kwargs):
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:34: in wrapper
    memo[key] = fn(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = {'script_parts': ['unzip', '-l', 'example']}, app_names = ('unzip',)
kwargs = {}, at_least = 0

    @memoize
    def is_app(command, *app_names, **kwargs):
        """Returns `True` if command is call to one of passed app names."""
    
        at_least = kwargs.pop('at_least', 0)
        if kwargs:
            raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))
    
>       if len(command.script_parts) > at_least:
E       AttributeError: 'dict' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:182: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py::test_match[command0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py::test_match[command1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_0.py::test_match[command2]
========================= 3 failed, 1 warning in 0.19s =========================
"""