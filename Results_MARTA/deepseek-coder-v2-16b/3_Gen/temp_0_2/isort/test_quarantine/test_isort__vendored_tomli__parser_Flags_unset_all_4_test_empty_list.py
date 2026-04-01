
from isort._vendored.tomli._parser import Flags
import pytest

def test_empty_list():
    flags = Flags()
    with pytest.raises(KeyError):
        flags.unset_all([])

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_4_test_empty_list.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_empty_list ________________________________

    def test_empty_list():
        flags = Flags()
        with pytest.raises(KeyError):
>           flags.unset_all([])

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_4_test_empty_list.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort._vendored.tomli._parser.Flags object at 0x7f47c716a5d0>, key = []

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
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_unset_all_4_test_empty_list.py::test_empty_list
============================== 1 failed in 0.13s ===============================
"""