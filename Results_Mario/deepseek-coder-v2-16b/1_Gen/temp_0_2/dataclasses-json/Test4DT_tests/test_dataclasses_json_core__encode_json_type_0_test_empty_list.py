
import pytest
from dataclasses import dataclass, fields
from typing import List, Dict, Union
from dataclasses_json.core import _encode_json_type

@dataclass
class ExampleClass:
    value: Union[List, Dict]

def test_empty_list():
    example = ExampleClass(value=[])
    encoded = _encode_json_type(example.value)
    assert encoded == []
