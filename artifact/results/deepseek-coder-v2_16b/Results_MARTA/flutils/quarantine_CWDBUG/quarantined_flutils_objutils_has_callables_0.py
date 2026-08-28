
import pytest
from flutils.objutils import has_callables

# Test 1: Basic Usage - Check if an object has multiple callable attributes
class TestClass:
    def method(self):
        pass

    @staticmethod
    def static_method():
        pass

def test_has_callables_basic():
    assert has_callables(TestClass(), 'method', 'static_method') == True

# Test 2: Object with No Callable Attributes
class NoCallable:
    def __init__(self):
        self.attr1 = "value"
        self.attr2 = 42

def test_has_callables_no_callable():
    assert has_callables(NoCallable(), 'attr1', 'attr2') == False

# Test 3: Object with One Non-Callable Attribute
class MixedAttributes:
    def method(self):
        pass

def test_has_callables_one_non_callable():
    assert has_callables(MixedAttributes(), 'method', 'non_existent_attr') == False

# Test 4: Using with Built-in Types
def test_has_callables_builtin_types():
    # This will depend on the implementation of dict in Python, but typically it should return True for get and keys if they are callable.
    assert has_callables(dict(), 'get', 'keys') == True

# Test 5: Edge Case: Empty Object and Attributes
class EmptyClass:
    pass

def test_has_callables_empty_object():
    assert has_callables(EmptyClass(), 'non_existent_attr') == False

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