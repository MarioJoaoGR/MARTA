
import pytest
from flutils.decorators import cached_property

class MyClass:
    def __init__(self):
        self.x = 5

    @cached_property
    def y(self):
        return self.x + 1

# Test that the property is computed once and then cached
def test_cached_property_is_computed_once():
    obj = MyClass()
    assert obj.y == 6
    # Accessing it again should not recompute
    assert obj.y == 6

# Test that deleting the attribute resets the property
def test_resetting_attribute_recomputes_property():
    obj = MyClass()
    assert obj.y == 6
    del obj.__dict__['y']
    # Accessing it after deletion should recompute
    assert obj.y == 7

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