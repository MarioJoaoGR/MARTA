
import pytest
from typesystem.base import Message, Position

def test_valid_inputs():
    with pytest.raises(TypeError):
        msg = Message(text='Valid text', code='custom', key=123, index=['users', 3, 'username'], position=Position(line=1, column=2))
