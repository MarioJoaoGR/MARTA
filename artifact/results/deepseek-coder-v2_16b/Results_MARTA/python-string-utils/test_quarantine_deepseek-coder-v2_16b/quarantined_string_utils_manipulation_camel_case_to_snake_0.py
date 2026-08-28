
import pytest
from string_utils.manipulation import camel_case_to_snake
from string_utils.exceptions import InvalidInputError

def is_string(obj):
    return isinstance(obj, str)

def is_camel_case(input_string):
    return re.match(r'^[a-z]+([A-Z][a-z]*)*$', input_string) is not None

# Test for camel_case_to_snake function with default separator
def test_camel_case_to_snake_default():
    assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_string_test'

# Test for camel_case_to_snake function with custom separator
def test_camel_case_to_snake_custom_separator():
    assert camel_case_to_snake('ThisIsACamelStringTest', separator='-') == 'this-is-a-camel-string-test'

# Test for invalid input in camel_case_to_snake function
def test_camel_case_to_snake_invalid_input():
    with pytest.raises(InvalidInputError):
        camel_case_to_snake(12345)

# Test for non-camel case input in camel_case_to_snake function
def test_camel_case_to_snake_non_camel_case():
    assert camel_case_to_snake('ThisIsNotACamelCaseString') == 'ThisIsNotACamelCaseString'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_string_utils_manipulation_camel_case_to_snake_0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py:4: in <module>
    from string_utils.exceptions import InvalidInputError
E   ModuleNotFoundError: No module named 'string_utils.exceptions'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""