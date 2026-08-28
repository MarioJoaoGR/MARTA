
import pytest
from pysnooper import variables as var_module
from unittest.mock import patch, MagicMock

# Test for CommonVariable._get_value method with dictionary input
def test_commonvariable_get_value_dict():
    class CommonVariable:
        def _get_value(self, main_value, key):
            if isinstance(main_value, dict):
                return main_value.get(key)
            return None

    common_var = CommonVariable()
    result = common_var._get_value({'a': 1, 'b': 2}, 'a')
    assert result == 1, "Expected value for key 'a' in dictionary should be 1"

# Test for CommonVariable._get_value method with list input
def test_commonvariable_get_value_list():
    class CommonVariable:
        def _get_value(self, main_value, key):
            if isinstance(main_value, list):
                return main_value[key]
            return None

    common_var = CommonVariable()
    result = common_var._get_value([10, 20, 30], 1)
    assert result == 20, "Expected value for index 1 in list should be 20"

# Test for CommonVariable._get_value method with key not found in dictionary
def test_commonvariable_get_value_key_not_found():
    class CommonVariable:
        def _get_value(self, main_value, key):
            if isinstance(main_value, dict):
                return main_value.get(key)
            return None

    common_var = CommonVariable()
    result = common_var._get_value({'a': 1, 'b': 2}, 'c')
    assert result is None, "Expected to get None for a key not found in the dictionary"
