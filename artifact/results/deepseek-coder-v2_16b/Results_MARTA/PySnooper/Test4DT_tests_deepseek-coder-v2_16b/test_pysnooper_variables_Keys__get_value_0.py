
import pytest
from pysnooper import variables

class Keys:
    def _get_value(self, main_value, key):
        return main_value[key]

# Test 1: Basic Usage with Dictionary
def test_basic_usage():
    keys = Keys()
    main_value = {'a': 1, 'b': 2}
    assert keys._get_value(main_value, 'a') == 1
    assert keys._get_value(main_value, 'b') == 2

# Test 2: Handling Non-Existent Key
def test_non_existent_key():
    keys = Keys()
    main_value = {'a': 1, 'b': 2}
    with pytest.raises(KeyError):
        keys._get_value(main_value, 'c')

# Test 3: Using Integer as Key
def test_integer_key():
    keys = Keys()
    main_value = {1: 'one', 2: 'two'}
    assert keys._get_value(main_value, 1) == 'one'
    assert keys._get_value(main_value, 2) == 'two'

# Test 4: Handling Different Data Types for Key
def test_different_data_types_for_key():
    keys = Keys()
    main_value = {'a': 1, 'b': 2}
    assert keys._get_value(main_value, 'a') == 1
    assert keys._get_value(main_value, 'b') == 2
