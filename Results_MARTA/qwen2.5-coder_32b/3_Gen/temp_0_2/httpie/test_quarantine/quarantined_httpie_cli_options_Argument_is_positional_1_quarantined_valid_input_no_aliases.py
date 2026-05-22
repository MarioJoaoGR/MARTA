
import pytest
from httpie.cli.options import Argument

def test_valid_input_no_aliases():
    arg = Argument(aliases=[], configuration={})
    assert arg.is_positional() is True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_options_Argument_is_positional_1_test_valid_input_no_aliases.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_no_aliases __________________________

    def test_valid_input_no_aliases():
        arg = Argument(aliases=[], configuration={})
>       assert arg.is_positional() is True
E       TypeError: 'bool' object is not callable

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_options_Argument_is_positional_1_test_valid_input_no_aliases.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_options_Argument_is_positional_1_test_valid_input_no_aliases.py::test_valid_input_no_aliases
============================== 1 failed in 0.21s ===============================
"""