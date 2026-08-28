
import pytest
from pathlib import Path
import os
import json
import time
from unittest.mock import patch, MagicMock
from thefuck.entrypoints.not_configured import _is_second_run, const

@pytest.fixture(autouse=True)
def mock_tracker_path():
    with patch('thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path', return_value=MagicMock()):
        yield




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
___________________________ test_is_second_run_true ____________________________

mock_time = <MagicMock name='time' id='140643699803184'>
mock_getpid = <MagicMock name='getpid' id='140643699811008'>

    @patch('os.getpid', return_value=12345)
    @patch('time.time', return_value=100.0)
    def test_is_second_run_true(mock_time, mock_getpid):
        tracker_path = Path('/tmp/test_marker_file/.not_configured_usage_tracker')
>       tracker_path.touch()

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:1168: in touch
    self._accessor.touch(self, mode, exist_ok)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pathlib._NormalAccessor object at 0x7fea2b763490>
path = PosixPath('/tmp/test_marker_file/.not_configured_usage_tracker')
mode = 438, exist_ok = True

    def touch(self, path, mode=0o666, exist_ok=True):
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                os.utime(path, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
>       fd = os.open(path, flags, mode)
E       FileNotFoundError: [Errno 2] No such file or directory: '/tmp/test_marker_file/.not_configured_usage_tracker'

/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:331: FileNotFoundError
______________________ test_is_second_run_false_wrong_pid ______________________

mock_time = <MagicMock name='time' id='140643700449648'>
mock_getpid = <MagicMock name='getpid' id='140643700441488'>

    @patch('os.getpid', return_value=12345)
    @patch('time.time', return_value=100.0)
    def test_is_second_run_false_wrong_pid(mock_time, mock_getpid):
        tracker_path = Path('/tmp/test_marker_file/.not_configured_usage_tracker')
>       tracker_path.touch()

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:1168: in touch
    self._accessor.touch(self, mode, exist_ok)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pathlib._NormalAccessor object at 0x7fea2b763490>
path = PosixPath('/tmp/test_marker_file/.not_configured_usage_tracker')
mode = 438, exist_ok = True

    def touch(self, path, mode=0o666, exist_ok=True):
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                os.utime(path, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
>       fd = os.open(path, flags, mode)
E       FileNotFoundError: [Errno 2] No such file or directory: '/tmp/test_marker_file/.not_configured_usage_tracker'

/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:331: FileNotFoundError
___________________ test_is_second_run_false_wrong_timestamp ___________________

mock_time = <MagicMock name='time' id='140643698502832'>
mock_getpid = <MagicMock name='getpid' id='140643698496928'>

    @patch('os.getpid', return_value=12345)
    @patch('time.time', return_value=100.0)
    def test_is_second_run_false_wrong_timestamp(mock_time, mock_getpid):
        tracker_path = Path('/tmp/test_marker_file/.not_configured_usage_tracker')
>       tracker_path.touch()

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:1168: in touch
    self._accessor.touch(self, mode, exist_ok)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pathlib._NormalAccessor object at 0x7fea2b763490>
path = PosixPath('/tmp/test_marker_file/.not_configured_usage_tracker')
mode = 438, exist_ok = True

    def touch(self, path, mode=0o666, exist_ok=True):
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                os.utime(path, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
>       fd = os.open(path, flags, mode)
E       FileNotFoundError: [Errno 2] No such file or directory: '/tmp/test_marker_file/.not_configured_usage_tracker'

/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py:331: FileNotFoundError
___________________ test_is_second_run_false_not_configured ____________________

mock_time = <MagicMock name='time' id='140643700134656'>
mock_getpid = <MagicMock name='getpid' id='140643700141376'>

    @patch('os.getpid', return_value=12345)
    @patch('time.time', return_value=100.0)
    def test_is_second_run_false_not_configured(mock_time, mock_getpid):
        tracker_path = Path('/tmp/test_marker_file/.not_configured_usage_tracker')
    
>       assert _is_second_run() == False

/opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py:50: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/entrypoints/not_configured.py:61: in _is_second_run
    current_pid = _get_shell_pid()
/opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/entrypoints/not_configured.py:21: in _get_shell_pid
    proc = Process(os.getpid())
/data/pydeps/marta/psutil/__init__.py:314: in __init__
    self._init(pid)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = psutil.Process(pid=12345, status='terminated'), pid = 12345
_ignore_nsp = False

    def _init(self, pid, _ignore_nsp=False):
        if pid is None:
            pid = os.getpid()
        else:
            if pid < 0:
                msg = f"pid must be a positive integer (got {pid})"
                raise ValueError(msg)
            try:
                _psplatform.cext.check_pid_range(pid)
            except OverflowError as err:
                msg = "process PID out of range"
                raise NoSuchProcess(pid, msg=msg) from err
    
        self._pid = pid
        self._name = None
        self._exe = None
        self._create_time = None
        self._gone = False
        self._pid_reused = False
        self._hash = None
        self._lock = threading.RLock()
        # used for caching on Windows only (on POSIX ppid may change)
        self._ppid = None
        # platform-specific modules define an _psplatform.Process
        # implementation class
        self._proc = _psplatform.Process(pid)
        self._last_sys_cpu_times = None
        self._last_proc_cpu_times = None
        self._exitcode = _SENTINEL
        self._ident = (self.pid, None)
        try:
            self._ident = self._get_ident()
        except AccessDenied:
            # This should happen on Windows only, since we use the fast
            # create time method. AFAIK, on all other platforms we are
            # able to get create time for all PIDs.
            pass
        except ZombieProcess:
            # Zombies can still be queried by this class (although
            # not always) and pids() return them so just go on.
            pass
        except NoSuchProcess:
            if not _ignore_nsp:
                msg = "process PID not found"
>               raise NoSuchProcess(pid, msg=msg) from None
E               psutil.NoSuchProcess: process PID not found (pid=12345)

/data/pydeps/marta/psutil/__init__.py:360: NoSuchProcess
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1
  /opt/marta/baselines/codamosa/replication/test-apps/thefuck/thefuck/conf.py:1: DeprecationWarning: the imp module is deprecated in favour of importlib and slated for removal in Python 3.12; see the module's documentation for alternative uses
    from imp import load_source

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py::test_is_second_run_true
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py::test_is_second_run_false_wrong_pid
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py::test_is_second_run_false_wrong_timestamp
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thefuck/Test4DT_tests_deepseek-coder-v2_16b/test_thefuck_entrypoints_not_configured__is_second_run_0.py::test_is_second_run_false_not_configured
========================= 4 failed, 1 warning in 0.26s =========================
"""