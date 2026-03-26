
import pytest
from unittest.mock import patch, MagicMock
from flutes.run import run_command, CommandResult

@pytest.fixture
def command_result():
    return CommandResult("test_command", 0, b"test output")

def test_run_command_with_valid_command(command_result):
    with patch('flutes.run.subprocess.run', return_value=MagicMock(returncode=0, stdout=b"output")):
        result = run_command(["ls", "-l"])
        assert isinstance(result, CommandResult)
        assert result.args == ["ls", "-l"]
        assert result.return_code == 0
        assert result.output == b"output"

def test_run_command_with_timeout(command_result):
    with patch('flutes.run.subprocess.run', side_effect=TimeoutError("Command timed out")):
        with pytest.raises(TimeoutError):
            run_command(["sleep", "10"], timeout=1)

def test_run_command_with_ignore_errors():
    with patch('flutes.run.subprocess.run', return_value=MagicMock(returncode=-32768)):
        result = run_command(["sleep", "10"], ignore_errors=True)
        assert isinstance(result, CommandResult)
        assert result.args == ["sleep", "10"]
        assert result.return_code == -32768
        assert result.output is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_run_command_1_test_edge_cases
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:14:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:14:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:14:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:16:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:16:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:16:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:27:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:27:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:27:15: E1101: Instance of 'CommandResult' has no 'args' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:29:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:29:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_1_test_edge_cases.py:29:15: E1101: Instance of 'CommandResult' has no 'output' member (no-member)


"""