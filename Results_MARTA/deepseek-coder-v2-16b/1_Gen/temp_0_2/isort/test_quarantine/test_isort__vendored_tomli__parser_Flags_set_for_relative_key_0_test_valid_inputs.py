
import pytest
from isort._vendored.tomli._parser import Flags

def test_valid_inputs():
    flags = Flags()
    
    # Test setting a flag for a relative key without recursion
    flags.set_for_relative_key(["a", "b"], ["c"], Flags.EXPLICIT_NEST)
    assert flags._flags == {
        'a': {
            'nested': {
                'b': {
                    'nested': {
                        'c': {'flags': {Flags.EXPLICIT_NEST}, 'recursive_flags': set(), 'nested': {}}
                    }
                }
            }
        }
    }

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        flags = Flags()
    
        # Test setting a flag for a relative key without recursion
        flags.set_for_relative_key(["a", "b"], ["c"], Flags.EXPLICIT_NEST)
>       assert flags._flags == {
            'a': {
                'nested': {
                    'b': {
                        'nested': {
                            'c': {'flags': {Flags.EXPLICIT_NEST}, 'recursive_flags': set(), 'nested': {}}
                        }
                    }
                }
            }
        }
E       AssertionError: assert {'a': {'flags...lags': set()}} == {'a': {'neste...': set()}}}}}}
E         
E         Differing items:
E         {'a': {'flags': set(), 'nested': {'b': {'flags': set(), 'nested': {'c': {'flags': {...}, 'nested': {}, 'recursive_flags': set()}}, 'recursive_flags': set()}}, 'recursive_flags': set()}} != {'a': {'nested': {'b': {'nested': {'c': {'flags': {...}, 'nested': {}, 'recursive_flags': set()}}}}}}
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_0_test_valid_inputs.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_for_relative_key_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""