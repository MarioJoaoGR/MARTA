
import pytest
from flutils.codecs import register_codecs, raw_utf8_escape, b64
from unittest.mock import patch

def test_register_codecs():
    with patch('flutils.codecs.raw_utf8_escape.register') as mock_raw_utf8_escape_register:
        with patch('flutils.codecs.b64.register') as mock_b64_register:
            register_codecs()
            assert mock_raw_utf8_escape_register.called
            assert mock_b64_register.called

def test_encode_with_raw_utf8_escape():
    with patch('flutils.codecs.raw_utf8_escape.register'):
        register_codecs()
        encoded = 'test©'.encode('raw_utf8_escape')
        assert encoded == b'test\\xc2\\xa9'

def test_decode_with_raw_utf8_escape():
    with patch('flutils.codecs.raw_utf8_escape.register'):
        register_codecs()
        decoded = b'test\\xc2\\xa9'.decode('raw_utf8_escape')
        assert decoded == 'test©'

def test_encode_with_b64():
    with patch('flutils.codecs.b64.register'):
        register_codecs()
        encoded = 'dGVzdA=='.encode('b64')
        assert encoded == b'test'

def test_decode_with_b64():
    with patch('flutils.codecs.b64.register'):
        register_codecs()
        decoded = b'test'.decode('b64')
        assert decoded == 'dGVzdA=='

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