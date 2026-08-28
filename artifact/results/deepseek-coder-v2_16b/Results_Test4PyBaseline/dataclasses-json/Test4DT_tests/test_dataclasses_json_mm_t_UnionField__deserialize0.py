
import pytest
from dataclasses import dataclass
from typing import Union, List
from warnings import simplefilter
from unittest.mock import patch
from copy import deepcopy
import json  # Importing the module here to resolve pylint error

# Import the function from the module
from dataclasses_json.mm import _UnionField  # Replace with actual module name and path

@dataclass
class ExampleDataClass:
    value: int

schema_dict = {
    List[int]: lambda x, attr, data, **kwargs: [int(v) for v in x],
    ExampleDataClass: lambda x, attr, data, **kwargs: ExampleDataClass(**x),
}

field = "some_field"  # Replace with actual field name or metadata instance
union_field = _UnionField(desc=schema_dict, cls=ExampleDataClass, field=field)

@pytest.fixture(autouse=True)
def enable_simplefilter():
    simplefilter("ignore", category=UserWarning)

def test_init():
    desc = schema_dict
    cls = ExampleDataClass
    field_name = "some_field"
    union_field = _UnionField(desc, cls, field_name)
    assert union_field.desc == desc
    assert union_field.cls == cls