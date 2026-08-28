
import pytest
from mimesis.builtins.pt_br import CNPJ

def test_get_verifying_digit_cnpj():
    cnpj = [3, 4, 1, 9, 2, 7, 0, 0, 0, 1, 8, 5]
    
    # Test with peso value 5
    result1 = CNPJ().get_verifying_digit_cnpj(cnpj, 5)
    assert result1 == 6
    
    # Test with peso value 6
    result2 = CNPJ().get_verifying_digit_cnpj(cnpj, 6)
    assert result2 == 7

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py:3: in <module>
    from mimesis.builtins.pt_br import CNPJ
E   ImportError: cannot import name 'CNPJ' from 'mimesis.builtins.pt_br' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/builtins/pt_br.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""