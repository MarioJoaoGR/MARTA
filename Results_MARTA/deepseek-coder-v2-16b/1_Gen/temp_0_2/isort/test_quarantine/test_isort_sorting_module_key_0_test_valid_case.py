
import pytest
from isort.sorting import Config
from isort.sorting import module_key

@pytest.fixture
def config():
    return Config()

def test_valid_case(config):
    assert module_key("my_module", config) == "B my_module"
    assert module_key("MyModule", config, sub_imports=True, ignore_case=False) == "A MYMODULE"
    assert module_key(".mymodule.submodule", config, straight_import=True) == "B mymodule_submodule"

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

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_valid_case.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_case _______________________

    @pytest.fixture
    def config():
>       return Config()

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_valid_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = typing.Any, args = (), kwargs = {}

    def __new__(cls, *args, **kwargs):
        if cls is Any:
>           raise TypeError("Any cannot be instantiated")
E           TypeError: Any cannot be instantiated

/usr/local/lib/python3.11/typing.py:538: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_sorting_module_key_0_test_valid_case.py::test_valid_case
=============================== 1 error in 0.12s ===============================
"""