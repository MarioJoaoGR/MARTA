
import pytest
from flutes.fs import get_folder_size
from pathlib import Path
import subprocess

@pytest.mark.parametrize("invalid_path", [
    "nonexistent_directory",  # Non-existent directory path
    "/non/existent/absolute/path",  # Absolute non-existent path
    123,  # Integer (not a valid path)
    None,  # None type (not a valid path)
])
def test_invalid_path(invalid_path):
    with pytest.raises(FileNotFoundError):
        get_folder_size(invalid_path)

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

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________ test_invalid_path[nonexistent_directory] ___________________

invalid_path = 'nonexistent_directory'

    @pytest.mark.parametrize("invalid_path", [
        "nonexistent_directory",  # Non-existent directory path
        "/non/existent/absolute/path",  # Absolute non-existent path
        123,  # Integer (not a valid path)
        None,  # None type (not a valid path)
    ])
    def test_invalid_path(invalid_path):
        with pytest.raises(FileNotFoundError):
>           get_folder_size(invalid_path)

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:34: in get_folder_size
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))
/usr/local/lib/python3.11/subprocess.py:466: in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = False, timeout = None, check = True
popenargs = (['du', '-bs', 'nonexistent_directory'],), kwargs = {'stdout': -1}
process = <Popen: returncode: 1 args: ['du', '-bs', 'nonexistent_directory']>
stdout = b'', stderr = None, retcode = 1

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
E               subprocess.CalledProcessError: Command '['du', '-bs', 'nonexistent_directory']' returned non-zero exit status 1.

/usr/local/lib/python3.11/subprocess.py:571: CalledProcessError
----------------------------- Captured stderr call -----------------------------
du: cannot access 'nonexistent_directory': No such file or directory
________________ test_invalid_path[/non/existent/absolute/path] ________________

invalid_path = '/non/existent/absolute/path'

    @pytest.mark.parametrize("invalid_path", [
        "nonexistent_directory",  # Non-existent directory path
        "/non/existent/absolute/path",  # Absolute non-existent path
        123,  # Integer (not a valid path)
        None,  # None type (not a valid path)
    ])
    def test_invalid_path(invalid_path):
        with pytest.raises(FileNotFoundError):
>           get_folder_size(invalid_path)

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:34: in get_folder_size
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))
/usr/local/lib/python3.11/subprocess.py:466: in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = False, timeout = None, check = True
popenargs = (['du', '-bs', '/non/existent/absolute/path'],)
kwargs = {'stdout': -1}
process = <Popen: returncode: 1 args: ['du', '-bs', '/non/existent/absolute/path']>
stdout = b'', stderr = None, retcode = 1

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
E               subprocess.CalledProcessError: Command '['du', '-bs', '/non/existent/absolute/path']' returned non-zero exit status 1.

/usr/local/lib/python3.11/subprocess.py:571: CalledProcessError
----------------------------- Captured stderr call -----------------------------
du: cannot access '/non/existent/absolute/path': No such file or directory
____________________________ test_invalid_path[123] ____________________________

invalid_path = 123

    @pytest.mark.parametrize("invalid_path", [
        "nonexistent_directory",  # Non-existent directory path
        "/non/existent/absolute/path",  # Absolute non-existent path
        123,  # Integer (not a valid path)
        None,  # None type (not a valid path)
    ])
    def test_invalid_path(invalid_path):
        with pytest.raises(FileNotFoundError):
>           get_folder_size(invalid_path)

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:34: in get_folder_size
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))
/usr/local/lib/python3.11/subprocess.py:466: in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = False, timeout = None, check = True
popenargs = (['du', '-bs', '123'],), kwargs = {'stdout': -1}
process = <Popen: returncode: 1 args: ['du', '-bs', '123']>, stdout = b''
stderr = None, retcode = 1

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
E               subprocess.CalledProcessError: Command '['du', '-bs', '123']' returned non-zero exit status 1.

/usr/local/lib/python3.11/subprocess.py:571: CalledProcessError
----------------------------- Captured stderr call -----------------------------
du: cannot access '123': No such file or directory
___________________________ test_invalid_path[None] ____________________________

invalid_path = None

    @pytest.mark.parametrize("invalid_path", [
        "nonexistent_directory",  # Non-existent directory path
        "/non/existent/absolute/path",  # Absolute non-existent path
        123,  # Integer (not a valid path)
        None,  # None type (not a valid path)
    ])
    def test_invalid_path(invalid_path):
        with pytest.raises(FileNotFoundError):
>           get_folder_size(invalid_path)

flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/fs.py:34: in get_folder_size
    return int(subprocess.check_output(['du', '-bs', str(path)]).split()[0].decode('utf-8'))
/usr/local/lib/python3.11/subprocess.py:466: in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input = None, capture_output = False, timeout = None, check = True
popenargs = (['du', '-bs', 'None'],), kwargs = {'stdout': -1}
process = <Popen: returncode: 1 args: ['du', '-bs', 'None']>, stdout = b''
stderr = None, retcode = 1

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
E               subprocess.CalledProcessError: Command '['du', '-bs', 'None']' returned non-zero exit status 1.

/usr/local/lib/python3.11/subprocess.py:571: CalledProcessError
----------------------------- Captured stderr call -----------------------------
du: cannot access 'None': No such file or directory
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py::test_invalid_path[nonexistent_directory]
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py::test_invalid_path[/non/existent/absolute/path]
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py::test_invalid_path[123]
FAILED flutes/Test4DT_tests/test_flutes_fs_get_folder_size_3_test_invalid_path.py::test_invalid_path[None]
============================== 4 failed in 0.25s ===============================
"""