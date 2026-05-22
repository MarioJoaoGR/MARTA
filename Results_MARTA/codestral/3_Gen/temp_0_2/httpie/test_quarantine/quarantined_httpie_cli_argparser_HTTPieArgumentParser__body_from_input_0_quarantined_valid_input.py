
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import HTTPieArgumentParser

@pytest.fixture
def valid_input():
    return "valid input data"

@pytest.mark.parametrize("data", [valid_input])
def test_valid_input(valid_input):
    with patch('httpie.cli.argparser.HTTPieArgumentParser') as MockParser:
        mock_instance = MockParser.return_value
        mock_instance._body_from_input(data=valid_input)
        
        assert mock_instance.args.data == valid_input.encode()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieArgumentParser__body_from_input_0_test_valid_input.py _
In test_valid_input: function uses no argument 'data'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_cli_argparser_HTTPieArgumentParser__body_from_input_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.21s ===============================
"""