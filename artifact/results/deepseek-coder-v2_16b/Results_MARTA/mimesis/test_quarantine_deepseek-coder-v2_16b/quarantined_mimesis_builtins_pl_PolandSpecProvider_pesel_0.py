
import pytest
from mimesis import Person, Datetime
from mimesis.enums import Gender
from mimesis.providers.base import Seed
from mimesis.providers.poland import PolandSpecProvider

def test_invalid_pesel_with_future_birth_date():
    provider = PolandSpecProvider()
    with pytest.raises(ValueError):
        provider.pesel(birth_date=Datetime().datetime(2050, 7, 26).date(), gender=Gender.MALE)

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
___ ERROR collecting test_mimesis_builtins_pl_PolandSpecProvider_pesel_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pl_PolandSpecProvider_pesel_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pl_PolandSpecProvider_pesel_0.py:6: in <module>
    from mimesis.providers.poland import PolandSpecProvider
E   ModuleNotFoundError: No module named 'mimesis.providers.poland'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_pl_PolandSpecProvider_pesel_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.29s ===============================
"""