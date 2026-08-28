
import pytest
from flutils.packages import bump_version

def test_bump_version_basic():
    assert bump_version('1.2.3') == '1.2.4'

def test_bump_version_increase_minor():
    assert bump_version('1.2.3', position=1) == '1.3'

def test_bump_version_increase_major():
    assert bump_version('1.2.3', position=0) == '2.0'

def test_bump_version_add_alpha_prerelease():
    assert bump_version('1.2.3', pre_release='a') == '1.2.4a0'

def test_bump_version_increase_minor_with_alpha_prerelease():
    assert bump_version('1.2.3', position=1, pre_release='a') == '1.3a0'

def test_bump_version_increase_major_with_beta_prerelease():
    assert bump_version('1.2.4', position=0, pre_release='b') == '2.0b0'

def test_invalid_version():
    with pytest.raises(ValueError):
        bump_version('invalid-version')

def test_invalid_position():
    with pytest.raises(ValueError):
        bump_version('1.2.3', position=5)

def test_invalid_prerelease():
    with pytest.raises(ValueError):
        bump_version('1.2.3', pre_release='invalid')

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