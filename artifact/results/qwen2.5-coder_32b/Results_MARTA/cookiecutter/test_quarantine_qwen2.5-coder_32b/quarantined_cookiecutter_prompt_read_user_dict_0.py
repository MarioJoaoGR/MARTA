
import pytest
import click
from unittest.mock import patch

def process_json(value):
    try:
        return eval(value)
    except Exception as e:
        raise ValueError(f"Invalid JSON: {e}")

def read_user_dict(var_name, default_value):
    """Prompt the user to provide a dictionary of data.

    :param str var_name: Variable as specified in the context
    :param default_value: Value that will be returned if no input is provided
    :return: A Python dictionary to use in the context.
    """
    if not isinstance(default_value, dict):
        raise TypeError

    default_display = 'default'

    user_value = click.prompt(
        var_name, default=default_display, type=click.STRING, value_proc=process_json
    )

    if user_value == default_display:
        # Return the given default w/o any processing
        return default_value
    return user_value




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_json_input _____________________________

    def test_valid_json_input():
        with patch('click.prompt', return_value='{"new_key": "new_value"}'):
            result = read_user_dict("Enter your data:", {"key": "value"})
>           assert result == {"new_key": "new_value"}
E           assert '{"new_key": "new_value"}' == {'new_key': 'new_value'}

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py:36: AssertionError
_______________________________ test_empty_input _______________________________

    def test_empty_input():
        with patch('click.prompt', return_value=''):
            result = read_user_dict("Enter your data:", {"key": "value"})
>           assert result == {"key": "value"}
E           AssertionError: assert '' == {'key': 'value'}

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py:41: AssertionError
___________________________ test_invalid_json_input ____________________________

    def test_invalid_json_input():
        with patch('click.prompt', return_value='invalid json'):
>           with pytest.raises(ValueError):
E           Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py:45: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py::test_valid_json_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py::test_empty_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_qwen2.5-coder_32b/test_cookiecutter_prompt_read_user_dict_0.py::test_invalid_json_input
============================== 3 failed in 0.05s ===============================
"""