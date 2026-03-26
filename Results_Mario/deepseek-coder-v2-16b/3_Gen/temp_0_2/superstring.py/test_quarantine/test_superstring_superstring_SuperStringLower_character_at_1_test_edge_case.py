
import pytest
from superstring.superstring import SuperStringBase, SuperStringLower

class TestSuperStringLower:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.base_string = "Hello, World!"
        self.base_instance = SuperStringBase(self.base_string)
        self.lower_instance = SuperStringLower(self.base_instance)

    def test_character_at_1_test_edge_case(self):
        assert self.lower_instance.character_at(1) == 'e'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_1_test_edge_case.py E [100%]

==================================== ERRORS ====================================
__ ERROR at setup of TestSuperStringLower.test_character_at_1_test_edge_case ___

self = <Test4DT_tests.test_superstring_superstring_SuperStringLower_character_at_1_test_edge_case.TestSuperStringLower object at 0x7f1212c9e010>

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.base_string = "Hello, World!"
>       self.base_instance = SuperStringBase(self.base_string)
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_1_test_edge_case.py:9: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_1_test_edge_case.py::TestSuperStringLower::test_character_at_1_test_edge_case
=============================== 1 error in 0.05s ===============================
"""