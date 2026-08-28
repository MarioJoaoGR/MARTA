
import pytest
from apimd.parser import esc_underscore




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_esc_underscore_multiple _________________________

    def test_esc_underscore_multiple():
>       assert esc_underscore("hello_world") == "hello\_world"
E       AssertionError: assert 'hello_world' == 'hello\\_world'
E         
E         - hello\_world
E         ?      -
E         + hello_world

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6: AssertionError
______________________ test_esc_underscore_single_or_none ______________________

    def test_esc_underscore_single_or_none():
        assert esc_underscore("single_name") == "single_name"
        assert esc_underscore("") == ""
>       assert esc_underscore("no_underscores_here") == "no_underscores_here"
E       AssertionError: assert 'no\\_underscores\\_here' == 'no_underscores_here'
E         
E         - no_underscores_here
E         + no\_underscores\_here
E         ?   +            +

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:11: AssertionError
______________________ test_esc_underscore_special_chars _______________________

    def test_esc_underscore_special_chars():
>       assert esc_underscore("hello!world") == "hello\!world"
E       AssertionError: assert 'hello!world' == 'hello\\!world'
E         
E         - hello\!world
E         ?      -
E         + hello!world

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:14: AssertionError
_______________________ test_esc_underscore_large_string _______________________

    def test_esc_underscore_large_string():
>       assert esc_underscore("a" * 100 + "_b" * 50) == "a" * 100 + r"\_\_b" * 50
E       AssertionError: assert 'aaaaaaaaaaaa...b\\_b\\_b\\_b' == 'aaaaaaaaaaaa...\_\\_b\\_\\_b'
E         
E         Skipping 92 identical leading characters in diff, use -v to show
E         - aaaaaaaa\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b\_\_b
E         + aaaaaaaa\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:17: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6
  /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6: DeprecationWarning: invalid escape sequence '\_'
    assert esc_underscore("hello_world") == "hello\_world"

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:14
  /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:14: DeprecationWarning: invalid escape sequence '\!'
    assert esc_underscore("hello!world") == "hello\!world"

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_multiple
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_single_or_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_special_chars
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_large_string
======================== 4 failed, 2 warnings in 0.09s =========================
"""