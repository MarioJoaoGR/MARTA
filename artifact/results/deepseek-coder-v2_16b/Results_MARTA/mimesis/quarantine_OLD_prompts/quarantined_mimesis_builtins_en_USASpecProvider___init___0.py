
import pytest
from unittest.mock import patch
from mimesis.providers import USASpecProvider
from mimesis.seed import Seed

def test_USASpecProvider_without_seed():
    with patch('mimesis.providers.BaseDataProvider.__init__', return_value=None):
        provider = USASpecProvider()
        assert provider.locale == 'en'
        assert isinstance(provider, USASpecProvider)

def test_USASpecProvider_with_seed():
    with patch('mimesis.providers.BaseDataProvider.__init__', return_value=None):
        seed = Seed()
        provider = USASpecProvider(seed=seed)
        assert provider.locale == 'en'
        assert isinstance(provider, USASpecProvider)
        assert provider.seed == seed

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
___ ERROR collecting test_mimesis_builtins_en_USASpecProvider___init___0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider___init___0.py:4: in <module>
    from mimesis.providers import USASpecProvider
E   ImportError: cannot import name 'USASpecProvider' from 'mimesis.providers' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_en_USASpecProvider___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.22s ===============================
"""