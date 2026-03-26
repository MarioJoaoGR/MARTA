
import pytest
from isort._vendored.tomli._parser import Flags

def test_valid_input_happy_path():
    flags = Flags()
    key = ("a", "b", "c")
    
    # Test setting a flag without recursion
    flags.set(key, Flags.EXPLICIT_NEST, recursive=False)
    assert flags._flags["a"]["nested"]["b"]["nested"]["c"]["recursive_flags"] == {Flags.EXPLICIT_NEST}

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_2_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        flags = Flags()
        key = ("a", "b", "c")
    
        # Test setting a flag without recursion
        flags.set(key, Flags.EXPLICIT_NEST, recursive=False)
>       assert flags._flags["a"]["nested"]["b"]["nested"]["c"]["recursive_flags"] == {Flags.EXPLICIT_NEST}
E       assert set() == {1}
E         
E         Extra items in the right set:
E         1
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_2_test_valid_input_happy_path.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_Flags_set_2_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.11s ===============================
"""