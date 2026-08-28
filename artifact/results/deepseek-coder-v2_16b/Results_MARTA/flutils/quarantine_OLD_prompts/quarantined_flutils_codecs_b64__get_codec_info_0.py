
import pytest
from unittest.mock import patch, MagicMock
import codecs

# Assuming the function _get_codec_info and the constant NAME are defined in a module named 'your_module'
# from your_module import _get_codec_info, NAME

NAME = "example_codec"  # Example predefined constant

def test_get_codec_info_found():
    with patch('your_module._get_codec_info', return_value=MagicMock()):
        result = your_module._get_codec_info(NAME)
        assert result is not None

def test_get_codec_info_not_found():
    with patch('your_module._get_codec_info', return_value=None):
        result = your_module._get_codec_info('unknown_codec')
        assert result is None

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