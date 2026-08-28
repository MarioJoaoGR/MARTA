
import pytest
from tornado.options import Option

def test_parse_timedelta():
    opt = Option(name="duration", type=str, default="0s")
    with pytest.raises(Exception):
        assert opt._parse_timedelta("invalid input")

    parsed_delta = opt._parse_timedelta("2h 30m")
    expected_delta = datetime.timedelta(hours=2, minutes=30)
    assert parsed_delta == expected_delta

def test_default_value():
    opt = Option(name="duration", type=str, default="1d")
    parsed_delta = opt._parse_timedelta("1d")
    expected_delta = datetime.timedelta(days=1)
    assert parsed_delta == expected_delta

def test_multiple_values():
    opt = Option(name="duration", type=str, default="0s", multiple=True)
    with pytest.raises(Exception):
        assert opt._parse_timedelta("invalid input")

    parsed_deltas = opt._parse_timedelta("2h 30m;1d")
    expected_delta1 = datetime.timedelta(hours=2, minutes=30)
    expected_delta2 = datetime.timedelta(days=1)
    assert len(parsed_deltas) == 2
    assert parsed_deltas[0] == expected_delta1
    assert parsed_deltas[1] == expected_delta2

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_tornado_options__Option__parse_timedelta_1.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_options__Option__parse_timedelta_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_options__Option__parse_timedelta_1.py:3: in <module>
    from tornado.options import Option
E   ImportError: cannot import name 'Option' from 'tornado.options' (/opt/marta/baselines/codamosa/replication/test-apps/tornado/tornado/options.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_options__Option__parse_timedelta_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.16s ===============================
"""