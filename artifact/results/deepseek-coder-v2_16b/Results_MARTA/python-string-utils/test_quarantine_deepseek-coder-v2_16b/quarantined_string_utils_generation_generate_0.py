
import pytest
from string_utils.generation import generate, roman_encode

# Test to ensure that the generate function can produce a sequence of Roman numerals starting from 1 and incrementing by 1 until reaching 10
def test_generate_sequence():
    roman_gen = generate()
    expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    
    generated_values = []
    for _ in range(10):  # Generate the first 10 Roman numerals starting from start and incrementing by step
        generated_values.append(next(roman_gen))
    
    assert generated_values == expected_output

# Test to ensure that the generate function can produce a sequence of Roman numerals starting from 5 and incrementing by 2 until reaching 15
def test_generate_sequence_with_step():
    roman_gen = generate(start=5, step=2, stop=15)
    expected_output = ['V', 'VII', 'IX', 'XI', 'XIII', 'XV']
    
    generated_values = []
    for _ in range(6):  # Generate the first 6 Roman numerals starting from start and incrementing by step
        generated_values.append(next(roman_gen))
    
    assert generated_values == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_________ ERROR collecting test_string_utils_generation_generate_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_generate_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_generate_0.py:3: in <module>
    from string_utils.generation import generate, roman_encode
E   ImportError: cannot import name 'generate' from 'string_utils.generation' (/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/generation.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_generation_generate_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.14s ===============================
"""