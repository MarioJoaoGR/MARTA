
from pytutils.enum import IntEnum
import pytest

class LookupEnumMixin:
    @classmethod
    def lookup_by_any(cls):
        """
        Retrieves a dictionary containing all items from both `lookup_by_name` and `lookup_by_value` attributes of the class.

        This method constructs a combined dictionary where keys are names and values are corresponding values, merging the data from `lookup_by_name` and `lookup_by_value`. It is typically used to provide a unified lookup mechanism for both naming and value-based access within a class.

        Parameters:
            cls (type): The enum type whose lookup dictionaries should be combined.

        Returns:
            dict: A dictionary containing all items from `lookup_by_name` and `lookup_by_value`.

        Example:
            To use this function with an example enum class `MyEnum` that has attributes `lookup_by_name` and `lookup_by_value`, you can call it as follows:

            ```python
            MyEnum = type('MyEnum', (IntEnum,), {'lookup_by_name': {1: 'one', 2: 'two'}, 'lookup_by_value': {0: 'zero', 1: 'one'}})
            combined_lookup = LookupEnumMixin.lookup_by_any(MyEnum)
            print(combined_lookup)  # Output will be {'one': 1, 'two': 2, 'zero': 0}
            ```

            This example assumes `IntEnum` is imported or defined elsewhere in the codebase for use with `MyEnum`.
        """
        lookup = dict(cls.lookup_by_name)
        lookup.update(cls.lookup_by_value)
        return lookup

# Test case to check invalid input
def test_invalid_input():
    class MyEnum(IntEnum):
        ONE = 1
        TWO = 2
    
    MyEnum.lookup_by_name = {1: 'one', 2: 'two'}
    MyEnum.lookup_by_value = {0: 'zero', 1: 'one'}
    
    with pytest.raises(TypeError):
        LookupEnumMixin.lookup_by_any()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_invalid_input
pytutils/Test4DT_tests/test_pytutils_enum_LookupEnumMixin_lookup_by_any_0_test_invalid_input.py:2:0: E0611: No name 'IntEnum' in module 'pytutils.enum' (no-name-in-module)


"""