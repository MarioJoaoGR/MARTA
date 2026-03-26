
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, Type

class UndefinedParameterError(Exception):
    """Raised when an undefined parameter is encountered."""
    pass

class _RaiseUndefinedParameters:
    @classmethod
    def handle_from_dict(cls, data_class: Type['ConfigParameters'], kvs: Dict[str, Any]) -> 'ConfigParameters':
        known_params = {f.name: None for f in fields(data_class)}  # Initialize with field names
        unknown_params = set(kvs.keys()) - set(known_params.keys())
        
        if unknown_params:
            raise UndefinedParameterError(f"Unknown parameters found: {unknown_params}")
        
        return data_class(**{**known_params, **kvs})

@dataclass
class ConfigParameters:
    param1: int
    param2: str
    param3: float
    param4: bool

def test_handle_from_dict_with_valid_parameters():
    kvs = {'param1': 1, 'param2': 'value', 'param3': 3.14, 'param4': True}
    config = _RaiseUndefinedParameters.handle_from_dict(ConfigParameters, kvs)
    assert isinstance(config, ConfigParameters)
    assert config.param1 == 1
    assert config.param2 == 'value'
    assert config.param3 == 3.14
    assert config.param4 is True

def test_handle_from_dict_with_unknown_parameters():
    kvs = {'param1': 1, 'param2': 'value', 'param3': 3.14, 'param5': 'unknown'}
    with pytest.raises(UndefinedParameterError) as excinfo:
        _RaiseUndefinedParameters.handle_from_dict(ConfigParameters, kvs)
    assert str(excinfo.value) == "Unknown parameters found: {'param5'}"

def test_handle_from_dict_with_missing_parameters():
    kvs = {'param1': 1, 'param2': 'value', 'param3': 3.14}
    config = _RaiseUndefinedParameters.handle_from_dict(ConfigParameters, kvs)
    assert isinstance(config, ConfigParameters)
    assert config.param1 == 1
    assert config.param2 == 'value'
    assert config.param3 == 3.14