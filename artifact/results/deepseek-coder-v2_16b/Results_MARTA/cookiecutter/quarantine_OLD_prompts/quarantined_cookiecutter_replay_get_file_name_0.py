
import os
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.replay import get_file_name

# Test for valid case where the directory and 'cookiecutter.json' file exist
@pytest.mark.parametrize("test_inputs, expected", [
    (('data', 'example'), 'data/example.json'),
    (('logs/', 'logfile'), 'logs/logfile.json'),
    (('backups/', 'backup123'), 'backups/backup123.json')
])
def test_get_file_name(test_inputs, expected):
    replay_dir, template_name = test_inputs
    with patch('os.path.join', return_value='data/example.json'):
        assert get_file_name(replay_dir, template_name) == expected

# Test for case where replay_dir is None
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_get_file_name_0.py . [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________ test_get_file_name[test_inputs1-logs/logfile.json] ______________

test_inputs = ('logs/', 'logfile'), expected = 'logs/logfile.json'

    @pytest.mark.parametrize("test_inputs, expected", [
        (('data', 'example'), 'data/example.json'),
        (('logs/', 'logfile'), 'logs/logfile.json'),
        (('backups/', 'backup123'), 'backups/backup123.json')
    ])
    def test_get_file_name(test_inputs, expected):
        replay_dir, template_name = test_inputs
        with patch('os.path.join', return_value='data/example.json'):
>           assert get_file_name(replay_dir, template_name) == expected
E           AssertionError: assert 'data/example.json' == 'logs/logfile.json'
E             
E             - logs/logfile.json
E             + data/example.json

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_get_file_name_0.py:16: AssertionError
___________ test_get_file_name[test_inputs2-backups/backup123.json] ____________

test_inputs = ('backups/', 'backup123'), expected = 'backups/backup123.json'

    @pytest.mark.parametrize("test_inputs, expected", [
        (('data', 'example'), 'data/example.json'),
        (('logs/', 'logfile'), 'logs/logfile.json'),
        (('backups/', 'backup123'), 'backups/backup123.json')
    ])
    def test_get_file_name(test_inputs, expected):
        replay_dir, template_name = test_inputs
        with patch('os.path.join', return_value='data/example.json'):
>           assert get_file_name(replay_dir, template_name) == expected
E           AssertionError: assert 'data/example.json' == 'backups/backup123.json'
E             
E             - backups/backup123.json
E             + data/example.json

/opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_get_file_name_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_get_file_name_0.py::test_get_file_name[test_inputs1-logs/logfile.json]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/cookiecutter/Test4DT_tests_deepseek-coder-v2_16b/test_cookiecutter_replay_get_file_name_0.py::test_get_file_name[test_inputs2-backups/backup123.json]
========================= 2 failed, 1 passed in 0.08s ==========================
"""