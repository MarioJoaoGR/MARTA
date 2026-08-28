
import pytest
from thefuck.types import CorrectedCommand

def modify_command(other_command, action):
    other_command.script += action

# Test scenario 1: Equality between two CorrectedCommand instances with same script and side effect but different priorities
def test_equality_with_different_priorities():
    cmd1 = CorrectedCommand("echo 'Hello'", modify_command, 1)
    cmd2 = CorrectedCommand("echo 'Hello'", modify_command, 2)
    assert cmd1 == cmd2

# Test scenario 2: Inequality between a CorrectedCommand instance and an invalid type (string)

# Test scenario 3: Equality between two CorrectedCommand instances with same script and side effect but different priority values
def test_equality_with_same_script_and_side_effect():
    cmd1 = CorrectedCommand("echo 'Hello'", modify_command, 1)
    cmd2 = CorrectedCommand("echo 'Hello'", modify_command, 3)
    assert cmd1 == cmd2