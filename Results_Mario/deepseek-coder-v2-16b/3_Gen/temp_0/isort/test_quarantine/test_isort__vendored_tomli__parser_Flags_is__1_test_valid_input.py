
import pytest
from isort._vendored.tomli._parser import Flags

def test_valid_input():
    flags = Flags()
    # Add a valid key and set the flag
    flags._flags = {
        "namespace": {
            "subnamespace": {
                "nested": {},
                "flags": {Flags.EXPLICIT_NEST: True}
            }
        }
    }
    
    # Test if the flag is set for a valid key
    assert flags.is_(["namespace", "subnamespace"], Flags.EXPLICIT_NEST) == True

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        flags = Flags()
        # Add a valid key and set the flag
        flags._flags = {
            "namespace": {
                "subnamespace": {
                    "nested": {},
                    "flags": {Flags.EXPLICIT_NEST: True}
                }
            }
        }
    
        # Test if the flag is set for a valid key
>       assert flags.is_(["namespace", "subnamespace"], Flags.EXPLICIT_NEST) == True

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.Flags object at 0x7f3f98990c50>
key = ['namespace', 'subnamespace'], flag = 1

    def is_(self, key: Key, flag: int) -> bool:
        if not key:
            return False  # document root has no flags
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return False
            inner_cont = cont[k]
>           if flag in inner_cont["recursive_flags"]:
E           KeyError: 'recursive_flags'

isort/isort/_vendored/tomli/_parser.py:183: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_is__1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.15s ===============================
"""