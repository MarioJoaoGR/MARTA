
import pytest
from subprocess import CalledProcessError, TimeoutExpired
from unittest.mock import patch

def error_wrapper(err: ExcType) -> ExcType:
    r"""Wrap exceptions raised in :py:mod:`subprocess` to output captured output by default.
    """
    if not isinstance(err, (CalledProcessError, TimeoutExpired)):
        return err

    def __str__(self):
        string = super(self.__class__, self).__str__()
        if self.output:
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

    err.__class__ = new_type
    return err  # type: ignore[return-value]

@pytest.mark.parametrize("error", [CalledProcessError(1, b"command", output=b"output"), TimeoutExpired("command", timeout=1, output=b"output")])
def test_invalid_inputs(error):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        wrapped_error = error_wrapper(error)
        assert str(wrapped_error) == f"{error.__class__.__name__}(): {error.cmd}\nCaptured output:\n    output"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_run_error_wrapper_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_invalid_inputs.py:6:23: E0602: Undefined variable 'ExcType' (undefined-variable)
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_invalid_inputs.py:6:35: E0602: Undefined variable 'ExcType' (undefined-variable)
flutes/Test4DT_tests/test_flutes_run_error_wrapper_0_test_invalid_inputs.py:34:33: E0602: Undefined variable 'StringIO' (undefined-variable)


"""