
from dataclasses import dataclass
import json

# Assuming these are the definitions of Address and PersonWithAddress
@dataclass
class Address:
    city: str
    zip_code: int

@dataclass
class PersonWithAddress:
    name: str
    age: int
    address: Address

def _asdict(obj, encode_json=False):
    # This is a placeholder for the actual implementation of _asdict
    result = obj.__dict__.copy()
    if encode_json and 'address' in result:
        result['address'] = json.dumps(result['address'].__dict__)
    return result

# Test case
def test_asdict_nested_dataclass_encode():
    address = Address(city="Wonderland", zip_code=12345)
    person_with_address = PersonWithAddress(name="Bob", age=25, address=address)
    result = _asdict(person_with_address, encode_json=True)
    assert result == {'name': 'Bob', 'age': 25, 'address': '{"city": "Wonderland", "zip_code": 12345}'}
