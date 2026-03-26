
import pytest
from isort.settings import _Config

def test_valid_case():
    config = _Config(
        py_version='3',
        skip=frozenset({'os', 'sys'}),
        line_length=88
    )
    assert isinstance(config, _Config)
    assert config.py_version == '3'
    assert config.skip == frozenset({'os', 'sys'})
    assert config.line_length == 88

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        config = _Config(
            py_version='3',
            skip=frozenset({'os', 'sys'}),
            line_length=88
        )
        assert isinstance(config, _Config)
>       assert config.py_version == '3'
E       AssertionError: assert 'py3' == '3'
E         
E         - 3
E         + py3

isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_valid_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings__Config___hash___0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.09s ===============================
"""