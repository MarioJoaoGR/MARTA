
import typing
from dataclasses import fields as dc_fields
from marshmallow import Schema, post_load
import typing

def build_schema(cls: typing.Type[A], mixin, infer_missing, partial) -> typing.Type["SchemaType[A]"]:
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
                dumped[i].update(_handle_undefined_parameters_safe(cls=_obj, kvs={}, usage="dump"))
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
************* Module Test4DT_tests.test_dataclasses_json_mm_build_schema_2_test_invalid_inputs
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:7:34: E0602: Undefined variable 'A' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:10:99: E0602: Undefined variable 'CatchAllVar' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:17:15: E0602: Undefined variable '_decode_dataclass' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:21:28: E0602: Undefined variable '_ExtendedEncoder' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:35:33: E0602: Undefined variable '_handle_undefined_parameters_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:37:26: E0602: Undefined variable '_handle_undefined_parameters_safe' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_mm_build_schema_2_test_invalid_inputs.py:40:14: E0602: Undefined variable 'schema' (undefined-variable)


"""