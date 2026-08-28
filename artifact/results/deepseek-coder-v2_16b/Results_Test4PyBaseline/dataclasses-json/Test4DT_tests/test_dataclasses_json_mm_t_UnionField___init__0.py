
import pytest
from dataclasses import dataclass
import json
from typing import List, Union
from dataclasses_json.mm import _UnionField

# Import the function from its module
from dataclasses_json.mm import _UnionField

def test_union_field_initialization():
    # Define a hypothetical dataclass for demonstration purposes
    @dataclass
    class ExampleDataClass:
        value: int

    # Define a schema dictionary that maps possible types to their corresponding serialization/deserialization logic
    schema_dict = {
        List[int]: lambda x, attr, data, **kwargs: [int(v) for v in x],
        ExampleDataClass: lambda x, attr, data, **kwargs: ExampleDataClass(**x),
    }

    # Define the field name or metadata instance
    field = "some_field"  # Replace with actual field name or metadata instance

    # Create an instance of _UnionField
    union_field = _UnionField(desc=schema_dict, cls=ExampleDataClass, field=field)

    assert union_field.desc == schema_dict
    assert union_field.cls == ExampleDataClass