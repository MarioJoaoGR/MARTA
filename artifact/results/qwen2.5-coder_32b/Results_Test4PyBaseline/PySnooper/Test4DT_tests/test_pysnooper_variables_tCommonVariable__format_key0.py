
# Module: pysnooper.variables
import pytest
from pysnooper.variables import CommonVariable

class TestCommonVariable:

    def test_format_key_not_implemented(self):
        # Create an instance of the base class with a source argument
        common_variable = CommonVariable(source="dummy_source")
        
        # Assert that calling _format_key raises a NotImplementedError
        with pytest.raises(NotImplementedError):
            common_variable._format_key("test_key")

    def test_subclass_format_key(self):
        # Define a subclass that implements _format_key
        class MySubclass(CommonVariable):
            def _format_key(self, key):
                return f"formatted_{key}"
        
        # Create an instance of the subclass with a source argument
        my_instance = MySubclass(source="dummy_source")
        
        # Test with different keys
        assert my_instance._format_key("example") == "formatted_example"
        assert my_instance._format_key("test_key") == "formatted_test_key"
        assert my_instance._format_key("") == "formatted_"

    def test_another_subclass_format_key(self):
        # Define another subclass that implements _format_key differently
        class AnotherSubclass(CommonVariable):
            def _format_key(self, key):
                return f"key_{key}_end"
        
        # Create an instance of the subclass with a source argument
        another_instance = AnotherSubclass(source="dummy_source")
        
        # Test with different keys
        assert another_instance._format_key("sample") == "key_sample_end"
        assert another_instance._format_key("another_key") == "key_another_key_end"
        assert another_instance._format_key("") == "key__end"

    def test_format_key_with_non_string_input(self):
        # Define a subclass that implements _format_key
        class MySubclass(CommonVariable):
            def _format_key(self, key):
                return f"formatted_{key}"
        
        # Create an instance of the subclass with a source argument
        my_instance = MySubclass(source="dummy_source")
        
        # Test with non-string inputs
        assert my_instance._format_key(123) == "formatted_123"
        assert my_instance._format_key(None) == "formatted_None"
        assert my_instance._format_key(True) == "formatted_True"

    def test_format_key_with_special_characters(self):
        # Define a subclass that implements _format_key
        class MySubclass(CommonVariable):
            def _format_key(self, key):
                return f"formatted_{key}"
        
        # Create an instance of the subclass with a source argument
        my_instance = MySubclass(source="dummy_source")
        
        # Test with special characters in keys
        assert my_instance._format_key("!@#") == "formatted_!@#"
        assert my_instance._format_key("space key") == "formatted_space key"
        assert my_instance._format_key("newline\nkey") == "formatted_newline\nkey"
