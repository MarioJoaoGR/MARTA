
import typing
from dataclasses import fields as dc_fields
from marshmallow import Schema, post_load
from dataclasses_json.mm import schema

def build_schema(cls: typing.Type[A], mixin, infer_missing, partial) -> typing.Type["SchemaType[A]"]:
    """
    Generates a Marshmallow schema for the given dataclass and optional parameters.

    This function constructs a custom schema class based on the provided dataclass and any additional mixins or configurations. It dynamically creates a subclass of `marshmallow.Schema` with specific fields, metadata, and methods tailored to the structure and requirements of the dataclass. The schema includes functionality for encoding (serialization) and decoding (deserialization) using custom encoders and decoders as needed.

    Parameters:
        cls (type): The dataclass class to be converted into a schema.
        mixin (type): A class used as a mixin for additional field configurations or methods.
        infer_missing (bool): If True, automatically infers default values for fields without explicit defaults; if False, marks such fields as required.
        partial (bool): Indicates whether the schema should allow partial data during deserialization.

    Returns:
        type: A subclass of `marshmallow.Schema` that represents the generated schema for the dataclass.
    """
    Meta = type('Meta', (), {
        'fields': tuple(field.name for field in dc_fields(cls)  # type: ignore
                        if field.name != 'dataclass_json_config' and field.type != typing.Optional[CatchAllVar]),
        # TODO #180
        # 'render_module': global_config.json_module
    })

    @post_load
    def make_instance(self, kvs, **kwargs):
        return _decode_dataclass(cls, kvs, partial)

    def dumps(self, *args, **kwargs):
        if 'cls' not in kwargs:
            kwargs['cls'] = _ExtendedEncoder

        return Schema.dumps(self, *args, **kwargs)

    def dump(self, obj, *, many=None):
        many = self.many if many is None else bool(many)
        dumped = Schema.dump(self, obj, many=many)
        # TODO This is hacky, but the other option I can think of is to generate a different schema
        #  depending on dump and load, which is even more hacky

        # The only problem is the catch-all field, we can't statically create a schema for it,
        # so we just update the dumped dict
        if many:
            for i, _obj in enumerate(obj):
                dumped[i].update(
                    _handle_undefined_parameters_safe(cls=_obj, kvs={}, usage="dump"))
        else:
            dumped.update(_handle_undefined_parameters_safe(cls=obj, kvs={}, usage="dump"))
        return dumped

    schema_ = schema(cls, mixin, infer_missing)
    DataClassSchema: typing.Type["SchemaType[A]"] = type(
        f'{cls.__name__.capitalize()}Schema',
        (Schema,),
        {'Meta': Meta,
         f'make_{cls.__name__.lower()}': make_instance,
         'dumps': dumps,
         'dump': dump,
         **schema_})

    return DataClassSchema

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_mm_build_schema_0_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:7:34: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:24:99: E0602: Undefined variable 'CatchAllVar' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:31:15: E0602: Undefined variable '_decode_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:35:28: E0602: Undefined variable '_ExtendedEncoder' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:50:20: E0602: Undefined variable '_handle_undefined_parameters_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_0_test_invalid_inputs.py:52:26: E0602: Undefined variable '_handle_undefined_parameters_safe' (undefined-variable)


"""