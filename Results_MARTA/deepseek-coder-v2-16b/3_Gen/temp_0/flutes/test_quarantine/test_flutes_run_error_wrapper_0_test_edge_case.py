
import subprocess
from flutes.run import CalledProcessError  # Importing the specific exception type

def error_wrapper(err: ExcType) -> ExcType:
    """Wrap exceptions raised in :py:mod:`subprocess` to output captured output by default.

    This function is designed to handle specific types of exceptions that are commonly raised during subprocess operations, such as `CalledProcessError` or `TimeoutExpired`. If the provided exception does not match these types, it returns the original error. For errors that can be handled (i.e., those two specific types), this function overrides the `__str__` method to include any captured output from the subprocess call in a user-friendly format.

    Parameters:
        err (ExcType): The exception raised by subprocess calls, expected to be either `CalledProcessError` or `TimeoutExpired`.

    Returns:
        ExcType: The wrapped exception with overridden `__str__` method that includes captured output if available. If the error is not one of the handled types, it returns the original error unchanged.

    Example:
        >>> import subprocess
        >>> try:
        ...     result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)
        ... except Exception as e:
        ...     wrapped_e = error_wrapper(e)
        ...     print(wrapped_e)
        ls: cannot access '/nonexistent_file': No such file or directory
        Captured output:
            ls: cannot access '/nonexistent_file': No such file or directory
    """
    if not isinstance(err, (CalledProcessError, subprocess.TimeoutExpired)):
        return err

    def __str__(self):
        string = super().__str__()
        if hasattr(self, 'output') and self.output:
            try:
                output = self.output.decode('utf-8')
            except UnicodeEncodeError:  # ignore output
                string += "\nFailed to parse output."
            else:
                string += "\nCaptured output:\n" + '\n'.join([f'    {line}' for line in output.split('\n')])
        else:
            string += "\nNo output was generated."
        return string

    # Dynamically create a new type that overrides __str__, because replacing __str__ on instances don't work.
    err_type = type(err)
    new_type = type(err_type.__name__, (err_type,), {"__str__": __str__})

    # Replace the class of the exception with our dynamically created one
    if not isinstance(err, Exception):  # Ensure it's an exception instance
        raise ValueError("Input must be a subprocess exception")
    err.__class__ = new_type
    return err  # type: ignore[return-value]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_error_wrapper_0_test_edge_case
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_edge_case.py:3:0: E0611: No name 'CalledProcessError' in module 'flutes.run' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_edge_case.py:5:23: E0602: Undefined variable 'ExcType' (undefined-variable)
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_edge_case.py:5:35: E0602: Undefined variable 'ExcType' (undefined-variable)

"""