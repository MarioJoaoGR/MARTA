
import pytest
from httpie.config import get_default_config_dir
from pathlib import Path
import os

# Constants for testing environment variables
ENV_HTTPIE_CONFIG_DIR = 'HTTPIE_CONFIG_DIR'
DEFAULT_RELATIVE_LEGACY_CONFIG_DIR = '.httpie'
DEFAULT_WINDOWS_CONFIG_DIR = Path('C:\\Users\\Default')
DEFAULT_RELATIVE_XDG_CONFIG_HOME = '.config'
DEFAULT_CONFIG_DIRNAME = 'httpie'
ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'

# Mocking the os.environ for testing
@pytest.fixture(autouse=True)
def mock_os_environ(monkeypatch):
    monkeypatch.setenv(ENV_HTTPIE_CONFIG_DIR, '/custom/config')
    monkeypatch.delenv('XDG_CONFIG_HOME', raising=False)
    monkeypatch.delenv('HTTPIE_CONFIG_DIR', raising=False)

def test_get_default_config_dir_explicitly_set():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/config'
    config_dir = get_default_config_dir()
    assert str(config_dir) == '/custom/config', f"Expected /custom/config, but got {config_dir}"

def test_get_default_config_dir_windows():
    os.name = 'nt'  # Mocking the os.name to be Windows
    config_dir = get_default_config_dir()
    assert str(config_dir) == str(DEFAULT_WINDOWS_CONFIG_DIR), f"Expected {DEFAULT_WINDOWS_CONFIG_DIR}, but got {config_dir}"

def test_get_default_config_dir_legacy():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    config_dir = get_default_config_dir()
    home_dir = Path.home()
    expected_legacy_path = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    assert str(config_dir) == str(expected_legacy_path), f"Expected {expected_legacy_path}, but got {config_dir}"

def test_get_default_config_dir_xdg():
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/xdg'
    config_dir = get_default_config_dir()
    home_dir = Path.home()
    expected_xdg_path = home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    assert str(config_dir) == str(expected_xdg_path), f"Expected {expected_xdg_path}, but got {config_dir}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_1.py . [ 25%]

INTERNALERROR> Traceback (most recent call last):
INTERNALERROR>   File "/data/pydeps/marta/_pytest/main.py", line 283, in wrap_session
INTERNALERROR>     session.exitstatus = doit(config, session) or 0
INTERNALERROR>   File "/data/pydeps/marta/_pytest/main.py", line 337, in _main
INTERNALERROR>     config.hook.pytest_runtestloop(session=session)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/logging.py", line 805, in pytest_runtestloop
INTERNALERROR>     return (yield)  # Run all the tests.
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/terminal.py", line 673, in pytest_runtestloop
INTERNALERROR>     result = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/main.py", line 362, in pytest_runtestloop
INTERNALERROR>     item.config.hook.pytest_runtest_protocol(item=item, nextitem=nextitem)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/warnings.py", line 112, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/assertion/__init__.py", line 176, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 53, in run_old_style_hookwrapper
INTERNALERROR>     return result.get_result()
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_result.py", line 103, in get_result
INTERNALERROR>     raise exc.with_traceback(tb)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 38, in run_old_style_hookwrapper
INTERNALERROR>     res = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/unittest.py", line 429, in pytest_runtest_protocol
INTERNALERROR>     res = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/faulthandler.py", line 87, in pytest_runtest_protocol
INTERNALERROR>     return (yield)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/runner.py", line 113, in pytest_runtest_protocol
INTERNALERROR>     runtestprotocol(item, nextitem=nextitem)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/runner.py", line 132, in runtestprotocol
INTERNALERROR>     reports.append(call_and_report(item, "call", log))
INTERNALERROR>   File "/data/pydeps/marta/_pytest/runner.py", line 244, in call_and_report
INTERNALERROR>     report: TestReport = ihook.pytest_runtest_makereport(item=item, call=call)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_hooks.py", line 512, in __call__
INTERNALERROR>     return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_manager.py", line 120, in _hookexec
INTERNALERROR>     return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 167, in _multicall
INTERNALERROR>     raise exception
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/tmpdir.py", line 318, in pytest_runtest_makereport
INTERNALERROR>     rep = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 43, in run_old_style_hookwrapper
INTERNALERROR>     teardown.send(result)
INTERNALERROR>   File "/data/pydeps/marta/pytest_jsonreport/plugin.py", line 83, in pytest_runtest_makereport
INTERNALERROR>     report = (yield).get_result()
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_result.py", line 103, in get_result
INTERNALERROR>     raise exc.with_traceback(tb)
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 38, in run_old_style_hookwrapper
INTERNALERROR>     res = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
INTERNALERROR>     teardown.throw(exception)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/skipping.py", line 269, in pytest_runtest_makereport
INTERNALERROR>     rep = yield
INTERNALERROR>   File "/data/pydeps/marta/pluggy/_callers.py", line 121, in _multicall
INTERNALERROR>     res = hook_impl.function(*args)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/runner.py", line 368, in pytest_runtest_makereport
INTERNALERROR>     return TestReport.from_item_and_call(item, call)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/reports.py", line 376, in from_item_and_call
INTERNALERROR>     longrepr = item.repr_failure(excinfo)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/python.py", line 1669, in repr_failure
INTERNALERROR>     return self._repr_failure_py(excinfo, style=style)
INTERNALERROR>   File "/data/pydeps/marta/_pytest/nodes.py", line 452, in _repr_failure_py
INTERNALERROR>     abspath = Path(os.getcwd()) != self.config.invocation_params.dir
INTERNALERROR>   File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 962, in __new__
INTERNALERROR>     raise NotImplementedError("cannot instantiate %r on your system"
INTERNALERROR> NotImplementedError: cannot instantiate 'WindowsPath' on your system

Traceback (most recent call last):
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/pydeps/marta/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 175, in main
    ret: ExitCode | int = config.hook.pytest_cmdline_main(config=config)
  File "/data/pydeps/marta/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/data/pydeps/marta/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/data/pydeps/marta/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/data/pydeps/marta/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/data/pydeps/marta/_pytest/main.py", line 330, in pytest_cmdline_main
    return wrap_session(config, _main)
  File "/data/pydeps/marta/_pytest/main.py", line 318, in wrap_session
    config.hook.pytest_sessionfinish(
  File "/data/pydeps/marta/pluggy/_hooks.py", line 512, in __call__
    return self._hookexec(self.name, self._hookimpls.copy(), kwargs, firstresult)
  File "/data/pydeps/marta/pluggy/_manager.py", line 120, in _hookexec
    return self._inner_hookexec(hook_name, methods, kwargs, firstresult)
  File "/data/pydeps/marta/pluggy/_callers.py", line 167, in _multicall
    raise exception
  File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
  File "/data/pydeps/marta/_pytest/logging.py", line 870, in pytest_sessionfinish
    return (yield)
  File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
  File "/data/pydeps/marta/_pytest/terminal.py", line 893, in pytest_sessionfinish
    result = yield
  File "/data/pydeps/marta/pluggy/_callers.py", line 139, in _multicall
    teardown.throw(exception)
  File "/data/pydeps/marta/_pytest/warnings.py", line 141, in pytest_sessionfinish
    return (yield)
  File "/data/pydeps/marta/pluggy/_callers.py", line 121, in _multicall
    res = hook_impl.function(*args)
  File "/data/pydeps/marta/_pytest/cacheprovider.py", line 477, in pytest_sessionfinish
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))
  File "/data/pydeps/marta/_pytest/cacheprovider.py", line 182, in set
    path = self._getvaluepath(key)
  File "/data/pydeps/marta/_pytest/cacheprovider.py", line 151, in _getvaluepath
    return self._cachedir.joinpath(self._CACHE_PREFIX_VALUES, Path(key))
  File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 962, in __new__
    raise NotImplementedError("cannot instantiate %r on your system"
NotImplementedError: cannot instantiate 'WindowsPath' on your system
"""