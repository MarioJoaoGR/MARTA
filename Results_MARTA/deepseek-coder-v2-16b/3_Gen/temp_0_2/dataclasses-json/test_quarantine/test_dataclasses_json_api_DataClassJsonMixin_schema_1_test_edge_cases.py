
from dataclasses_json import api
from typing import Type, Optional

class DataClassJsonMixin:
    """
        DataClassJsonMixin is an ABC that functions as a Mixin.
    
        As with other ABCs, it should not be instantiated directly.
        """
    dataclass_json_config: Optional[dict] = None

def schema(cls: Type[A], *, infer_missing: bool = False, only=None, exclude=(), many: bool = False, context=None, load_only=(), dump_only=(), partial: bool = False, unknown=None) -> "SchemaType[A]":
    """
    Generates a Marshmallow schema for the given dataclass and optional mixin class.

    This function constructs a custom schema class based on the provided dataclass (`cls`) and an optional mixin class. It dynamically creates a new schema type that inherits from `marshmallow.Schema` and includes specific metadata, post-load methods, and dump/dumps methods tailored to the structure of the dataclass.

    Parameters:
        cls (type): The dataclass for which to generate a schema.
        infer_missing (bool): A flag indicating whether to infer missing properties such as default values or required status for fields that do not have these specified by the user. If set to True, it will assume all unspecified fields are required unless otherwise indicated by their metadata.
        only (list | tuple | None): Specifies a list of field names to include in the schema. Only the listed fields and their nested structures will be included. If not provided, all fields will be included.
        exclude (tuple): A tuple of field names to exclude from the schema. These fields will not appear in the generated schema.
        many (bool): Indicates whether the schema should be designed for handling a list of instances (`many=True`) or a single instance (`many=False`). This affects how data is serialized and deserialized, especially when dealing with collections like lists or sets.
        context (dict | None): A dictionary that can be used to pass additional information to the schema during its construction. This can be useful for customizing behavior based on specific runtime conditions.
        load_only (tuple): Specifies a tuple of field names that should only be loaded during deserialization, not included in serialization. Useful for fields that are only needed temporarily during input processing but not exposed externally.
        dump_only (tuple): Specifies a tuple of field names that should only be dumped during serialization, not included in deserialization. This is useful for sensitive or read-only fields that should not be modified by external inputs.
        partial (bool): A flag indicating whether the schema should be created with support for partial data. This can be useful when creating schemas where some fields may be optional or missing in certain contexts.
        unknown (str | None): Specifies how to handle unknown (extra) field names during deserialization. If set to 'ignore', extra fields are ignored; if set to 'preserve', extra fields are included as-is; if set to 'raise', an error is raised for unexpected fields.

    Returns:
        type: A new subclass of `marshmallow.Schema` that is dynamically generated to match the structure and metadata of the provided dataclass, optionally extended by the mixin class.

    Examples:
        To generate a schema for a dataclass `MyDataClass` with an optional mixin, you can call the function as follows:
        
        ```python
        from my_module import MyDataClass, build_schema

        class MyMixin: pass  # Define your mixin class here if needed.

        DataClassSchema = build_schema(MyDataClass, MyMixin, infer_missing=True, partial=False)
        print(DataClassSchema.__name__)
        ```

    Note:
        This function relies on the `marshmallow` library for schema generation and expects that all necessary dependencies are installed. The generated schema includes methods to serialize (`dumps`) and deserialize (`dump`) instances of the dataclass, handling missing or undefined parameters as specified by the `partial` flag.
    """
    Schema = api.build_schema(cls, DataClassJsonMixin, infer_missing=infer_missing, partial=partial)

    if unknown is None:
        undefined_parameter_action = _undefined_parameter_action_safe(cls)
        if undefined_parameter_action is not None:
            # We can just make use of the same-named mm keywords
            unknown = undefined_parameter_action.name.lower()

    return Schema(only=only, exclude=exclude, many=many, context=context, load_only=load_only, dump_only=dump_only, partial=partial, unknown=unknown)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_DataClassJsonMixin_schema_1_test_edge_cases
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1_test_edge_cases.py:13:21: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_DataClassJsonMixin_schema_1_test_edge_cases.py:52:37: E0602: Undefined variable '_undefined_parameter_action_safe' (undefined-variable)


"""