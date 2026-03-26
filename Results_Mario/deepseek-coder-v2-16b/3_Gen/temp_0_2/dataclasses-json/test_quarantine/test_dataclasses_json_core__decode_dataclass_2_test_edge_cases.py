
import pytest
from dataclasses import dataclass, fields, MISSING
from typing import get_type_hints
from dataclasses_json.core import _isinstance_safe, _user_overrides_or_exts, _decode_letter_case_overrides, _handle_undefined_parameters_safe, _is_optional, _is_new_type, _is_supported_generic, _support_extended_types
from dataclasses_json.core import is_dataclass, _decode_dataclass, _decode_generic

@pytest.fixture
def sample_dataclass():
    @dataclass
    class Sample:
        name: str
        age: int = 0

    return Sample

def test_edge_cases(sample_dataclass):
    kvs = {'name': 'John', 'age': '30'}
    instance = _decode_dataclass(sample_dataclass, kvs, infer_missing=True)
    assert isinstance(instance, sample_dataclass)
    assert instance.name == 'John'
    assert instance.age == 30
