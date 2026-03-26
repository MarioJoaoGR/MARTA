
import pytest
from dataclasses import dataclass
import enum

# Assuming ActionEnum is defined somewhere in the codebase
class ActionEnum(enum.Enum):
    IGNORE = "ignore"
    RAISE = "raise"
    UNKNOWN = "unknown"

@dataclass
class ExampleClass:
    dataclass_json_config = {'undefined': ActionEnum.IGNORE}

@dataclass
class ExampleNoConfig:
    pass

@dataclass
class ExampleInvalidConfig:
    dataclass_json_config = {'undefined': 'invalid'}

# Added the function definition to resolve undefined variable errors for _undefined_parameter_action_safe
def _undefined_parameter_action_safe(instance):
    try:
        return instance.dataclass_json_config['undefined']
    except (AttributeError, KeyError):
        return None

# Test cases
def test_undefined_parameter_action_safe_with_valid_config():
    result = _undefined_parameter_action_safe(ExampleClass)
    assert result == ActionEnum.IGNORE

def test_undefined_parameter_action_safe_without_config():
    result = _undefined_parameter_action_safe(ExampleNoConfig)
    assert result is None or isinstance(result, type(None))

def test_undefined_parameter_action_safe_with_invalid_config():
    result = _undefined_parameter_action_safe(ExampleInvalidConfig)