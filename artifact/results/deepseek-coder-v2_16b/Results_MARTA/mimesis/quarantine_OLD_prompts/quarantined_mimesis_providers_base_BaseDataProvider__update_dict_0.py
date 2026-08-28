
import pytest
from unittest.mock import patch
from mimesis.providers.base import BaseDataProvider
import locales

# Test initialization with default locale and seed
def test_default_init():
    with patch('locales.DEFAULT_LOCALE', 'en_US'):
        base_data_provider = BaseDataProvider()
        assert base_data_provider._data_dir == Path(__file__).parent.parent.joinpath('data')
        assert isinstance(base_data_provider, BaseDataProvider)

# Test initialization with specific locale and seed
def test_specific_init():
    with patch('locales.DEFAULT_LOCALE', 'en_US'):
        base_data_provider = BaseDataProvider(locale="es_ES", seed=12345)
        assert base_data_provider._data_dir == Path(__file__).parent.parent.joinpath('data')
        assert isinstance(base_data_provider, BaseDataProvider)

# Test updating a dictionary recursively
def test_update_dict():
    provider = BaseDataProvider()
    initial_dict = {'a': 1}
    updated_dict = {'b': 2}
    result = provider._update_dict(initial_dict, updated_dict)
    assert result == {'a': 1, 'b': 2}

# Test updating a nested dictionary recursively
def test_nested_update_dict():
    provider = BaseDataProvider()
    initial_dict = {'a': {'b': 1}}
    updated_dict = {'a': {'c': 2}}
    result = provider._update_dict(initial_dict, updated_dict)
    assert result == {'a': {'b': 1, 'c': 2}}

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
_ ERROR collecting test_mimesis_providers_base_BaseDataProvider__update_dict_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__update_dict_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__update_dict_0.py:5: in <module>
    import locales
E   ModuleNotFoundError: No module named 'locales'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__update_dict_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""