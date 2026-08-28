
import pytest
from pymonet.maybe import Maybe, Nothing

def test_filter_with_valid_value():
    maybe_some = Maybe(value=42, is_nothing=False)
    filtered_maybe = maybe_some.filter(lambda x: isinstance(x, int))
    assert not filtered_maybe.is_nothing
    assert filtered_maybe.value == 42

def test_filter_with_invalid_value():
    maybe_none = Maybe(value=None, is_nothing=True)
    filtered_maybe = maybe_none.filter(lambda x: isinstance(x, int))
    assert filtered_maybe.is_nothing
    assert filtered_maybe.value is None

def test_filter_with_empty_maybe():
    empty_maybe = Maybe(value=None, is_nothing=True)
    default_value = Nothing()
    filtered_maybe = empty_maybe.filter(lambda x: isinstance(x, int))
    assert filtered_maybe.is_nothing
    assert filtered_maybe.value == default_value.value

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____________ ERROR collecting test_pymonet_maybe_Maybe_filter_0.py _____________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_maybe_Maybe_filter_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_maybe_Maybe_filter_0.py:3: in <module>
    from pymonet.maybe import Maybe, Nothing
E   ImportError: cannot import name 'Nothing' from 'pymonet.maybe' (/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/maybe.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_maybe_Maybe_filter_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.12s ===============================
"""