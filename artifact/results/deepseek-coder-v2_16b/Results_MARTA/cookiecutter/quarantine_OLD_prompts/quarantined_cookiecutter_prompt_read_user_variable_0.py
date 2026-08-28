
import pytest
from unittest.mock import patch
from cookiecutter.prompt import read_user_variable


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_variable_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('builtins.input', return_value='valid_input'):
>           result = read_user_variable("test_var", "default_value")

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_variable_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/prompt.py:19: in read_user_variable
    return click.prompt(var_name, default=default_value)
/data/pydeps/marta/click/termui.py:171: in prompt
    value = prompt_func(prompt)
/data/pydeps/marta/click/termui.py:147: in prompt_func
    return f(text[-1:])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f5a8b40d9f0>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/marta/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
test_var [default_value]: 
_____________________________ test_missing_default _____________________________

    def test_missing_default():
        with patch('builtins.input', side_effect=['', '']):
>           result = read_user_variable("test_var", None)

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_variable_0.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/prompt.py:19: in read_user_variable
    return click.prompt(var_name, default=default_value)
/data/pydeps/marta/click/termui.py:171: in prompt
    value = prompt_func(prompt)
/data/pydeps/marta/click/termui.py:147: in prompt_func
    return f(text[-1:])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f5a8b40d9f0>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/marta/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
test_var: 
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_variable_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_variable_0.py::test_missing_default
============================== 2 failed in 0.13s ===============================
"""