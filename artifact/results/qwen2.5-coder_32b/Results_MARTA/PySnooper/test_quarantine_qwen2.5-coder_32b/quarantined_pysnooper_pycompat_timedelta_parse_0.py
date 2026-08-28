
import pytest
from datetime import timedelta as datetime_module
from pysnooper.pycompat import str

def timedelta_parse(s):
    parts = s.replace('.', ':').split(':')
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
        microseconds = 0
    elif len(parts) == 4:
        hours, minutes, seconds, microseconds = map(int, parts)
    else:
        raise ValueError("Input string must be in the format 'HH:MM:SS' or 'HH:MM:SS.mmmmmm'")
    
    return datetime_module(hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)

def test_timedelta_parse_full_precision():
    result = timedelta_parse('01:23:45.678901')
    assert result == datetime_module(seconds=5025, microseconds=678901)

def test_timedelta_parse_without_microseconds():
    result = timedelta_parse('23:59:59')
    assert result == datetime_module(days=1, seconds=1)

def test_timedelta_parse_fractional_seconds():
    result = timedelta_parse('00:45:30.123')
    assert result == datetime_module(seconds=2730, microseconds=123000)

def test_timedelta_parse_zero_hours_minutes():
    result = timedelta_parse('00:00:00.999999')
    assert result == datetime_module(microseconds=999999)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_pysnooper_pycompat_timedelta_parse_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_pycompat_timedelta_parse_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_pycompat_timedelta_parse_0.py:4: in <module>
    from pysnooper.pycompat import str
E   ImportError: cannot import name 'str' from 'pysnooper.pycompat' (/opt/marta/baselines/codamosa/replication/test-apps/PySnooper/pysnooper/pycompat.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_qwen2.5-coder_32b/test_pysnooper_pycompat_timedelta_parse_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""