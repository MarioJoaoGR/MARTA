
import pytest
from flutes.run import run_command, CommandResult
from typing import Union, List, Optional, Dict, PathType
import subprocess
import tempfile

@pytest.mark.parametrize("args", [
    "ls -l",
    ["ls", "-l"],
    "pwd",
    ["pwd"]
])
def test_valid_inputs(args: Union[str, List[str]]):
    result = run_command(args)
    assert isinstance(result, CommandResult), f"Expected a CommandResult instance but got {type(result)}"
    if isinstance(args, list):
        expected_cmd = " ".join(args)
    else:
        expected_cmd = args
    assert result.command == expected_cmd, f"Expected command to be '{expected_cmd}' but got '{result.command}'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_run_command_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:4:0: E0611: No name 'PathType' in module 'typing' (no-name-in-module)


"""