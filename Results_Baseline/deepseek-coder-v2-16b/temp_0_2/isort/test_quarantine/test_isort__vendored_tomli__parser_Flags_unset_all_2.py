
import pytest
from isort._vendored.tomli._parser import Flags

def test_unset_all_non_existing_key():
    flags = Flags()
    with pytest.raises(KeyError):
        flags.unset_all(['non', 'existent', 'key'])

def test_unset_all_empty_key():
    flags = Flags()
    with pytest.raises(TypeError):
        flags.unset_all([])  # Should raise TypeError as the function expects a tuple or list of keys

def test_unset_all_existing_key():
    flags = Flags()
    flags._flags['a'] = {'nested': {}}
    flags._flags['a']['nested']['b'] = {}
    flags.unset_all(['a', 'nested'])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_unset_all_non_existing_key ________________________

    def test_unset_all_non_existing_key():
        flags = Flags()
>       with pytest.raises(KeyError):
E       Failed: DID NOT RAISE <class 'KeyError'>

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2.py:7: Failed
___________________________ test_unset_all_empty_key ___________________________

    def test_unset_all_empty_key():
        flags = Flags()
        with pytest.raises(TypeError):
>           flags.unset_all([])  # Should raise TypeError as the function expects a tuple or list of keys

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.Flags object at 0x7f73be2422d0>, key = []

    def unset_all(self, key: Key) -> None:
        cont = self._flags
        for k in key[:-1]:
            if k not in cont:
                return
            cont = cont[k]["nested"]
>       cont.pop(key[-1], None)
E       IndexError: list index out of range

isort/isort/_vendored/tomli/_parser.py:149: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2.py::test_unset_all_non_existing_key
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_2.py::test_unset_all_empty_key
========================= 2 failed, 1 passed in 0.11s ==========================
"""