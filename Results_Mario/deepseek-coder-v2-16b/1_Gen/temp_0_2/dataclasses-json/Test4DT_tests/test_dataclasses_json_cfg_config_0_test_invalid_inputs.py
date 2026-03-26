
import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError

def test_invalid_inputs():
    with pytest.raises(UndefinedParameterError):
        # Test invalid undefined parameter action
        config({}, undefined='invalid_action')
