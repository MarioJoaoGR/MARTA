
import pytest
from blib2to3.pgen2.tokenize import tokenize_any

def test_tokenize_any():
    # Test case 1: Basic usage of tokenize_any with multiple choices
    pattern = tokenize_any("apple", "banana", "cherry")
    assert pattern == "(apple|banana|cherry)*"

    # Test case 2: Usage with a single choice
    pattern = tokenize_any("a")
    assert pattern == "(a)*"

    # Test case 3: Usage with numbers from 1 to 5
    choices = [str(i) for i in range(1, 6)]
    pattern = tokenize_any(*choices)
    assert pattern == "(1|2|3|4|5)*"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_src_blib2to3_pgen2_tokenize_any_0.py __________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_any_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_any_0.py:3: in <module>
    from blib2to3.pgen2.tokenize import tokenize_any
E   ImportError: cannot import name 'tokenize_any' from 'blib2to3.pgen2.tokenize' (/opt/marta/baselines/codamosa/replication/test-apps/black/src/blib2to3/pgen2/tokenize.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/black/Test4DT_tests_deepseek-coder-v2_16b/test_src_blib2to3_pgen2_tokenize_any_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""