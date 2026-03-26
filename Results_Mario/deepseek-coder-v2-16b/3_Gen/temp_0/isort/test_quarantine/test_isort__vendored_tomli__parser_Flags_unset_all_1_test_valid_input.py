
import pytest
from isort._vendored.tomli._parser import Flags

def test_valid_input():
    flags = Flags()
    flags._flags['a'] = {'nested': {}}
    flags._flags['a']['nested']['b'] = {}
    
    # Test with valid key sequence
    flags.unset_all(['a', 'nested', 'b'])
    assert 'b' not in flags._flags['a']['nested']

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        flags = Flags()
        flags._flags['a'] = {'nested': {}}
        flags._flags['a']['nested']['b'] = {}
    
        # Test with valid key sequence
        flags.unset_all(['a', 'nested', 'b'])
>       assert 'b' not in flags._flags['a']['nested']
E       AssertionError: assert 'b' not in {'b': {}}

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_1_test_valid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.12s ===============================
"""