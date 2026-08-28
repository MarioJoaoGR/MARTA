
import pytest
from flutils.decorators import cached_property

# Test 1: Basic Usage of cached_property
def test_cached_property_basic():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    # Subsequent access should not recompute the value
    assert obj.y == 6

# Test 2: Resetting Cache by Deleting Attribute
def test_cached_property_reset():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    # Resetting the cache by deleting the attribute
    del obj.__dict__['y']
    assert obj.y == 6  # Recomputed and cached again

# Test 3: Handling Deleted Attribute in __get__ method
def test_cached_property_deleted_attribute():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    # Deleting the attribute directly in the instance dictionary
    del obj.__dict__['y']
    with pytest.raises(AttributeError):
        obj.y  # Should raise AttributeError because the property should be reset

# Test 4: Handling Coroutine Functions
@pytest.mark.asyncio
async def test_cached_property_coroutine():
    class MyClass:
        async def _compute_z(self):
            return 7

        @cached_property
        def z(self):
            import asyncio
            return asyncio.run(self._compute_z())

    obj = MyClass()
    assert obj.z == 7
    # Subsequent access should not recompute the value
    assert obj.z == 7

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