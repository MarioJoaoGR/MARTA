
import pytest
import os
from pytutils.log import get_config

@pytest.fixture(autouse=True)
def mock_env_var(monkeypatch):
    monkeypatch.setenv('CONFIG', '{"key": "value"}')

def test_get_config_with_given():
    config = get_config(given={'key': 'value'})
    assert config == {'key': 'value'}

def test_get_config_with_env_var():
    os.environ.pop('CONFIG', None)  # Ensure the env var is not set initially
    config = get_config(env_var='CONFIG')
    assert config == {"key": "value"}

def test_get_config_with_default():
    config = get_config(default={'default_key': 'default_value'})
    assert config == {'default_key': 'default_value'}

def test_get_config_invalid_config():
    with pytest.raises(ValueError):
        get_config()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

pytutils/Test4DT_tests/test_pytutils_log_get_config_4_test_edge_cases.py . [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
_________________________ test_get_config_with_env_var _________________________

    def test_get_config_with_env_var():
        os.environ.pop('CONFIG', None)  # Ensure the env var is not set initially
>       config = get_config(env_var='CONFIG')

pytutils/Test4DT_tests/test_pytutils_log_get_config_4_test_edge_cases.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = 'CONFIG', default = None

    def get_config(given=None, env_var=None, default=None):
        config = given
    
        if not config and env_var:
            config = os.environ.get(env_var)
    
        if not config and default:
            config = default
    
        if config is None:
>           raise ValueError('Invalid logging config: %s' % config)
E           ValueError: Invalid logging config: None

pytutils/pytutils/log.py:114: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_4_test_edge_cases.py::test_get_config_with_env_var
========================= 1 failed, 3 passed in 0.08s ==========================
"""