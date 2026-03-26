
import pytest
from sty.lib import Register

def unmute(*objects: Register) -> None:
    err = ValueError(
        "The unmute() method can only be used with objects that inherit "
        "from the 'Register class'."
    )
    for obj in objects:
        if not isinstance(obj, Register):
            raise err
        obj.unmute()

def test_none_input():
    with pytest.raises(ValueError) as excinfo:
        unmute(None, None)
    assert str(excinfo.value) == "The unmute() method can only be used with objects that inherit from the 'Register class'."
