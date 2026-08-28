
import pytest
from mimesis.builtins.ru import RussiaSpecProvider
from mimesis.seed import Seed

# Test initialization without a seed
def test_russia_spec_provider_initialization():
    provider = RussiaSpecProvider()
    assert isinstance(provider, RussiaSpecProvider)
    assert provider._locale == 'ru'
    # No seed is provided, so it should default to the current system time
    assert isinstance(provider.seed, Seed)

# Test initialization with a specific seed
def test_russia_spec_provider_initialization_with_seed():
    seed = Seed(specific_data='some_special_data')
    provider = RussiaSpecProvider(seed=seed)
    assert isinstance(provider, RussiaSpecProvider)
    assert provider._locale == 'ru'
    assert provider.seed == seed

# Test generating a passport series without specifying the year
def test_passport_series_without_year():
    provider = RussiaSpecProvider()
    series = provider.passport_series()
    region, year = series.split()
    assert len(region) == 2 and region.isdigit()
    assert len(year) == 2 and year.isdigit()
    # Check that the year is between 10 and 18 (inclusive)
    assert int(year) >= 10 and int(year) <= 18

# Test generating a passport series specifying the year
def test_passport_series_with_year():
    provider = RussiaSpecProvider()
    series = provider.passport_series(year=2023)
    region, year = series.split()
    assert len(region) == 2 and region.isdigit()
    assert len(year) == 2 and year.isdigit()
    # Check that the specified year is used
    assert int(year) == 2023

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
_ ERROR collecting test_mimesis_builtins_ru_RussiaSpecProvider_passport_series_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_ru_RussiaSpecProvider_passport_series_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_ru_RussiaSpecProvider_passport_series_0.py:4: in <module>
    from mimesis.seed import Seed
E   ModuleNotFoundError: No module named 'mimesis.seed'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_builtins_ru_RussiaSpecProvider_passport_series_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.24s ===============================
"""