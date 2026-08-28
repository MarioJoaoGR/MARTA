
import pytest
from thefuck.rules.dirty_unzip import match
from thefuck.types import Command



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_with_d_flag _________________________

    def test_valid_input_with_d_flag():
>       command = Command(script_parts=['unzip', '-d', '/path/to/extract', 'archive.zip'])
E       TypeError: Command.__init__() got an unexpected keyword argument 'script_parts'

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py:7: TypeError
______________________ test_invalid_input_without_d_flag _______________________

    def test_invalid_input_without_d_flag():
>       command = Command(script_parts=['unzip', 'example.zip'])
E       TypeError: Command.__init__() got an unexpected keyword argument 'script_parts'

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py:11: TypeError
__________________________ test_error_case_none_input __________________________

    def test_error_case_none_input():
        command = None
        with pytest.raises(TypeError):
>           match(command)

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/data/pydeps/marta/decorator.py:235: in fun
    return caller(func, *(extras + args), **kw)
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:191: in _for_app
    if is_app(command, *app_names, **kwargs):
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:34: in wrapper
    memo[key] = fn(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

command = None, app_names = ('unzip',), kwargs = {}, at_least = 0

    @memoize
    def is_app(command, *app_names, **kwargs):
        """Returns `True` if command is call to one of passed app names."""
    
        at_least = kwargs.pop('at_least', 0)
        if kwargs:
            raise TypeError("got an unexpected keyword argument '{}'".format(kwargs.keys()))
    
>       if len(command.script_parts) > at_least:
E       AttributeError: 'NoneType' object has no attribute 'script_parts'

/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/utils.py:182: AttributeError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py::test_valid_input_with_d_flag
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py::test_invalid_input_without_d_flag
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_rules_dirty_unzip_match_1.py::test_error_case_none_input
========================= 3 failed, 1 warning in 0.19s =========================
"""