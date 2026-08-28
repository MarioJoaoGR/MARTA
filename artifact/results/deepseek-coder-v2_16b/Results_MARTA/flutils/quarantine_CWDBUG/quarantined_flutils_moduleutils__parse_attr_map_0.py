
import pytest
from flutils.moduleutils import _CherryPickMap, _parse_attr_map
from collections import defaultdict
from typing import Tuple

# Test 1: Valid attr_map with multiple rows
def test_valid_attr_map():
    attr_map = (('name', 'age'), ('first_name', 'birth_year'))
    parsed_result = _parse_attr_map(attr_map, "module.function")
    assert isinstance(parsed_result, _CherryPickMap)
    assert len(parsed_result.modules) == 2
    assert len(parsed_result.identifiers) == 4

# Test 2: Valid attr_map with a single row of strings
def test_valid_attr_map_single_row():
    attr_map = ('name', 'age', 'first_name', 'birth_year')
    parsed_result = _parse_attr_map(attr_map, "module.function")
    assert isinstance(parsed_result, _CherryPickMap)
    assert len(parsed_result.modules) == 4
    assert len(parsed_result.identifiers) == 2

# Test 3: Empty attr_map
def test_empty_attr_map():
    attr_map = ()
    parsed_result = _parse_attr_map(attr_map, "module.function")
    assert isinstance(parsed_result, _CherryPickMap)
    assert len(parsed_result.modules) == 0
    assert len(parsed_result.identifiers) == 0

# Test 4: Invalid attr_map type (should raise CherryPickError)
def test_invalid_attr_map_type():
    with pytest.raises(CherryPickError):
        _parse_attr_map("not a tuple", "module.function")

# Test 5: Duplicate attribute names in attr_map (should raise CherryPickError)
def test_duplicate_attribute_names():
    attr_map = (('name', 'age'), ('first_name', 'birth_year'), ('name', 'address'))
    with pytest.raises(CherryPickError):
        _parse_attr_map(attr_map, "module.function")

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