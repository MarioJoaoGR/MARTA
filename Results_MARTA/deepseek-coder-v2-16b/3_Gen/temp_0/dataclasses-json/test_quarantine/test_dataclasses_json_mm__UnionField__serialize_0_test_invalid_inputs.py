
from dataclasses_json.mm import _UnionField
import warnings
from typing import Union, get_origin, issubclass as is_subclass
from dataclasses import is_dataclass

class _UnionField:
    """
    A class representing a union field descriptor for defining and managing fields in a class.

    Parameters:
        desc (dict): A dictionary where keys are possible types that can be part of a typing.Union, and values are the schema objects responsible for serializing those types.
        cls (type): The class to which this union field belongs.
        field (str): The name of the field within the class that will be part of the union.

    Examples:
        To create a union field in a class, you can use the following code:
        
        ```python
        class MyClass:
            pass

        my_union_field = _UnionField({"int": int, "str": str}, MyClass, "my_field")
        ```

    This will add an attribute `my_field` to the `MyClass` class with a description of "A description".

    Note that this class is designed for internal use and should not be instantiated directly. It is used by other parts of the system to manage union fields in classes.
    
    Implementation Details:
        The function initializes an instance of _UnionField with provided parameters, including a description, the associated class, and the field name. This constructor method sets up the necessary attributes for managing the union field within the class.
        
        Parameters:
            desc (dict): A dictionary where keys are possible types that can be part of a typing.Union, and values are the schema objects responsible for serializing those types.
            cls (type): The Python type or class to which this union field belongs.
            field (str): The name of the specific field within the class that is part of the union.
    """
    def __init__(self, desc, cls, field, *args, **kwargs):
        self.desc = desc
        self.cls = cls
        self.field = field
        super().__init__(*args, **kwargs)

    def _serialize(self, value, attr, obj, **kwargs):
        """
        Serializes the given dataclass instance based on its type using the corresponding schema from `desc`.
        
        Parameters:
            value (Any): The value to be serialized.
            attr (str): The attribute name of the field being processed.
            obj (dataclass): The dataclass instance that contains the field.
            **kwargs: Additional keyword arguments passed to the marshmallow schema serializer.
        
        Returns:
            dict or None: A dictionary representation of the value, including a '__type' key indicating the type of the original value if it matches any specified union type; otherwise, returns None.
        """
        if self.allow_none and value is None:
            return None
        for type_, schema_ in self.desc.items():
            if is_subclass(type(value), type_) or (get_origin(type_) == Union and any(is_subclass(type(value), t) for t in get_args(type_))):
                if is_dataclass(value):
                    res = schema_._serialize(value, attr, obj, **kwargs)
                    res['__type'] = str(type_.__name__)
                    return res
                break
            elif isinstance(value, get_origin(type_)):
                return schema_._serialize(value, attr, obj, **kwargs)
        else:
            warnings.warn(
                f'The type "{type(value).__name__}" (value: "{value}") '
                f'is not in the list of possible types of typing.Union '
                f'(dataclass: {self.cls.__name__}, field: {self.field}). '
                f'Value cannot be serialized properly.')
        return super()._serialize(value, attr, obj, **kwargs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs.py:4:0: E0611: No name 'issubclass' in module 'typing' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs.py:7:0: E0102: class already defined line 2 (function-redefined)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs.py:57:11: E1101: Instance of '_UnionField' has no 'allow_none' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs.py:60:123: E0602: Undefined variable 'get_args' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm__UnionField__serialize_0_test_invalid_inputs.py:74:15: E1101: Super of '_UnionField' has no '_serialize' member (no-member)


"""