
from dataclasses import dataclass
from typing import Dict, Optional
import pytest
from dataclasses_json.api import DataClassJsonMixin  # Import from the correct module

# Assuming YourDataclass is defined somewhere in your_module
# from your_module import YourDataclass

@dataclass
class YourDataclass(DataClassJsonMixin):
    name: str
    age: int

def test_valid_case():
    obj = YourDataclass(name='John Doe', age=30)
    result = obj.to_dict()  # This should now work as expected
    assert isinstance(result, dict), "The result is not a dictionary"
    assert 'name' in result and result['name'] == 'John Doe', "Name field is missing or incorrect"
    assert 'age' in result and result['age'] == 30, "Age field is missing or incorrect"
