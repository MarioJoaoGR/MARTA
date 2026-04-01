
import pytest
from dataclasses import dataclass
from typing import Optional, Union, Tuple, Callable
import json
from dataclasses_json import DataClassJsonMixin

@dataclass
class Person:
    name: str
    age: int

p = Person(name='John', age=30)

def test_valid_case():
    class ExtendedEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Person):
                return {'name': obj.name, 'age': obj.age}
            return super().default(obj)
    
    config = {
        "skipkeys": False,
        "ensure_ascii": True,
        "check_circular": True,
        "allow_nan": True,
        "indent": None,
        "separators": None,
        "default": ExtendedEncoder().default,
        "sort_keys": False
    }
    
    expected_output = json.dumps({'name': 'John', 'age': 30}, cls=ExtendedEncoder)
    
    class DataClassJsonMixinMock(DataClassJsonMixin):
        dataclass_json_config: Optional[dict] = None
        
        def to_dict(self, encode_json=False):
            return {'name': self.name, 'age': self.age}
    
    person_mock = DataClassJsonMixinMock()
    person_mock.name = 'John'
    person_mock.age = 30
    
    result = person_mock.to_json(**config)
    assert result == expected_output
