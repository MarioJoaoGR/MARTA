
import pytest
from thefuck.rules.lein_not_task import match
from thefuck.types import Command

def test_valid_input():
    command = Command(script='lein test', output="Error: The task you have entered is not a task. See 'lein help' Did you mean this?")
    assert match(command) == True

def test_missing_attributes():
    with pytest.raises(AttributeError):
        command = {'script': 'lein test'}
        match(command)

def test_invalid_output():
    command = Command(script='lein test', output="This is a different error message.")
    assert not match(command)
