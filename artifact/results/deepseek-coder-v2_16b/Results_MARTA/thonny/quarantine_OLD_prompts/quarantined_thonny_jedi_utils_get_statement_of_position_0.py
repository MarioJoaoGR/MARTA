
import pytest
from unittest.mock import patch
import ast
from jedi.parser_utils import get_statement_of_position as original_get_statement_of_position

def test_get_statement_of_position():
    node = ast.parse("print('Hello, World!')")
    pos = (1, 0)
    
    with patch('jedi.parser_utils.get_statement_of_position', autospec=True) as mock_get_statement:
        mock_get_statement.return_value = "Mocked Statement"
        
        from thonny.plugins.esp.esp8266_api_stubs.builtins import get_statement_of_position
        statement = get_statement_of_position(node, pos)
        
        assert statement == "Mocked Statement"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
____ ERROR collecting test_thonny_jedi_utils_get_statement_of_position_0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py:5: in <module>
    from jedi.parser_utils import get_statement_of_position as original_get_statement_of_position
E   ImportError: cannot import name 'get_statement_of_position' from 'jedi.parser_utils' (/data/pydeps/marta/jedi/parser_utils.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_get_statement_of_position_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.20s ===============================
"""