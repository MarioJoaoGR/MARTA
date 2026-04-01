
import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError

def test_invalid_inputs():
    # Test invalid undefined parameter action
    with pytest.raises(UndefinedParameterError) as excinfo:
        config({}, undefined="invalid_action")
    
    assert str(excinfo.value) == "Invalid undefined parameter action, must be one of ['INCLUDE', 'RAISE', 'EXCLUDE']"
