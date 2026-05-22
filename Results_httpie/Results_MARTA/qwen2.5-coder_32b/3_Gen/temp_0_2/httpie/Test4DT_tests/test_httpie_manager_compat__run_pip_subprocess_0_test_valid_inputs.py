
import subprocess
from typing import List
from unittest.mock import patch

class PipError(Exception):
    def __init__(self, stdout: bytes, stderr: bytes):
        self.stdout = stdout
        self.stderr = stderr
        super().__init__(stdout, stderr)

def _run_pip_subprocess(pip_executable: List[str], args: List[str]) -> bytes:
    """Executes a subprocess invocation for pip with specified arguments.

    This function is designed to run a subprocess that executes the pip command with given arguments. The `pip_executable` parameter should be a list of strings representing the pip executable and any additional arguments to be passed to it, such as ['pip', '--isolated']. The `args` parameter represents additional arguments for the pip command, which are appended to the end of the `pip_executable` list before running the command.

    Parameters:
        pip_executable (List[str]): A list of strings representing the pip executable and any additional arguments to be passed to it. For example, `['pip', '--isolated']`.
        args (List[str]): Additional arguments to pass to the pip command. These are appended to the end of the `pip_executable` list before running the command.

    Returns:
        bytes: The standard output captured from the subprocess as a byte string.

    Raises:
        PipError: If the pip command exits with an error status code, this exception is raised with the stdout and stderr messages from the failed command.
    """
    cmd = [*pip_executable, *args]
    try:
        process = subprocess.run(
            cmd,
            check=True,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as error:
        raise PipError(error.stdout, error.stderr) from error
    else:
        return process.stdout

# Test case for valid inputs
def test_valid_inputs():
    with patch('subprocess.run') as mock_run:
        # Mock the subprocess.run to return a successful output
        mock_run.return_value.stdout = b'Success Output'
        
        # Call the function with valid inputs
        result = _run_pip_subprocess(['pip', '--isolated'], ['install', 'somepackage'])
        
        # Assert that the function returned the expected output
        assert result == b'Success Output'
