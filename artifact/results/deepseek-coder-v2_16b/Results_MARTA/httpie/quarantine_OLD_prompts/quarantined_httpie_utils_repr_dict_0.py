
import pytest
from httpie.utils import repr_dict
import pformat
from unittest.mock import patch

def test_repr_dict_simple():
    simple_dict = {'key': 'value'}
    with patch('httpie.utils.pformat', return_value='{"key": "value"}') as mock_pformat:
        result = repr_dict(simple_dict)
        assert result == '{"key": "value"}'
        mock_pformat.assert_called_once_with({'key': 'value'})

def test_repr_dict_nested():
    nested_dict = {'outerKey': {'innerKey': [1, 2, 3]}}
    with patch('httpie.utils.pformat', return_value='{"outerKey": {"innerKey": [1, 2, 3}}') as mock_pformat:
        result = repr_dict(nested_dict)
        assert result == '{"outerKey": {"innerKey": [1, 2, 3]}}'
        mock_pformat.assert_called_once_with({'outerKey': {'innerKey': [1, 2, 3]}})

def test_repr_dict_mixed():
    mixed_dict = {'stringKey': 'a string', 'intKey': 42, 'listKey': [1, 'two', None]}
    with patch('httpie.utils.pformat', return_value='{"stringKey": "a string", "intKey": 42, "listKey": [1, "two", None]}') as mock_pformat:
        result = repr_dict(mixed_dict)
        assert result == '{"stringKey": "a string", "intKey": 42, "listKey": [1, "two", None]}'
        mock_pformat.assert_called_once_with({'stringKey': 'a string', 'intKey': 42, 'listKey': [1, 'two', None]})

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
______________ ERROR collecting test_httpie_utils_repr_dict_0.py _______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_repr_dict_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_repr_dict_0.py:4: in <module>
    import pformat
E   ModuleNotFoundError: No module named 'pformat'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_utils_repr_dict_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.24s ===============================
"""