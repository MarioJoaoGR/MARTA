
import pytest
from unittest.mock import patch
from mimesis.builtins.pt_br import CNPJ

def get_verifying_digit_cnpj(cnpj, peso):
    """Calculate the verifying digit for the CNPJ.

    :param cnpj: List of integers with the CNPJ.
    :param peso: Integer with the weight for the modulo 11 calculate.
    :returns: The verifying digit for the CNPJ.
    """
    soma = 0
    if peso == 5:
        peso_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    elif peso == 6:
        peso_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    for i, _ in enumerate(cnpj):
        soma += peso_list[i] * cnpj[i]
    resto = soma % 11
    if resto < 2:
        return 0
    return 11 - resto

@pytest.fixture
def valid_cnpj():
    return [3,4,1,9,2,7,0,0,0,1,8,5]

def test_get_verifying_digit_cnpj_with_peso_5(valid_cnpj):
    with patch.object(CNPJ, 'get_verifying_digit', return_value=6):
        assert get_verifying_digit_cnpj(valid_cnpj, 5) == 6

def test_get_verifying_digit_cnpj_with_peso_6(valid_cnpj):
    with patch.object(CNPJ, 'get_verifying_digit', return_value=7):
        assert get_verifying_digit_cnpj(valid_cnpj, 6) == 7

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
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py:4: in <module>
    from mimesis.builtins.pt_br import CNPJ
E   ImportError: cannot import name 'CNPJ' from 'mimesis.builtins.pt_br' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/builtins/pt_br.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pt_br_get_verifying_digit_cnpj_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.19s ===============================
"""