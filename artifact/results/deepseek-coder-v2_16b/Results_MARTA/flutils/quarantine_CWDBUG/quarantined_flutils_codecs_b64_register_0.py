
import pytest
import codecs
from flutils.codecs.b64 import register, _get_codec_info

def test_register():
    """Test that the 'b64' codec is registered correctly."""
    # Ensure the codec is not already registered
    with pytest.raises(LookupError):
        codecs.getdecoder('b64')
    
    # Call the register function
    register()
    
    # Check if the codec is now registered
    decoder = codecs.getdecoder('b64')
    assert callable(decoder)

def test_get_codec_info():
    """Test that _get_codec_info returns valid codec information."""
    info = _get_codec_info()
    
    # Check if the returned object has the necessary attributes
    assert hasattr(info, 'name') and info.name == 'b64'
    assert callable(info.encode)
    assert callable(info.decode)

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