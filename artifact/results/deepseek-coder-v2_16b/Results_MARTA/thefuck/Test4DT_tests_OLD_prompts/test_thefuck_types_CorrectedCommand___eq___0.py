
import pytest
from thefuck.types import CorrectedCommand

def test_correctedcommand_initialization():
    def modify_command(other_command, action):
        other_command.script += action
    
    cmd = CorrectedCommand("echo 'Hello'", modify_command, 1)
    assert isinstance(cmd, CorrectedCommand)
    assert cmd.script == "echo 'Hello'"
    assert callable(cmd.side_effect)
    assert cmd.priority == 1


def test_correctedcommand_eq_different_side_effect():
    def side_effect1(command, action):
        command.script += " side_effect1"
    
    def side_effect2(command, action):
        command.script += " side_effect2"
    
    cmd1 = CorrectedCommand("echo 'Hello'", side_effect1, 1)
    cmd2 = CorrectedCommand("echo 'Hello'", side_effect2, 1)
    
    assert not (cmd1 == cmd2)

def test_correctedcommand_eq_different_script():
    def modify_command(other_command, action):
        other_command.script += action
    
    cmd1 = CorrectedCommand("echo 'Hello'", modify_command, 1)
    cmd2 = CorrectedCommand("echo 'World'", modify_command, 1)
    
    assert not (cmd1 == cmd2)