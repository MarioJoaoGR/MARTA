
import os
import pytest
from cookiecutter.replay import dump
from cookiecutter.utils import make_sure_path_exists, get_file_name
import json

# Test for valid call with all parameters provided
def test_valid_dump():
    replay_dir = 'data'
    template_name = 'example'
    context = {'cookiecutter': {'key': 'value'}, 'other_key': 'other_value'}
    
    dump(replay_dir, template_name, context)
    
    expected_file_path = os.path.join(replay_dir, f"{template_name}.json")
    assert os.path.isfile(expected_file_path), f"Expected file {expected_file_path} does not exist."
    
    with open(expected_file_path, 'r') as file:
        written_context = json.load(file)
        assert written_context == context, "Written JSON content does not match the provided context."

# Test for invalid template name type (should raise TypeError)
def test_invalid_template_name_type():
    replay_dir = 'data'
    template_name = 123
    context = {'cookiecutter': {'key': 'value'}, 'other_key': 'other_value'}
    
    with pytest.raises(TypeError):
        dump(replay_dir, template_name, context)

# Test for invalid context type (should raise TypeError)
def test_invalid_context_type():
    replay_dir = 'data'
    template_name = 'example'
    context = 'invalid_context'
    
    with pytest.raises(TypeError):
        dump(replay_dir, template_name, context)

# Test for missing cookiecutter key in context (should raise ValueError)
def test_missing_cookiecutter_key():
    replay_dir = 'data'
    template_name = 'example'
    context = {'other_key': 'other_value'}
    
    with pytest.raises(ValueError):
        dump(replay_dir, template_name, context)

# Test for invalid replay directory (should raise IOError)
def test_invalid_replay_directory():
    replay_dir = 'non_existent_dir'
    template_name = 'example'
    context = {'cookiecutter': {'key': 'value'}, 'other_key': 'other_value'}
    
    with pytest.raises(IOError):
        dump(replay_dir, template_name, context)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____________ ERROR collecting test_cookiecutter_replay_dump_0.py ______________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_dump_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_dump_0.py:5: in <module>
    from cookiecutter.utils import make_sure_path_exists, get_file_name
E   ImportError: cannot import name 'get_file_name' from 'cookiecutter.utils' (/opt/marta/baselines/codamosa/replication/test-apps/cookiecutter/cookiecutter/utils.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_dump_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.15s ===============================
"""