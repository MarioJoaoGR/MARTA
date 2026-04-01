
import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError
from typing import Optional, Callable, Dict, Union, List
import functools

def test_valid_inputs():
    # Test basic configuration
    metadata = {}
    config(metadata, encoder=lambda x: x, decoder=lambda y: y)
    assert 'encoder' in metadata['dataclasses_json']
    assert 'decoder' in metadata['dataclasses_json']

    # Test custom field name and letter case handling
    def custom_case(name):
        return name.lower()

    config(metadata, letter_case=custom_case, field_name="Name")
    assert metadata['dataclasses_json']['letter_case']('Name') == 'name'

    # Test handling undefined parameters
    with pytest.raises(UndefinedParameterError) as excinfo:
        config(metadata, undefined="ignore")
    assert str(excinfo.value) == "Invalid undefined parameter action, must be one of ['INCLUDE', 'RAISE', 'EXCLUDE']"
