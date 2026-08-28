
import pytest
from dataclasses_json.undefined import _UndefinedParameterAction

def test_invalid_input():
    # Attempt to instantiate an abstract class should raise a TypeError
    with pytest.raises(TypeError) as excinfo:
        action = _UndefinedParameterAction()
    assert "Can't instantiate abstract class" in str(excinfo.value)
