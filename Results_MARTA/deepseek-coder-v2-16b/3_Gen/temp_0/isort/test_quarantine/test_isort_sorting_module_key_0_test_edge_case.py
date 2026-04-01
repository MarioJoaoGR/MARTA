
import pytest
from isort.sorting import module_key
from isort.config import Config

@pytest.fixture
def config():
    return Config()

def test_module_key_basic(config):
    assert module_key("math", config) == 'Bmath'

def test_module_key_ignore_case(config):
    assert module_key("MathModule", config, ignore_case=True) == 'Amathmodule'

def test_module_key_sub_imports_and_length_sort(config):
    section_config = {"length_sort": True, "length_sort_sections": ["constants"]}
    assert module_key("CONSTANT_VALUE", config, sub_imports=True, **section_config) == 'A0CONSTANT_VALUE'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_sorting_module_key_0_test_edge_case
isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:4:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:4:0: E0611: No name 'config' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:18:11: E1123: Unexpected keyword argument 'length_sort' in function call (unexpected-keyword-arg)
isort/Test4DT_tests/test_isort_sorting_module_key_0_test_edge_case.py:18:11: E1123: Unexpected keyword argument 'length_sort_sections' in function call (unexpected-keyword-arg)


"""