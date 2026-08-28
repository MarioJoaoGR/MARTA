
import pytest
from thefuck.types import CorrectedCommand

def example_side_effect(command, arg):
    pass  # Placeholder for actual side effect function

@pytest.fixture
def cmd():
    return CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)

def test_get_script_without_repeat(cmd):
    assert cmd._get_script() == "echo 'Hello, World!'"

@pytest.mark.xfail(reason="Expected to raise TypeError because of missing settings")
def test_get_script_with_repeat():
    with pytest.raises(TypeError):
        cmd = CorrectedCommand("echo 'Hello, World!'", example_side_effect, 1)
        assert cmd._get_script() == "echo 'Hello, World!'"
