
import pytest
from dataclasses import dataclass
from dataclasses_json.utils import _undefined_parameter_action_safe

@pytest.fixture
def no_config_dataclass():
    @dataclass(frozen=True)
    class MyDataClass:
        pass
    return MyDataClass

def test_missing_config(no_config_dataclass):
    result = _undefined_parameter_action_safe(no_config_dataclass)
    assert result is None
