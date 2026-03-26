
import typing
from dataclasses import dataclass, fields as dc_fields
from marshmallow import Schema, fields
from dataclasses_json.mm import _user_overrides_or_exts, build_type, MISSING, _is_optional

def schema(cls, mixin, infer_missing):
    """
    Generates a Marshmallow schema based on the provided dataclass and optional parameters.

    This function constructs a schema dictionary by analyzing the fields of the given dataclass and applying any user-defined overrides or extensions specified in class metadata. It supports various Python types, including optional fields, unions, and custom options for field generation. The function also handles nested structures and provides warnings for unsupported or unknown types.

    Parameters:
        cls (type): The dataclass type to be used as the base for generating the schema.
        mixin (type): A class used as a mixin for dataclass fields, which can customize field generation behavior.
        infer_missing (bool): A flag indicating whether to infer missing parameters and set them accordingly in the generated schema. If False, default values must be explicitly provided in the dataclass definitions.

    Returns:
        dict: A dictionary representing the Marshmallow schema for the given dataclass, with fields configured according to their metadata and options.
    """
    schema = {}
    overrides = _user_overrides_or_exts(cls)
    # TODO check the undefined parameters and add the proper schema action
    #  https://marshmallow.readthedocs.io/en/stable/quickstart.html
    for field in dc_fields(cls):
        metadata = overrides[field.name]
        if metadata.mm_field is not None:
            schema[field.name] = metadata.mm_field
        else:
            type_ = field.type
            options: typing.Dict[str, typing.Any] = {}
            missing_key = 'missing' if infer_missing else 'default'
            if field.default is not MISSING:
                options['load_default'] = field.default
            elif field.default_factory is not MISSING:
                options['load_default'] = field.default_factory()
            else:
                options['required'] = True

            if options.get('load_default', ...) is None:
                options['allow_none'] = True

            if _is_optional(type_):
                options.setdefault('load_default', None)
                options['allow_none'] = True
                if len(type_.__args__) == 2:
                    # Union[str, int, None] is optional too, but it has more than 1 typed field.
                    type_ = [tp for tp in type_.__args__ if tp is not type(None)][0]

            if metadata.letter_case is not None:
                options['data_key'] = metadata.letter_case(field.name)

            t = build_type(type_, options, mixin, field, cls)
            if field.metadata.get('dataclasses_json', {}).get('decoder'):
                # If the field defines a custom decoder, it should completely replace the Marshmallow field's conversion
                # logic.
                # From Marshmallow's documentation for the _deserialize method:
                # "Deserialize value. Concrete :class:`Field` classes should implement this method. "
                # This is the method that Field implementations override to perform the actual deserialization logic.
                # In this case we specifically override this method instead of `deserialize` to minimize potential
                # side effects, and only cancel the actual value deserialization.
                t._deserialize = lambda v, *_a, **_kw: v

            if field.type != typing.Optional[typing.Any]:
                schema[field.name] = t

    return schema

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.02s =============================
"""