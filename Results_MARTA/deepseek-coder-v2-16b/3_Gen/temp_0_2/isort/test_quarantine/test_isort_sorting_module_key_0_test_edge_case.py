
import re
from isort.sorting import module_key
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def mock_config():
    config = MagicMock()
    config.constants = {"mymodule"}
    config.classes = {}
    config.variables = {}
    config.case_sensitive = False
    config.length_sort = True
    config.force_to_top = set()
    config.reverse_relative = False
    return config

def test_module_key_basic(mock_config):
    assert module_key("mymodule", mock_config) == "B mymodule"

def test_module_key_subimports(mock_config):
    assert module_key(".mymodule", mock_config, sub_imports=True) == "C .mymodule"

def test_module_key_ignore_case(mock_config):
    assert module_key("MYMODULE", mock_config, ignore_case=True) == "A mymodule"

def test_module_key_straight_import(mock_config):
    assert module_key("submodule.mymodule", mock_config, straight_import=True) == "B submodule.mymodule"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py FF [ 50%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_module_key_basic _____________________________

mock_config = <MagicMock id='140240244622864'>

    def test_module_key_basic(mock_config):
>       assert module_key("mymodule", mock_config) == "B mymodule"
E       AssertionError: assert 'B8:mymodule' == 'B mymodule'
E         
E         - B mymodule
E         ?  ^
E         + B8:mymodule
E         ?  ^^

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:20: AssertionError
__________________________ test_module_key_subimports __________________________

mock_config = <MagicMock id='140240229737168'>

    def test_module_key_subimports(mock_config):
>       assert module_key(".mymodule", mock_config, sub_imports=True) == "C .mymodule"
E       AssertionError: assert 'BC10:._mymodule' == 'C .mymodule'
E         
E         - C .mymodule
E         ?  ^
E         + BC10:._mymodule
E         ? + ^^^ +

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:23: AssertionError
_________________________ test_module_key_ignore_case __________________________

mock_config = <MagicMock id='140240229077328'>

    def test_module_key_ignore_case(mock_config):
>       assert module_key("MYMODULE", mock_config, ignore_case=True) == "A mymodule"
E       AssertionError: assert 'B8:mymodule' == 'A mymodule'
E         
E         - A mymodule
E         ? ^^
E         + B8:mymodule
E         ? ^^^

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:26: AssertionError
_______________________ test_module_key_straight_import ________________________

mock_config = <MagicMock id='140240229081552'>

    def test_module_key_straight_import(mock_config):
>       assert module_key("submodule.mymodule", mock_config, straight_import=True) == "B submodule.mymodule"
E       AssertionError: assert 'B18:submodule.mymodule' == 'B submodule.mymodule'
E         
E         - B submodule.mymodule
E         ?  ^
E         + B18:submodule.mymodule
E         ?  ^^^

isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:29: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py::test_module_key_basic
FAILED isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py::test_module_key_subimports
FAILED isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py::test_module_key_ignore_case
FAILED isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py::test_module_key_straight_import
============================== 4 failed in 0.14s ===============================
"""