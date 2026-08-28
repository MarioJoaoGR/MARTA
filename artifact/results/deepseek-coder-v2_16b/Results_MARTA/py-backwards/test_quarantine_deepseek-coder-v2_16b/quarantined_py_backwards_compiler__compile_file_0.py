
import pytest
from pathlib import Path
from py_backwards.utils.input_output import InputOutput
from py_backwards.targets import CompilationTarget
from py_backwards.exceptions import CompilationError

# Test scenario 1: Successful compilation of a Python file
def test_successful_compilation():
    # Arrange
    input_path = Path("test_input.py")
    output_path = Path("test_output.py")
    io_paths = InputOutput(input=input_path, output=output_path)
    compilation_target = CompilationTarget.PYTHON3
    
    # Create a dummy input file with some Python code
    with open(input_path, 'w') as f:
        f.write("print('Hello, World!')")
    
    expected_dependencies = []  # No dependencies for this simple example
    
    # Act & Assert
    try:
        result = _compile_file(io_paths, compilation_target)
        assert result == expected_dependencies
        
        # Check if the output file was created and contains the transformed code
        with open(output_path, 'r') as f:
            content = f.read()
        assert "print('Hello, World!')" in content
    finally:
        input_path.unlink()  # Clean up the test file
        output_path.unlink()  # Clean up the output file

# Test scenario 2: Compilation failure due to syntax error
def test_compilation_failure():
    # Arrange
    input_path = Path("test_input.py")
    output_path = Path("test_output.py")
    io_paths = InputOutput(input=input_path, output=output_path)
    compilation_target = CompilationTarget.PYTHON3
    
    # Create a dummy input file with a syntax error
    with open(input_path, 'w') as f:
        f.write("print('Hello, World!'")  # Missing closing parenthesis
    
    expected_dependencies = []  # No dependencies for this simple example
    
    # Act & Assert
    with pytest.raises(CompilationError):
        _compile_file(io_paths, compilation_target)
        
    # Check if the output file was not created due to the syntax error
    assert not output_path.exists()

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
________ ERROR collecting test_py_backwards_compiler__compile_file_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_compiler__compile_file_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_compiler__compile_file_0.py:4: in <module>
    from py_backwards.utils.input_output import InputOutput
E   ModuleNotFoundError: No module named 'py_backwards.utils.input_output'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_compiler__compile_file_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""