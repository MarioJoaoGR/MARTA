
import pytest
from ansible.playbook.base import _generic_g_parent

class MyClass:
    def __init__(self):
        self._squashed = False
        self._finalized = False
        self._attributes = {'name': 'Example Name', 'age': 30}
        self._attr_defaults = {'name': 'Default Name', 'age': 25}

    def _get_parent_attribute(self, prop_name):
        return getattr(super(), prop_name)

class TestGenericGParent:
    
    @pytest.fixture(autouse=True)
    def setup_env_vars(self):
        pass  # No environment variables to set for this test

    def test_valid_case_1(self):
        my_instance = MyClass()
        prop_value = _generic_g_parent('name', my_instance)
        assert prop_value == 'Example Name'

    def test_valid_case_2(self):
        my_instance = MyClass()
        prop_value = _generic_g_parent('age', my_instance)
        assert prop_value == 30

    def test_invalid_property(self):
        my_instance = MyClass()
        with pytest.raises(AttributeError):
            _generic_g_parent('non_existent_property', my_instance)
