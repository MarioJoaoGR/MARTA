
import pytest
import asyncio
from flutils.decorators import wrapper

@pytest.mark.asyncio
async def test_wrapper():
    # Create a mock function and object for testing
    class MockClass:
        def __init__(self):
            self.func = lambda x: print(x)  # Example function
    
    obj = MockClass()
    
    # Call the wrapper method
    future_obj = wrapper(obj)
    
    # Ensure the future is created and stored in obj.__dict__
    assert isinstance(future_obj, asyncio.Future)
    assert future_obj == obj.__dict__[wrapper.__name__]
    
    # Optionally, you can add more assertions to check the behavior of func execution within the future
    await asyncio.sleep(0)  # Allow time for the future to complete (if it's an immediate print this might not be necessary)

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