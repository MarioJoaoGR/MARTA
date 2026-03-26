
import pytest
from isort.sorting import section_key, Config
import re

@pytest.fixture
def config():
    return Config(lexicographical=True, sort_relative_in_force_sorted_sections=True)

def test_section_key_basic(config):
    assert section_key("from .mod1 import *", config) == 'B3from .mod1 import *'
    assert section_key("import os", config) == 'Bimport os'
    assert section_key("from .mod2 import item", config) == 'Bitem'

def test_section_key_with_config_changes(config):
    config.lexicographical = False
    assert section_key("from .mod1 import *", config) == 'Bfrom .mod1 import *'
    assert section_key("import os", config) == 'Bimport os'
    assert section_key("from .mod2 import item", config) == 'Bitem'

def test_section_key_with_case_sensitivity(config):
    config.case_sensitive = False
    assert section_key("FROM .MOD1 IMPORT *", config) == 'B3from .mod1 import *'
    assert section_key("Import os", config) == 'Bimport os'
    assert section_key("From .mod2 Import item", config) == 'Bitem'

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

isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_section_key_basic ___________________

    @pytest.fixture
    def config():
>       return Config(lexicographical=True, sort_relative_in_force_sorted_sections=True)

isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = typing.Any, args = ()
kwargs = {'lexicographical': True, 'sort_relative_in_force_sorted_sections': True}

    def __new__(cls, *args, **kwargs):
        if cls is Any:
>           raise TypeError("Any cannot be instantiated")
E           TypeError: Any cannot be instantiated

/usr/local/lib/python3.11/typing.py:538: TypeError
____________ ERROR at setup of test_section_key_with_config_changes ____________

    @pytest.fixture
    def config():
>       return Config(lexicographical=True, sort_relative_in_force_sorted_sections=True)

isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = typing.Any, args = ()
kwargs = {'lexicographical': True, 'sort_relative_in_force_sorted_sections': True}

    def __new__(cls, *args, **kwargs):
        if cls is Any:
>           raise TypeError("Any cannot be instantiated")
E           TypeError: Any cannot be instantiated

/usr/local/lib/python3.11/typing.py:538: TypeError
___________ ERROR at setup of test_section_key_with_case_sensitivity ___________

    @pytest.fixture
    def config():
>       return Config(lexicographical=True, sort_relative_in_force_sorted_sections=True)

isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = typing.Any, args = ()
kwargs = {'lexicographical': True, 'sort_relative_in_force_sorted_sections': True}

    def __new__(cls, *args, **kwargs):
        if cls is Any:
>           raise TypeError("Any cannot be instantiated")
E           TypeError: Any cannot be instantiated

/usr/local/lib/python3.11/typing.py:538: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py::test_section_key_basic
ERROR isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py::test_section_key_with_config_changes
ERROR isort/Test4DT_tests/test_isort_sorting_section_key_0_test_edge_case.py::test_section_key_with_case_sensitivity
============================== 3 errors in 0.22s ===============================
"""