
import pytest
from string_utils.generation import generate

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test when start is not an integer
        list(generate("start", 10, 1))
        
    with pytest.raises(TypeError):
        # Test when stop is not an integer
        list(generate(1, "stop", 1))
        
    with pytest.raises(TypeError):
        # Test when step is not an integer
        list(generate(1, 10, "step"))
        
    with pytest.raises(ValueError):
        # Test when start is greater than stop
        list(generate(10, 1, 1))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_generate_1_test_invalid_inputs
python-string-utils/Test4DT_tests/test_string_utils_generation_generate_1_test_invalid_inputs.py:3:0: E0611: No name 'generate' in module 'string_utils.generation' (no-name-in-module)


"""