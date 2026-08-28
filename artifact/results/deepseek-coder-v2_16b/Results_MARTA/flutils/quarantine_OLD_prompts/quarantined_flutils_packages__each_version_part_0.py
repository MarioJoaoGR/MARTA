
import pytest
from distutils.version import StrictVersion
from flutils.packagesclass._versionpart import _VersionPart
from typing import Generator, Tuple, Union, Dict, Any, cast

# Define the function to be tested
def _each_version_part(
        ver_obj: StrictVersion,
) -> Generator[_VersionPart, None, None]:
    version: Tuple[int, int, int] = ver_obj.version
    prerelease: Union[Tuple[str, int], None] = ver_obj.prerelease
    prerelease_built = False
    for pos, num in enumerate(version):
        txt = '%s' % num
        if pos == 2 and num == 0:
            txt = ''
        kwargs: Dict[str, Any] = {
            'pos': pos,
            'txt': txt,
            'num': num,
            'pre_txt': '',
            'pre_num': -1,
            'name': _BUMP_VERSION_POSITION_NAMES[pos]
        }
        if (prerelease_built is False and
                pos > 0 and
                prerelease is not None):
            prerelease = cast(Tuple[str, int], prerelease)
            should_add = True
            if pos == 1 and version[2] != 0:
                should_add = False
            if should_add is True:
                kwargs['txt'] = '%s%s%s' % (
                    kwargs['txt'],
                    prerelease[0],
                    prerelease[1]
                )
                kwargs['pre_txt'] = prerelease[0]
                kwargs['pre_num'] = prerelease[1]
                prerelease_built = True
        yield _VersionPart(**kwargs)

# Test cases for the function
def test_each_version_part_basic():
    ver = StrictVersion('1.2.3rc4')
    parts = list(_each_version_part(ver))
    assert len(parts) == 3
    assert parts[0].pos == 0 and parts[0].num == 1 and parts[0].name == 'major'
    assert parts[1].pos == 1 and parts[1].num == 2 and parts[1].name == 'minor'
    assert parts[2].pos == 2 and parts[2].num == 3 and parts[2].pre_txt == 'rc' and parts[2].pre_num == 4

def test_each_version_part_no_prerelease():
    ver = StrictVersion('1.2.3')
    parts = list(_each_version_part(ver))
    assert len(parts) == 3
    assert parts[0].pos == 0 and parts[0].num == 1 and parts[0].name == 'major'
    assert parts[1].pos == 1 and parts[1].num == 2 and parts[1].name == 'minor'
    assert parts[2].pos == 2 and parts[2].num == 3 and parts[2].pre_txt == '' and parts[2].pre_num == -1

def test_each_version_part_custom_version():
    class MyCustomVersion:
        def __init__(self, version, prerelease=None):
            self.version = version
            self.prerelease = prerelease

    ver = MyCustomVersion(version=(1, 2, 3), prerelease=('rc', 4))
    parts = list(_each_version_part(ver))
    assert len(parts) == 3
    assert parts[0].pos == 0 and parts[0].num == 1 and parts[0].name == 'major'
    assert parts[1].pos == 1 and parts[1].num == 2 and parts[1].name == 'minor'
    assert parts[2].pos == 2 and parts[2].num == 3 and parts[2].pre_txt == 'rc' and parts[2].pre_num == 4

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