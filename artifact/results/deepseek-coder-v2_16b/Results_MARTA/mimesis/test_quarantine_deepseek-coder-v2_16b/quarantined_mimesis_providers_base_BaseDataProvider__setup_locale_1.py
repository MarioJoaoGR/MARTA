
import pytest
from mimesis import UnsupportedLocale
from mimesis.providers.base import BaseDataProvider, locales

def test_BaseDataProvider_default_initialization():
    provider = BaseDataProvider()
    assert provider.locale == locales.DEFAULT_LOCALE
    assert provider._data == {}
    assert provider._datafile == ''
    assert str(provider) == 'BaseDataProvider'

def test_BaseDataProvider_specific_locale_and_seed():
    provider = BaseDataProvider(locale="en_US", seed=42)
    assert provider.locale == "en_US"
    assert provider._data == {}
    assert provider._datafile == ''
    assert str(provider) == 'BaseDataProvider'

def test_BaseDataProvider_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        BaseDataProvider(locale="xx_YY")

def test_BaseDataProvider__setup_locale_valid_locale():
    provider = BaseDataProvider()
    provider._setup_locale("en_US")
    assert provider.locale == "en_US"

def test_BaseDataProvider__setup_locale_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        provider = BaseDataProvider()
        provider._setup_locale("xx_YY")

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
_ ERROR collecting test_mimesis_providers_base_BaseDataProvider__setup_locale_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_1.py:3: in <module>
    from mimesis import UnsupportedLocale
E   ImportError: cannot import name 'UnsupportedLocale' from 'mimesis' (/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""