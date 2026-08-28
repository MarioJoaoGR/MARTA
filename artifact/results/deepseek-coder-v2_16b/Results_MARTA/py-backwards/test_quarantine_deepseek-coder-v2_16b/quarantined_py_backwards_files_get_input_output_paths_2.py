
import pytest
from pathlib import Path
from py_backwards import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists

# Test 1: Basic Call with Absolute Paths
def test_get_input_output_paths_basic():
    input_path = 'C:/data/input'
    output_path = 'D:/output/results.txt'
    root = None
    pairs = list(get_input_output_paths(input_path, output_path, root))
    assert len(pairs) == 1
    assert isinstance(pairs[0].input, Path)
    assert isinstance(pairs[0].output, Path)
    assert str(pairs[0].input) == 'C:/data/input'
    assert str(pairs[0].output) == 'D:/output/results.txt'

# Test 2: Using a Root Directory with Relative Input Path
def test_get_input_output_paths_with_root():
    input_path = 'data/input'
    output_path = 'D:/outputs/results.txt'
    root = 'C:/root'
    pairs = list(get_input_output_paths(input_path, output_path, root))
    assert len(pairs) == 1
    assert isinstance(pairs[0].input, Path)
    assert isinstance(pairs[0].output, Path)
    assert str(pairs[0].input) == 'C:/root/data/input'
    assert str(pairs[0].output) == 'D:/outputs/results.txt'

# Test 3: Handling Input as Directory and Output as File
def test_get_input_output_paths_directory_to_file():
    input_path = 'data/input'
    output_path = 'D:/outputs/results.txt'
    root = None
    pairs = list(get_input_output_paths(input_path, output_path, root))
    assert len(pairs) == 1
    assert isinstance(pairs[0].input, Path)
    assert isinstance(pairs[0].output, Path)
    assert str(pairs[0].input) == 'data/input'
    assert str(pairs[0].output) == 'D:/outputs/results.txt'

# Test 4: Handling Input as File and Output as Directory
def test_get_input_output_paths_file_to_directory():
    input_path = 'data/input.txt'
    output_path = 'D:/outputs/'
    root = None
    pairs = list(get_input_output_paths(input_path, output_path, root))
    assert len(pairs) == 1
    assert isinstance(pairs[0].input, Path)
    assert isinstance(pairs[0].output, Path)
    assert str(pairs[0].input) == 'data/input.txt'
    assert str(pairs[0].output) == 'D:/outputs/data/input.txt'

# Test 5: InvalidInputOutput Exception when Input Ends with '.py' but Output Does Not
def test_get_input_output_paths_invalid_input_output():
    input_path = 'source/code'
    output_path = 'dist'
    root = None
    with pytest.raises(InvalidInputOutput):
        list(get_input_output_paths(input_path, output_path, root))

# Test 6: InputDoesntExists Exception when Input Path Does Not Exist
def test_get_input_output_paths_input_doesnt_exist():
    input_path = 'non_existent/input'
    output_path = 'dist'
    root = None
    with pytest.raises(InputDoesntExists):
        list(get_input_output_paths(input_path, output_path, root))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_py_backwards_files_get_input_output_paths_2.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_files_get_input_output_paths_2.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_files_get_input_output_paths_2.py:4: in <module>
    from py_backwards import get_input_output_paths, InputOutput, InvalidInputOutput, InputDoesntExists
E   ImportError: cannot import name 'get_input_output_paths' from 'py_backwards' (/opt/marta/baselines/codamosa/replication/test-apps/py-backwards/py_backwards/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_files_get_input_output_paths_2.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.13s ===============================
"""