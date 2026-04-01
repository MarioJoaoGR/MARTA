
import pytest
from sty.primitive import Register

def test_edge_cases():
    register = Register()
    register_dict = register.as_dict()
    
    # Check that the output is a dictionary
    assert isinstance(register_dict, dict)
    
    # Check that the dictionary keys and values are correct
    expected_keys = {'is_muted', 'eightbit_call', 'rgb_call'}
    actual_keys = set(register_dict.keys())
    assert expected_keys == actual_keys

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        register = Register()
        register_dict = register.as_dict()
    
        # Check that the output is a dictionary
        assert isinstance(register_dict, dict)
    
        # Check that the dictionary keys and values are correct
        expected_keys = {'is_muted', 'eightbit_call', 'rgb_call'}
        actual_keys = set(register_dict.keys())
>       assert expected_keys == actual_keys
E       AssertionError: assert {'eightbit_ca...', 'rgb_call'} == set()
E         
E         Extra items in the left set:
E         'is_muted'
E         'eightbit_call'
E         'rgb_call'
E         Use -v to get more diff

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_cases.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED sty/Test4DT_tests/test_sty_primitive_Register_as_dict_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.02s ===============================
"""