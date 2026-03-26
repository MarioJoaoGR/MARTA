
# Module: Test4DT_tests.test_isort__vendored_tomli__parser_suffixed_err_0
import pytest
from tomli._parser import suffixed_err, TOMLDecodeError

# Test Case 1: Basic Usage
def test_suffixed_err_basic():
    src = "def example_function():\n    print('Hello, world!')"
    pos = 20  # Position of the error in the source code (character index)
    msg = "Unexpected token found"
    
    with pytest.raises(TOMLDecodeError) as excinfo:
        raise suffixed_err(src, pos, msg)
    
    assert str(excinfo.value) == f"{msg} (at line 2, column 15)"

# Test Case 2: Error at Specific Position
def test_suffixed_err_specific_position():
    src = "key1 = 'value1'\nkey2 = 42"
    pos = 5  # Position of the error in the source code (character index)
    msg = "Invalid character found"
    
    with pytest.raises(TOMLDecodeError) as excinfo:
        raise suffixed_err(src, pos, msg)
    
    assert str(excinfo.value) == f"{msg} (at line 1, column 6)"

# Test Case 3: Empty Source Code
def test_suffixed_err_empty_source():
    src = ""
    pos = 0  # Position of the error in the source code (character index)
    msg = "Empty input"
    
    with pytest.raises(TOMLDecodeError) as excinfo:
        raise suffixed_err(src, pos, msg)
    
    assert str(excinfo.value) == f"{msg} (at line 1, column 1)"

# Test Case 4: Large Source Code
def test_suffixed_err_large_source():
    src = "a" * 1000  # A large string for demonstration purposes
    pos = 500  # Position of the error in the source code (character index)
    msg = "Error near this position"
    
    with pytest.raises(TOMLDecodeError) as excinfo:
        raise suffixed_err(src, pos, msg)
    
    assert str(excinfo.value) == f"{msg} (at line 501, column 501)"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort__vendored_tomli__parser_suffixed_err_0
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0.py:4:0: E0611: No name 'suffixed_err' in module 'tomli._parser' (no-name-in-module)
isort/Test4DT_tests/test_isort__vendored_tomli__parser_suffixed_err_0.py:4:0: E0611: No name 'TOMLDecodeError' in module 'tomli._parser' (no-name-in-module)


"""