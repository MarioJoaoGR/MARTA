
import pytest
from dataclasses import dataclass
from dataclasses_json.utils import _undefined_parameter_action_safe

@dataclass
class NoConfigDataclass:
    pass

def test_none_configuration():
    result = _undefined_parameter_action_safe(NoConfigDataclass)
    assert result is None, "Expected None when dataclass has no configuration"
