
import pytest
from flutils.packages import _build_version_bump_type, _BUMP_VERSION_MAJOR, _BUMP_VERSION_MINOR, _BUMP_VERSION_PATCH, _BUMP_VERSION_MINOR_ALPHA, _BUMP_VERSION_MINOR_BETA, _BUMP_VERSION_PATCH_ALPHA, _BUMP_VERSION_PATCH_BETA
from typing import Union, cast

def test_major_bump_no_prerelease():
    assert _build_version_bump_type(0, None) == _BUMP_VERSION_MAJOR

def test_minor_bump_with_alpha_prerelease():
    assert _build_version_bump_type(1, 'alpha') == _BUMP_VERSION_MINOR_ALPHA

def test_patch_bump_with_beta_prerelease():
    assert _build_version_bump_type(2, 'beta') == _BUMP_VERSION_PATCH_BETA

def test_invalid_prerelease_value():
    with pytest.raises(ValueError) as excinfo:
        _build_version_bump_type(1, 'gamma')
    assert str(excinfo.value) == "The given value for 'pre_release', 'gamma', can only be one of: alpha, beta, a, b."

def test_major_bump_with_prerelease():
    with pytest.raises(ValueError) as excinfo:
        _build_version_bump_type(0, 'beta')
    assert str(excinfo.value) == "Only the 'minor' or 'patch' parts of the version number can get a prerelease bump."

def test_minor_bump_no_prerelease():
    assert _build_version_bump_type(1, None) == _BUMP_VERSION_MINOR

def test_patch_bump_no_prerelease():
    assert _build_version_bump_type(2, None) == _BUMP_VERSION_PATCH

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