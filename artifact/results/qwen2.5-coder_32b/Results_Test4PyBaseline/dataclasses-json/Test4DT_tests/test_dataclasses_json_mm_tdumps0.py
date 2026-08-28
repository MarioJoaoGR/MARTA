
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin

@dataclass
class MyDataClass(DataClassJsonMixin):
    name: str
    age: int

def test_dumps_default_encoder():
    my_instance = MyDataClass(name="Alice", age=30)
    assert my_instance.to_json() == '{"name": "Alice", "age": 30}'

def test_dumps_custom_encoder():
    import json

    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, MyDataClass):
                return {'custom_name': obj.name, 'custom_age': obj.age}
            return super().default(obj)

    my_instance = MyDataClass(name="Bob", age=25)