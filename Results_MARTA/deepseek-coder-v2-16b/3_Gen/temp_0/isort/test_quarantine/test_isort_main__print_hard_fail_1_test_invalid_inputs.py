
import pytest
from isort.main import _print_hard_fail, Config

def test_invalid_inputs():
    config = "InvalidType"  # Invalid type for config
    offending_file = 123  # Non-string value for file
    message = {'key': 'value'}  # Non-string value for message
    
    with pytest.raises(TypeError):
        _print_hard_fail(config, offending_file, message)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        config = "InvalidType"  # Invalid type for config
        offending_file = 123  # Non-string value for file
        message = {'key': 'value'}  # Non-string value for message
    
        with pytest.raises(TypeError):
>           _print_hard_fail(config, offending_file, message)

isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_invalid_inputs.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

config = 'InvalidType', offending_file = 123, message = {'key': 'value'}

    def _print_hard_fail(
        config: Config, offending_file: str | None = None, message: str | None = None
    ) -> None:
        """Fail on unrecoverable exception with custom message."""
        message = message or (
            f"Unrecoverable exception thrown when parsing {offending_file or ''}! "
            "This should NEVER happen.\n"
            "If encountered, please open an issue: https://github.com/PyCQA/isort/issues/new"
        )
        printer = create_terminal_printer(
>           color=config.color_output, error=config.format_error, success=config.format_success
        )
E       AttributeError: 'str' object has no attribute 'color_output'

isort/isort/main.py:130: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__print_hard_fail_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.17s ===============================
"""