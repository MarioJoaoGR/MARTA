
import pytest
from thonny.roughparse import _build_char_in_string_func, _is_char_in_string



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        build_func = _build_char_in_string_func(0)
>       check_character = build_func(10)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

offset = 10, _startindex = 0
_icis = <function _is_char_in_string at 0x7fa1d92f4040>

    def inner(offset, _startindex=startindex, _icis=_is_char_in_string):
>       return _icis(_startindex + "+%dc" % offset)
E       TypeError: unsupported operand type(s) for +: 'int' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:963: TypeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        build_func = _build_char_in_string_func(0)
>       check_character = build_func(10)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

offset = 10, _startindex = 0
_icis = <function _is_char_in_string at 0x7fa1d92f4040>

    def inner(offset, _startindex=startindex, _icis=_is_char_in_string):
>       return _icis(_startindex + "+%dc" % offset)
E       TypeError: unsupported operand type(s) for +: 'int' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:963: TypeError
_____________________________ test_negative_offset _____________________________

    def test_negative_offset():
        build_func = _build_char_in_string_func(5)
>       check_character = build_func(-2)

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

offset = -2, _startindex = 5
_icis = <function _is_char_in_string at 0x7fa1d92f4040>

    def inner(offset, _startindex=startindex, _icis=_is_char_in_string):
>       return _icis(_startindex + "+%dc" % offset)
E       TypeError: unsupported operand type(s) for +: 'int' and 'str'

/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/roughparse.py:963: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py::test_invalid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_roughparse__build_char_in_string_func_0.py::test_negative_offset
============================== 3 failed in 0.08s ===============================
"""