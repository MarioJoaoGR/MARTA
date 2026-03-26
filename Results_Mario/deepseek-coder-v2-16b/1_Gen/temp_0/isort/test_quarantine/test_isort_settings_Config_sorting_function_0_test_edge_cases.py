
import pytest
from isort.settings import SortingFunctionDoesNotExist

def test_sorting_function():
    config = Config()
    
    # Test default sorting function
    assert config.sorting_function() == sorted
    
    # Test natural sort order
    config.sort_order = "natural"
    assert config.sorting_function() == sorting.naturally
    
    # Test invalid sort order
    with pytest.raises(SortingFunctionDoesNotExist):
        config.sort_order = "invalid_sort_order"
        config.sorting_function()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_sorting_function_0_test_edge_cases
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:6:13: E0602: Undefined variable 'Config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:13:40: E0602: Undefined variable 'sorting' (undefined-variable)


"""