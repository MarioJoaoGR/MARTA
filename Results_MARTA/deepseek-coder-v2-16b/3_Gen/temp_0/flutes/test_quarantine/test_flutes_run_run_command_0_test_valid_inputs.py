
import pytest
from flutes.run import run_command, CommandResult
import subprocess
import tempfile

@pytest.mark.parametrize("args, env, cwd, timeout, verbose, return_output, ignore_errors", [
    ("ls -l", None, None, None, False, False, False),
    (["python", "-c", "print('Hello, World!')"], {"PYTHONPATH": "/path/to/custom/lib"}, "/project/dir", 10, True, True, False)
])
def test_run_command(args, env, cwd, timeout, verbose, return_output, ignore_errors):
    result = run_command(args, env=env, cwd=cwd, timeout=timeout, verbose=verbose, return_output=return_output, ignore_errors=ignore_errors)
    
    if isinstance(args, str) and args.startswith("python"):  # Handle Python script output
        assert result.stdout is not None
        assert "Hello, World!" in result.stdout.decode('utf-8')
    else:
        with tempfile.TemporaryFile() as f:
            ret = subprocess.run(args, check=True, stdout=f, stderr=subprocess.STDOUT, timeout=timeout, env=env, cwd=str(cwd) if cwd is not None else None)
            f.seek(0)
            output = f.read()
            assert result.stdout == output
    
    if return_output:
        assert result.stdout is not None
    else:
        assert isinstance(result.returncode, int)

    if ignore_errors and (isinstance(args, str) and args.startswith("python")):
        assert result.returncode != -32768

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_run_command_0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:15:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:15:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:15:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:16:34: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:16:34: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:16:34: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:22:19: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:22:19: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:22:19: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:25:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:25:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:25:15: E1101: Instance of 'CommandResult' has no 'stdout' member (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:27:26: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:27:26: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:27:26: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:30:15: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:30:15: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)
flutes/Test4DT_tests/test_flutes_run_run_command_0_test_valid_inputs.py:30:15: E1101: Instance of 'CommandResult' has no 'returncode' member; maybe 'return_code'? (no-member)


"""