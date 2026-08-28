
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
__________________________ test_esc_underscore_basic ___________________________

    def test_esc_underscore_basic():
>       assert esc_underscore("hello_world") == "hello\_world"
E       AssertionError: assert 'hello_world' == 'hello\\_world'
E         
E         - hello\_world
E         ?      -
E         + hello_world

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6: AssertionError
______________________ test_esc_underscore_no_underscores ______________________

    def test_esc_underscore_no_underscores():
>       assert esc_underscore("no_underscores_here") == "no_underscores_here"
E       AssertionError: assert 'no\\_underscores\\_here' == 'no_underscores_here'
E         
E         - no_underscores_here
E         + no\_underscores\_here
E         ?   +            +

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:9: AssertionError
____________________ test_esc_underscore_special_characters ____________________

    def test_esc_underscore_special_characters():
>       assert esc_underscore("hello!world") == "hello\!world"
E       AssertionError: assert 'hello!world' == 'hello\\!world'
E         
E         - hello\!world
E         ?      -
E         + hello!world

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:12: AssertionError
_______________________ test_esc_underscore_large_string _______________________

    def test_esc_underscore_large_string():
        expected = "a" * 100 + r"\_\_" + "b" * 50
        result = esc_underscore("a" * 100 + "_b" * 50)
>       assert result == expected
E       AssertionError: assert 'aaaaaaaaaaaa...b\\_b\\_b\\_b' == 'aaaaaaaaaaaa...bbbbbbbbbbbbb'
E         
E         Skipping 92 identical leading characters in diff, use -v to show
E         - aaaaaaaa\_\_bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
E         + aaaaaaaa\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b\_b

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:17: AssertionError
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6
  /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:6: DeprecationWarning: invalid escape sequence '\_'
    assert esc_underscore("hello_world") == "hello\_world"

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:12
  /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py:12: DeprecationWarning: invalid escape sequence '\!'
    assert esc_underscore("hello!world") == "hello\!world"

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_no_underscores
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_special_characters
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser_esc_underscore_0.py::test_esc_underscore_large_string
======================== 4 failed, 2 warnings in 0.06s =========================
"""