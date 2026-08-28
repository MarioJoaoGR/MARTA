
import pytest
from cookiecutter.prompt import read_user_yes_no
import click



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
>       assert read_user_yes_no('Do you like Python?', default_value='n') == True

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/prompt.py:32: in read_user_yes_no
    return click.prompt(question, default=default_value, type=click.BOOL)
/data/pydeps/marta/click/termui.py:171: in prompt
    value = prompt_func(prompt)
/data/pydeps/marta/click/termui.py:147: in prompt_func
    return f(text[-1:])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4cc779da50>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/marta/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
Do you like Python? [n]: 
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        with pytest.raises(TypeError):
            read_user_yes_no('Do you like Python?')
>       assert read_user_yes_no('Do you like Python?', default_value='n') == False

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/prompt.py:32: in read_user_yes_no
    return click.prompt(question, default=default_value, type=click.BOOL)
/data/pydeps/marta/click/termui.py:171: in prompt
    value = prompt_func(prompt)
/data/pydeps/marta/click/termui.py:147: in prompt_func
    return f(text[-1:])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <_pytest.capture.DontReadFromInput object at 0x7f4cc779da50>, size = -1

    def read(self, size: int = -1) -> str:
>       raise OSError(
            "pytest: reading from stdin while output is captured!  Consider using `-s`."
        )
E       OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/marta/_pytest/capture.py:208: OSError
----------------------------- Captured stdout call -----------------------------
Do you like Python? [n]: 
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(ValueError):
>           read_user_yes_no('Do you like Python?')
E           TypeError: read_user_yes_no() missing 1 required positional argument: 'default_value'

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py:16: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_prompt_read_user_yes_no_0.py::test_invalid_inputs
============================== 3 failed in 0.13s ===============================
"""