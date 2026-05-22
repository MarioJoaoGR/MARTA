
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import KeyValueArgType

def test_valid_input_default_separators():
    with patch('httpie.cli.argtypes.KeyValueArgType', autospec=True) as mock_KeyValueArgType:
        key_value_arg_type = KeyValueArgType()
        assert key_value_arg_type is not None
        assert key_value_arg_type.separators == ('=', ':')

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

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_KeyValueArgType___init___0_test_valid_input_default_separators.py F [100%]

=================================== FAILURES ===================================
_____________________ test_valid_input_default_separators ______________________

    def test_valid_input_default_separators():
        with patch('httpie.cli.argtypes.KeyValueArgType', autospec=True) as mock_KeyValueArgType:
            key_value_arg_type = KeyValueArgType()
            assert key_value_arg_type is not None
>           assert key_value_arg_type.separators == ('=', ':')
E           AssertionError: assert () == ('=', ':')
E             
E             Right contains 2 more items, first extra item: '='
E             Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_KeyValueArgType___init___0_test_valid_input_default_separators.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_argtypes_KeyValueArgType___init___0_test_valid_input_default_separators.py::test_valid_input_default_separators
============================== 1 failed in 0.15s ===============================
"""