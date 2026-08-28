
import pytest
from unittest.mock import patch
from httpie.cli.argparser import check_options, OUTPUT_OPTIONS

def test_check_options_valid():
    with patch('httpie.cli.argparser.OUTPUT_OPTIONS', {'a', 'b'}):
        assert check_options({'a', 'b'}, 'output') is None

def test_check_options_invalid():
    with patch('httpie.cli.argparser.OUTPUT_OPTIONS', {'a', 'b'}), pytest.raises(Exception) as excinfo:
        check_options({'a', 'b', 'c'}, 'output')
    assert str(excinfo.value) == "Unknown output options: c"

def test_check_options_list():
    with patch('httpie.cli.argparser.OUTPUT_OPTIONS', {'a', 'b'}):
        with pytest.raises(Exception) as excinfo:
            check_options(['a', 'b', 'c'], 'output')
        assert str(excinfo.value) == "Unknown output options: c"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
________ ERROR collecting test_httpie_cli_argparser_check_options_0.py _________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_check_options_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_check_options_0.py:4: in <module>
    from httpie.cli.argparser import check_options, OUTPUT_OPTIONS
E   ImportError: cannot import name 'check_options' from 'httpie.cli.argparser' (/opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/cli/argparser.py)
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5
  /opt/marta/baselines/codamosa/replication/test-apps/httpie/httpie/plugins/manager.py:5: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
    from pkg_resources import iter_entry_points

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argparser_check_options_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 1 warning, 1 error in 0.91s ==========================
"""