
import pytest
from dataclasses import dataclass, field, MISSING
from typing import Optional, Union
from dataclasses_json.mm import schema
from dataclasses_json import DataClassJsonMixin, LetterCase


@dataclass
class MyDataClass:
    name: str = field(metadata={'dataclasses_json': {'encoder': lambda x: x.upper()}})
    age: int
    email: Optional[str] = None

@dataclass
class AnotherDataClass:
    name: str
    age: Optional[int] = field(default=None)

@dataclass
class CaseSensitiveDataClass:
    first_name: str = field(metadata={'dataclasses_json': {'letter_case': LetterCase.CAMEL}})
    last_name: str = field(metadata={'dataclasses_json': {'letter_case': LetterCase.SNAKE}})


def test_schema_basic_usage():
    marshmallow_schema = schema(MyDataClass, DataClassJsonMixin, True)
    assert 'name' in marshmallow_schema
    assert 'age' in marshmallow_schema
    assert 'email' in marshmallow_schema


def test_schema_infer_missing_false():
    marshmallow_schema_default = schema(MyDataClass, DataClassJsonMixin, False)