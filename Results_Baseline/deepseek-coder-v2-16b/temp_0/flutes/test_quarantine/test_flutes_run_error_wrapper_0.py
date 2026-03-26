
import pytest
import subprocess
from flutes.run import error_wrapper

# Test for handling a subprocess.CalledProcessError
def test_error_wrapper_calledprocesserror():
    try:
        result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        wrapped_e = error_wrapper(e)
        assert "No such file or directory" in str(wrapped_e), f"Expected 'No such file or directory' in output, but got {str(wrapped_e)}"
        assert "Captured output:" in str(wrapped_e), "Expected 'Captured output:' to be included in the error message."

# Test for handling a subprocess.TimeoutExpired
def test_error_wrapper_timeoutexpired():
    try:
        result = subprocess.run(['sleep', '10'], timeout=1, capture_output=True)
    except subprocess.TimeoutExpired as e:
        wrapped_e = error_wrapper(e)
        assert "Command timed out" in str(wrapped_e), f"Expected 'Command timed out' in output, but got {str(wrapped_e)}"
        assert "Captured output:" not in str(wrapped_e), "Unexpectedly found 'Captured output:' in the error message."

# Test for handling a custom exception
class CustomException(Exception):
    pass

def test_error_wrapper_customexception():
    try:
        raise CustomException("This is a custom exception")
    except Exception as e:
        wrapped_e = error_wrapper(e)
        assert "CustomException" in str(wrapped_e), f"Expected 'CustomException' to be included in the error message, but got {str(wrapped_e)}"
        assert "This is a custom exception" in str(wrapped_e), "Expected the original exception message to be included."

# Test for handling an exception that is not subprocess related
def test_error_wrapper_generic():
    class GenericException(Exception):
        pass
    
    err = GenericException("This is a generic exception")
    wrapped_e = error_wrapper(err)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py FFF.             [100%]

=================================== FAILURES ===================================
____________________ test_error_wrapper_calledprocesserror _____________________

    def test_error_wrapper_calledprocesserror():
        try:
>           result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = True, timeout = None, check = True
popenargs = (['ls', '-l', '/nonexistent_file'],)
kwargs = {'stderr': -1, 'stdout': -1}
process = <Popen: returncode: 2 args: ['ls', '-l', '/nonexistent_file']>
stdout = b''
stderr = b"ls: cannot access '/nonexistent_file': No such file or directory\n"
retcode = 2

    def run(*popenargs,
            input=None, capture_output=False, timeout=None, check=False, **kwargs):
        """Run command with arguments and return a CompletedProcess instance.
    
        The returned instance will have attributes args, returncode, stdout and
        stderr. By default, stdout and stderr are not captured, and those attributes
        will be None. Pass stdout=PIPE and/or stderr=PIPE in order to capture them,
        or pass capture_output=True to capture both.
    
        If check is True and the exit code was non-zero, it raises a
        CalledProcessError. The CalledProcessError object will have the return code
        in the returncode attribute, and output & stderr attributes if those streams
        were captured.
    
        If timeout is given, and the process takes too long, a TimeoutExpired
        exception will be raised.
    
        There is an optional argument "input", allowing you to
        pass bytes or a string to the subprocess's stdin.  If you use this argument
        you may not also use the Popen constructor's "stdin" argument, as
        it will be used internally.
    
        By default, all communication is in bytes, and therefore any "input" should
        be bytes, and the stdout and stderr will be bytes. If in text mode, any
        "input" should be a string, and stdout and stderr will be strings decoded
        according to locale encoding, or by "encoding" if set. Text mode is
        triggered by setting any of text, encoding, errors or universal_newlines.
    
        The other arguments are the same as for the Popen constructor.
        """
        if input is not None:
            if kwargs.get('stdin') is not None:
                raise ValueError('stdin and input arguments may not both be used.')
            kwargs['stdin'] = PIPE
    
        if capture_output:
            if kwargs.get('stdout') is not None or kwargs.get('stderr') is not None:
                raise ValueError('stdout and stderr arguments may not be used '
                                 'with capture_output.')
            kwargs['stdout'] = PIPE
            kwargs['stderr'] = PIPE
    
        with Popen(*popenargs, **kwargs) as process:
            try:
                stdout, stderr = process.communicate(input, timeout=timeout)
            except TimeoutExpired as exc:
                process.kill()
                if _mswindows:
                    # Windows accumulates the output in a single blocking
                    # read() call run on child threads, with the timeout
                    # being done in a join() on those threads.  communicate()
                    # _after_ kill() is required to collect that and add it
                    # to the exception.
                    exc.stdout, exc.stderr = process.communicate()
                else:
                    # POSIX _communicate already populated the output so
                    # far into the TimeoutExpired exception.
                    process.wait()
                raise
            except:  # Including KeyboardInterrupt, communicate handled that.
                process.kill()
                # We don't call process.wait() as .__exit__ does that for us.
                raise
            retcode = process.poll()
            if check and retcode:
>               raise CalledProcessError(retcode, process.args,
                                         output=stdout, stderr=stderr)
E               flutes.run.CalledProcessError: Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.
E               No output was generated.

/usr/local/lib/python3.11/subprocess.py:571: CalledProcessError

During handling of the above exception, another exception occurred:

    def test_error_wrapper_calledprocesserror():
        try:
            result = subprocess.run(['ls', '-l', '/nonexistent_file'], check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            wrapped_e = error_wrapper(e)
>           assert "No such file or directory" in str(wrapped_e), f"Expected 'No such file or directory' in output, but got {str(wrapped_e)}"
E           AssertionError: Expected 'No such file or directory' in output, but got Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.
E             No output was generated.
E           assert 'No such file or directory' in "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.\nNo output was generated."
E            +  where "Command '['ls', '-l', '/nonexistent_file']' returned non-zero exit status 2.\nNo output was generated." = str(CalledProcessError(2, ['ls', '-l', '/nonexistent_file']))

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:12: AssertionError
______________________ test_error_wrapper_timeoutexpired _______________________

    def test_error_wrapper_timeoutexpired():
        try:
>           result = subprocess.run(['sleep', '10'], timeout=1, capture_output=True)

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/subprocess.py:550: in run
    stdout, stderr = process.communicate(input, timeout=timeout)
/usr/local/lib/python3.11/subprocess.py:1209: in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
/usr/local/lib/python3.11/subprocess.py:2116: in _communicate
    self._check_timeout(endtime, orig_timeout, stdout, stderr)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Popen: returncode: -9 args: ['sleep', '10']>
endtime = 1306710.162831945, orig_timeout = 1, stdout_seq = [], stderr_seq = []
skip_check_and_raise = False

    def _check_timeout(self, endtime, orig_timeout, stdout_seq, stderr_seq,
                       skip_check_and_raise=False):
        """Convenience for checking if a timeout has expired."""
        if endtime is None:
            return
        if skip_check_and_raise or _time() > endtime:
>           raise TimeoutExpired(
                    self.args, orig_timeout,
                    output=b''.join(stdout_seq) if stdout_seq else None,
                    stderr=b''.join(stderr_seq) if stderr_seq else None)
E           flutes.run.TimeoutExpired: Command '['sleep', '10']' timed out after 1 seconds
E           No output was generated.

/usr/local/lib/python3.11/subprocess.py:1253: TimeoutExpired

During handling of the above exception, another exception occurred:

    def test_error_wrapper_timeoutexpired():
        try:
            result = subprocess.run(['sleep', '10'], timeout=1, capture_output=True)
        except subprocess.TimeoutExpired as e:
            wrapped_e = error_wrapper(e)
>           assert "Command timed out" in str(wrapped_e), f"Expected 'Command timed out' in output, but got {str(wrapped_e)}"
E           AssertionError: Expected 'Command timed out' in output, but got Command '['sleep', '10']' timed out after 1 seconds
E             No output was generated.
E           assert 'Command timed out' in "Command '['sleep', '10']' timed out after 1 seconds\nNo output was generated."
E            +  where "Command '['sleep', '10']' timed out after 1 seconds\nNo output was generated." = str(TimeoutExpired(['sleep', '10'], 1))

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:21: AssertionError
______________________ test_error_wrapper_customexception ______________________

    def test_error_wrapper_customexception():
        try:
>           raise CustomException("This is a custom exception")
E           Test4DT_tests.test_flutes_run_error_wrapper_0.CustomException: This is a custom exception

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:30: CustomException

During handling of the above exception, another exception occurred:

    def test_error_wrapper_customexception():
        try:
            raise CustomException("This is a custom exception")
        except Exception as e:
            wrapped_e = error_wrapper(e)
>           assert "CustomException" in str(wrapped_e), f"Expected 'CustomException' to be included in the error message, but got {str(wrapped_e)}"
E           AssertionError: Expected 'CustomException' to be included in the error message, but got This is a custom exception
E           assert 'CustomException' in 'This is a custom exception'
E            +  where 'This is a custom exception' = str(CustomException('This is a custom exception'))

flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py:33: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py::test_error_wrapper_calledprocesserror
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py::test_error_wrapper_timeoutexpired
FAILED flutes/Test4DT_tests/test_flutes_run_error_wrapper_0.py::test_error_wrapper_customexception
========================= 3 failed, 1 passed in 1.18s ==========================
"""