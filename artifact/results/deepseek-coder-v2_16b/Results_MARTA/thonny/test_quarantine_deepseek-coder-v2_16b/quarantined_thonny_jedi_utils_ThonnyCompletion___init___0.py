
import pytest
from thonny import ThonnyCompletion

def test_thonny_completion_initialization():
    # Arrange/Act
    completion = ThonnyCompletion(name='print', complete='print()', type='function', description='Prints to the console.', parent=None, full_name='builtins.print')
    
    # Assert
    assert completion.name == 'print'
    assert completion.complete == 'print()'
    assert completion.type == 'function'
    assert completion.description == 'Prints to the console.'
    assert completion.parent is None
    assert completion.full_name == 'builtins.print'

def test_thonny_completion_dictionary_interface():
    # Arrange/Act
    completion = ThonnyCompletion(name='print', complete='print()', type='function', description='Prints to the console.', parent=None, full_name='builtins.print')
    
    # Assert
    assert completion['name'] == 'print'
    assert completion['complete'] == 'print()'
    assert completion['type'] == 'function'
    assert completion['description'] == 'Prints to the console.'
    assert completion['parent'] is None
    assert completion['full_name'] == 'builtins.print'

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
____ ERROR collecting test_thonny_jedi_utils_ThonnyCompletion___init___0.py ____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_ThonnyCompletion___init___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_ThonnyCompletion___init___0.py:3: in <module>
    from thonny import ThonnyCompletion
E   ImportError: cannot import name 'ThonnyCompletion' from 'thonny' (/opt/marta/baselines/codamosa/replication/test-apps/thonny/thonny/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_jedi_utils_ThonnyCompletion___init___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.11s ===============================
"""