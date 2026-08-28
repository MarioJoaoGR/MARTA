
import pytest
from distutils.version import StrictVersion
from flutils.packages import _build_version_info, _VersionInfo, _each_version_part

def test_basic_usage():
    version = "1.2.3"
    ver_info = _build_version_info(version)
    assert isinstance(ver_info, _VersionInfo)
    assert ver_info.version == (1, 2, 3)
    assert ver_info.prerelease is None

def test_with_pre_release():
    version = "1.2.3rc4"
    ver_info = _build_version_info(version)
    assert isinstance(ver_info, _VersionInfo)
    assert ver_info.version == (1, 2, 3)
    assert ver_info.prerelease == ('rc', 4)

def test_invalid_version():
    version = "invalid_version"
    with pytest.raises(ValueError):
        _build_version_info(version)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
Traceback (most recent call last):
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/pydeps/marta/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 156, in main
    config = _prepareconfig(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 332, in _prepareconfig
    config = get_config(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 293, in get_config
    dir=pathlib.Path.cwd(),
  File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 993, in cwd
    return cls(cls._accessor.getcwd())
FileNotFoundError: [Errno 2] No such file or directory
"""