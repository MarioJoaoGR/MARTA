
import pytest
from unittest.mock import patch
import subprocess

# Assuming _run_command is defined in a module named 'module'
def _run_command(command):
    if command == "ls -l":
        return subprocess.CompletedProcess(args="ls -l", returncode=0, stdout="stdout_output", stderr="stderr_output")
    elif command == "":
        return subprocess.CompletedProcess(args="", returncode=0, stdout="", stderr="")
    else:
        raise ValueError("Invalid command")

@pytest.fixture
def module():
    class ModuleMock:
        def run_command(self, command, check_rc):
            if check_rc and command == "ls -l":
                return _run_command(command)
            elif check_rc and command == "":
                return _run_command(command)
            else:
                raise ValueError("Invalid command")
    return ModuleMock()

def test_valid_input(module):
    with patch('subprocess.run', side_effect=_run_command):
        result = module._run_command('ls -l')
        assert result is not None
        assert result.stdout == "stdout_output"
        assert result.stderr == "stderr_output"

def test_none_input(module):
    with patch('subprocess.run', side_effect=_run_command):
        with pytest.raises(ValueError):
            module._run_command(None)

def test_empty_string_input(module):
    with patch('subprocess.run', side_effect=_run_command):
        result = module._run_command('')
        assert result is not None
        assert result.stdout == ""
        assert result.stderr == ""
