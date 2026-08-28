
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.dist import remove_dists
import os



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('semantic_release.dist.logger', MagicMock()):
            # Assuming the directory exists and is empty for this test case
>           remove_dists('/tmp/existing_dir')

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/dist.py:34: in remove_dists
    run(command)
/data/pydeps/sut/invoke/__init__.py:52: in run
    return Context().run(command, **kwargs)
/data/pydeps/sut/invoke/context.py:122: in run
    return self._run(runner, command, **kwargs)
/data/pydeps/sut/invoke/context.py:129: in _run
    return runner.run(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:403: in run
    return self._run_body(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:469: in _run_body
    return self.make_promise() if self._asynchronous else self._finish()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <invoke.runners.Local object at 0x7f891fdff670>

    def _finish(self) -> "Result":
        # Wait for subprocess to run, forwarding signals as we get them.
        try:
            while True:
                try:
                    self.wait()
                    break  # done waiting!
                # Don't locally stop on ^C, only forward it:
                # - if remote end really stops, we'll naturally stop after
                # - if remote end does not stop (eg REPL, editor) we don't want
                # to stop prematurely
                except KeyboardInterrupt as e:
                    self.send_interrupt(e)
                # TODO: honor other signals sent to our own process and
                # transmit them to the subprocess before handling 'normally'.
        # Make sure we tie off our worker threads, even if something exploded.
        # Any exceptions that raised during self.wait() above will appear after
        # this block.
        finally:
            # Inform stdin-mirroring worker to stop its eternal looping
            self.program_finished.set()
            # Join threads, storing inner exceptions, & set a timeout if
            # necessary. (Segregate WatcherErrors as they are "anticipated
            # errors" that want to show up at the end during creation of
            # Failure objects.)
            watcher_errors = []
            thread_exceptions = []
            for target, thread in self.threads.items():
                thread.join(self._thread_join_timeout(target))
                exception = thread.exception()
                if exception is not None:
                    real = exception.value
                    if isinstance(real, WatcherError):
                        watcher_errors.append(real)
                    else:
                        thread_exceptions.append(exception)
        # If any exceptions appeared inside the threads, raise them now as an
        # aggregate exception object.
        # NOTE: this is kept outside the 'finally' so that main-thread
        # exceptions are raised before worker-thread exceptions; they're more
        # likely to be Big Serious Problems.
        if thread_exceptions:
>           raise ThreadException(thread_exceptions)
E           invoke.exceptions.ThreadException: 
E           Saw 1 exceptions within threads (OSError):
E           
E           
E           Thread args: {'kwargs': {'echo': None,
E                       'input_': <_pytest.capture.DontReadFromInput object at 0x7f89209f1c30>,
E                       'output': <_io.TextIOWrapper name="<_io.FileIO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>},
E            'target': <bound method Runner.handle_stdin of <invoke.runners.Local object at 0x7f891fdff670>>}
E           
E           Traceback (most recent call last):
E           
E             File "/data/pydeps/sut/invoke/util.py", line 211, in run
E               super().run()
E           
E             File "/opt/conda/envs/test4py_env/lib/python3.10/threading.py", line 953, in run
E               self._target(*self._args, **self._kwargs)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 889, in handle_stdin
E               data = self.read_our_stdin(input_)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 834, in read_our_stdin
E               bytes_ = input_.read(bytes_to_read(input_))
E           
E             File "/data/pydeps/marta/_pytest/capture.py", line 208, in read
E               raise OSError(
E           
E           OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/sut/invoke/runners.py:521: ThreadException
----------------------------- Captured stderr call -----------------------------
bash: warning: setlocale: LC_ALL: cannot change locale (en_GB.UTF-8)
_______________________________ test_none_input ________________________________

    def test_none_input():
        with patch('semantic_release.dist.logger', MagicMock()):
            with pytest.raises(FileNotFoundError):
>               remove_dists(None)

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/dist.py:34: in remove_dists
    run(command)
/data/pydeps/sut/invoke/__init__.py:52: in run
    return Context().run(command, **kwargs)
/data/pydeps/sut/invoke/context.py:122: in run
    return self._run(runner, command, **kwargs)
/data/pydeps/sut/invoke/context.py:129: in _run
    return runner.run(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:403: in run
    return self._run_body(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:469: in _run_body
    return self.make_promise() if self._asynchronous else self._finish()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <invoke.runners.Local object at 0x7f891fdfcf10>

    def _finish(self) -> "Result":
        # Wait for subprocess to run, forwarding signals as we get them.
        try:
            while True:
                try:
                    self.wait()
                    break  # done waiting!
                # Don't locally stop on ^C, only forward it:
                # - if remote end really stops, we'll naturally stop after
                # - if remote end does not stop (eg REPL, editor) we don't want
                # to stop prematurely
                except KeyboardInterrupt as e:
                    self.send_interrupt(e)
                # TODO: honor other signals sent to our own process and
                # transmit them to the subprocess before handling 'normally'.
        # Make sure we tie off our worker threads, even if something exploded.
        # Any exceptions that raised during self.wait() above will appear after
        # this block.
        finally:
            # Inform stdin-mirroring worker to stop its eternal looping
            self.program_finished.set()
            # Join threads, storing inner exceptions, & set a timeout if
            # necessary. (Segregate WatcherErrors as they are "anticipated
            # errors" that want to show up at the end during creation of
            # Failure objects.)
            watcher_errors = []
            thread_exceptions = []
            for target, thread in self.threads.items():
                thread.join(self._thread_join_timeout(target))
                exception = thread.exception()
                if exception is not None:
                    real = exception.value
                    if isinstance(real, WatcherError):
                        watcher_errors.append(real)
                    else:
                        thread_exceptions.append(exception)
        # If any exceptions appeared inside the threads, raise them now as an
        # aggregate exception object.
        # NOTE: this is kept outside the 'finally' so that main-thread
        # exceptions are raised before worker-thread exceptions; they're more
        # likely to be Big Serious Problems.
        if thread_exceptions:
>           raise ThreadException(thread_exceptions)
E           invoke.exceptions.ThreadException: 
E           Saw 1 exceptions within threads (OSError):
E           
E           
E           Thread args: {'kwargs': {'echo': None,
E                       'input_': <_pytest.capture.DontReadFromInput object at 0x7f89209f1c30>,
E                       'output': <_io.TextIOWrapper name="<_io.FileIO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>},
E            'target': <bound method Runner.handle_stdin of <invoke.runners.Local object at 0x7f891fdfcf10>>}
E           
E           Traceback (most recent call last):
E           
E             File "/data/pydeps/sut/invoke/util.py", line 211, in run
E               super().run()
E           
E             File "/opt/conda/envs/test4py_env/lib/python3.10/threading.py", line 953, in run
E               self._target(*self._args, **self._kwargs)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 889, in handle_stdin
E               data = self.read_our_stdin(input_)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 834, in read_our_stdin
E               bytes_ = input_.read(bytes_to_read(input_))
E           
E             File "/data/pydeps/marta/_pytest/capture.py", line 208, in read
E               raise OSError(
E           
E           OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/sut/invoke/runners.py:521: ThreadException
----------------------------- Captured stderr call -----------------------------
bash: warning: setlocale: LC_ALL: cannot change locale (en_GB.UTF-8)
______________________________ test_invalid_path _______________________________

    def test_invalid_path():
        with patch('semantic_release.dist.logger', MagicMock()), pytest.raises(FileNotFoundError):
>           remove_dists('/nonexistent/directory')

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/dist.py:34: in remove_dists
    run(command)
/data/pydeps/sut/invoke/__init__.py:52: in run
    return Context().run(command, **kwargs)
/data/pydeps/sut/invoke/context.py:122: in run
    return self._run(runner, command, **kwargs)
/data/pydeps/sut/invoke/context.py:129: in _run
    return runner.run(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:403: in run
    return self._run_body(command, **kwargs)
/data/pydeps/sut/invoke/runners.py:469: in _run_body
    return self.make_promise() if self._asynchronous else self._finish()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <invoke.runners.Local object at 0x7f891e51d5d0>

    def _finish(self) -> "Result":
        # Wait for subprocess to run, forwarding signals as we get them.
        try:
            while True:
                try:
                    self.wait()
                    break  # done waiting!
                # Don't locally stop on ^C, only forward it:
                # - if remote end really stops, we'll naturally stop after
                # - if remote end does not stop (eg REPL, editor) we don't want
                # to stop prematurely
                except KeyboardInterrupt as e:
                    self.send_interrupt(e)
                # TODO: honor other signals sent to our own process and
                # transmit them to the subprocess before handling 'normally'.
        # Make sure we tie off our worker threads, even if something exploded.
        # Any exceptions that raised during self.wait() above will appear after
        # this block.
        finally:
            # Inform stdin-mirroring worker to stop its eternal looping
            self.program_finished.set()
            # Join threads, storing inner exceptions, & set a timeout if
            # necessary. (Segregate WatcherErrors as they are "anticipated
            # errors" that want to show up at the end during creation of
            # Failure objects.)
            watcher_errors = []
            thread_exceptions = []
            for target, thread in self.threads.items():
                thread.join(self._thread_join_timeout(target))
                exception = thread.exception()
                if exception is not None:
                    real = exception.value
                    if isinstance(real, WatcherError):
                        watcher_errors.append(real)
                    else:
                        thread_exceptions.append(exception)
        # If any exceptions appeared inside the threads, raise them now as an
        # aggregate exception object.
        # NOTE: this is kept outside the 'finally' so that main-thread
        # exceptions are raised before worker-thread exceptions; they're more
        # likely to be Big Serious Problems.
        if thread_exceptions:
>           raise ThreadException(thread_exceptions)
E           invoke.exceptions.ThreadException: 
E           Saw 1 exceptions within threads (OSError):
E           
E           
E           Thread args: {'kwargs': {'echo': None,
E                       'input_': <_pytest.capture.DontReadFromInput object at 0x7f89209f1c30>,
E                       'output': <_io.TextIOWrapper name="<_io.FileIO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>},
E            'target': <bound method Runner.handle_stdin of <invoke.runners.Local object at 0x7f891e51d5d0>>}
E           
E           Traceback (most recent call last):
E           
E             File "/data/pydeps/sut/invoke/util.py", line 211, in run
E               super().run()
E           
E             File "/opt/conda/envs/test4py_env/lib/python3.10/threading.py", line 953, in run
E               self._target(*self._args, **self._kwargs)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 889, in handle_stdin
E               data = self.read_our_stdin(input_)
E           
E             File "/data/pydeps/sut/invoke/runners.py", line 834, in read_our_stdin
E               bytes_ = input_.read(bytes_to_read(input_))
E           
E             File "/data/pydeps/marta/_pytest/capture.py", line 208, in read
E               raise OSError(
E           
E           OSError: pytest: reading from stdin while output is captured!  Consider using `-s`.

/data/pydeps/sut/invoke/runners.py:521: ThreadException
----------------------------- Captured stderr call -----------------------------
bash: warning: setlocale: LC_ALL: cannot change locale (en_GB.UTF-8)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py::test_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_dist_remove_dists_0.py::test_invalid_path
============================== 3 failed in 0.29s ===============================
"""