
import pytest
from flutils.moduleutils import _CherryPickFinder
import sys

# Test 1: Ensure that _CherryPickFinder is a singleton and added to sys.meta_path correctly
def test_cherrypickfinder_singleton():
    finder1 = _CherryPickFinder()
    finder2 = _CherryPickFinder()
    assert finder1 is finder2, "Two instances of _CherryPickFinder should be the same object."
    
    # Check if the finder is in sys.meta_path
    assert isinstance(_CherryPickFinder(), _CherryPickFinder), "_CherryPickFinder should be in sys.meta_path"
    assert len(sys.meta_path) == 1, "There should only be one instance of _CherryPickFinder in sys.meta_path."

# Test 2: Ensure that the load method correctly adds the finder to sys.meta_path if it's not already present
def test_cherrypickfinder_load():
    # Remove any existing instances from sys.meta_path for a clean state
    while _CherryPickFinder() in sys.meta_path:
        sys.meta_path.remove(_CherryPickFinder())
    
    assert len(sys.meta_path) == 0, "Initially, there should be no instances of _CherryPickFinder in sys.meta_path."
    
    # Load the finder and check if it's added to sys.meta_path
    _CherryPickFinder().load()
    assert len(sys.meta_path) == 1, "_CherryPickFinder should be added to sys.meta_path after loading."
    
    # Try reloading and ensure the count doesn't change
    _CherryPickFinder().load()
    assert len(sys.meta_path) == 1, "Reloading should not add a new instance of _CherryPickFinder to sys.meta_path."

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