
import pytest
from httpie.cli.argtypes import KeyValueArgType

def test_invalid_input_none_separators():
    with pytest.raises(TypeError):
        KeyValueArgType()

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType___init___1_test_invalid_input_none_separators.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_input_none_separators ______________________

    def test_invalid_input_none_separators():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType___init___1_test_invalid_input_none_separators.py:6: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType___init___1_test_invalid_input_none_separators.py::test_invalid_input_none_separators
============================== 1 failed in 0.18s ===============================
"""