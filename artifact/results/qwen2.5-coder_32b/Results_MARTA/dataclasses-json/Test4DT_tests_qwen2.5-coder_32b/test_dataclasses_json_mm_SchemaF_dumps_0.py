
import pytest
from dataclasses import dataclass
import typing
from dataclasses_json.mm import SchemaF

@dataclass
class User:
    name: str
    age: int

# Subclass SchemaF to implement custom serialization logic
class MySchema(SchemaF):
    def dump(self, obj: typing.List[User], many=None) -> typing.List[str]:
        if many is None:
            many = isinstance(obj, list)
        
        if many:
            return [self._serialize(user) for user in obj]
        else:
            return self._serialize(obj)

    def _serialize(self, user: User) -> str:
        import json
        return json.dumps(user.__dict__)

# Test that attempting to instantiate SchemaF raises NotImplementedError
def test_schemaf_instantiation():
    with pytest.raises(NotImplementedError):
        schema_instance = SchemaF()

# Test dumping a list of users using MySchema

# Test dumping a single user using MySchema