
import pytest
from pathlib import Path
from flutils.pathutils import chmod
from unittest.mock import patch, MagicMock

def test_chmod_single_file():
    with patch('flutils.pathutils.normalize_path', return_value=MagicMock(name='Path', is_dir=lambda: False)):
        chmod('~/tmp/flutils.tests.osutils.txt', mode_file=0o660)
        assert Path('~/tmp/flutils.tests.osutils.txt').chmod.called_with(0o660)

def test_chmod_recursive_mode_change():
    with patch('flutils.pathutils.normalize_path', return_value=MagicMock(name='Path', is_dir=lambda: False)):
        chmod('~/tmp/**', mode_file=0o644, mode_dir=0o755)
        assert Path().glob.called_with('~/tmp/**')
        for sub_path in Path().glob('~/tmp/**'):
            if sub_path.is_dir():
                assert sub_path.chmod.called_with(0o755)
            elif sub_path.is_file():
                assert sub_path.chmod.called_with(0o644)

def test_chmod_immediate_contents():
    with patch('flutils.pathutils.normalize_path', return_value=MagicMock(name='Path', is_dir=lambda: False)):
        chmod('~/tmp/*')
        assert Path().glob.called_with('~/tmp/*')
        for sub_path in Path().glob('~/tmp/*'):
            if sub_path.is_dir():
                assert sub_path.chmod.called_with(0o755)
            elif sub_path.is_file():
                assert sub_path.chmod.called_with(0o644)

def test_chmod_include_parent():
    with patch('flutils.pathutils.normalize_path', return_value=MagicMock(name='Path', is_dir=lambda: False)):
        chmod('~/tmp/**', mode_file=0o644, mode_dir=0o755, include_parent=True)
        assert Path().glob.called_with('~/tmp/**')
        for sub_path in Path().glob('~/tmp/**'):
            if sub_path.is_dir():
                assert sub_path.chmod.called_with(0o755)
            elif sub_path.is_file():
                assert sub_path.chmod.called_with(0o644)
        assert Path('~/tmp').chmod.called_with(0o755)

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