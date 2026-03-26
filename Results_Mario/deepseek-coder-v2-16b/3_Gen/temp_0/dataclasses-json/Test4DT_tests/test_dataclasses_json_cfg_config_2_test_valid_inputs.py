
import pytest
from dataclasses import dataclass
from typing import Optional, Callable, Dict, Union
from dataclasses_json import dataclass_json, config
from dataclasses_json.cfg import Undefined, UndefinedParameterError

def test_valid_inputs():
    @dataclass
    class Example:
        a: int
        b: str = "default"
        c: Optional[int] = None

    metadata = {}
    new_metadata = config(metadata, encoder=lambda x: x, decoder=lambda y: y)
    assert 'dataclasses_json' in new_metadata
    assert 'encoder' in new_metadata['dataclasses_json']
    assert 'decoder' in new_metadata['dataclasses_json']

    @dataclass
    class Example2:
        a_camel_case: int

    metadata = {}
    new_metadata = config(metadata, letter_case=lambda s: s.upper())
    assert 'letter_case' in new_metadata['dataclasses_json']
    assert callable(new_metadata['dataclasses_json']['letter_case'])

    @dataclass
    class Example3:
        a: int
        b: str = "default"

    metadata = {}
    with pytest.raises(UndefinedParameterError):
        new_metadata = config(metadata, undefined="ignore")
