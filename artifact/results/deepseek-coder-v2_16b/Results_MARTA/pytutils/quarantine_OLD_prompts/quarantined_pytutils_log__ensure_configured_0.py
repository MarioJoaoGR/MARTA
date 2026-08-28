
import pytest
from unittest.mock import patch, call
import os
from pytutils.log import _ensure_configured, configure


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log__ensure_configured_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_ensure_configured_custom_config _____________________

    def test_ensure_configured_custom_config():
        with patch('pytutils.log._CONFIGURED', [], create=True):
            os.environ['LOGGING'] = '{"handlers": {"file": {"level": "DEBUG", "class": "logging.FileHandler", "filename": "app.log"}}}'
>           _ensure_configured()

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log__ensure_configured_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:138: in _ensure_configured
    configure()
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:92: in configure
    logging.config.dictConfig(cfg)
/opt/conda/envs/test4py_env/lib/python3.10/logging/config.py:811: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f333de3d3c0>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
>           raise ValueError("dictionary doesn't specify a version")
E           ValueError: dictionary doesn't specify a version

/opt/conda/envs/test4py_env/lib/python3.10/logging/config.py:498: ValueError
____________________ test_ensure_configured_invalid_config _____________________

given = None, env_var = 'LOGGING'
default = {'disable_existing_loggers': False, 'formatters': {'colored': {'()': 'colorlog.ColoredFormatter', 'datefmt': '%H:%M:%S... {'class': 'logging.StreamHandler', 'formatter': 'colored', 'level': 10}}, 'loggers': {'requests': {'level': 20}}, ...}

    def get_config(given=None, env_var=None, default=None):
        config = given
    
        if not config and env_var:
            config = os.environ.get(env_var)
    
        if not config and default:
            config = default
    
        if config is None:
            raise ValueError('Invalid logging config: %s' % config)
    
        if isinstance(config, _PyInfo.string_types):
            import json
    
            try:
>               config = json.loads(config)

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:116: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/json/__init__.py:346: in loads
    return _default_decoder.decode(s)
/opt/conda/envs/test4py_env/lib/python3.10/json/decoder.py:337: in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <json.decoder.JSONDecoder object at 0x7f333eb66f80>, s = 'invalid json'
idx = 0

    def raw_decode(self, s, idx=0):
        """Decode a JSON document from ``s`` (a ``str`` beginning with
        a JSON document) and return a 2-tuple of the Python
        representation and the index in ``s`` where the document ended.
    
        This can be used to decode a JSON document from a string that may
        have extraneous data at the end.
    
        """
        try:
            obj, end = self.scan_once(s, idx)
        except StopIteration as err:
>           raise JSONDecodeError("Expecting value", s, err.value) from None
E           json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

/opt/conda/envs/test4py_env/lib/python3.10/json/decoder.py:355: JSONDecodeError

During handling of the above exception, another exception occurred:

    def test_ensure_configured_invalid_config():
        with patch('pytutils.log._CONFIGURED', [], create=True):
            os.environ['LOGGING'] = 'invalid json'
            with pytest.raises(ValueError):
>               _ensure_configured()

/opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log__ensure_configured_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:138: in _ensure_configured
    configure()
/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:89: in configure
    cfg = get_config(config, env_var, default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = 'LOGGING'
default = {'disable_existing_loggers': False, 'formatters': {'colored': {'()': 'colorlog.ColoredFormatter', 'datefmt': '%H:%M:%S... {'class': 'logging.StreamHandler', 'formatter': 'colored', 'level': 10}}, 'loggers': {'requests': {'level': 20}}, ...}

    def get_config(given=None, env_var=None, default=None):
        config = given
    
        if not config and env_var:
            config = os.environ.get(env_var)
    
        if not config and default:
            config = default
    
        if config is None:
            raise ValueError('Invalid logging config: %s' % config)
    
        if isinstance(config, _PyInfo.string_types):
            import json
    
            try:
                config = json.loads(config)
            except ValueError:
                import yaml
    
                try:
>                   config = yaml.load(config)
E                   TypeError: load() missing 1 required positional argument: 'Loader'

/opt/marta/baselines/codamosa/replication/test-apps/pytutils/pytutils/log.py:121: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log__ensure_configured_0.py::test_ensure_configured_custom_config
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pytutils/Test4DT_tests_deepseek-coder-v2_16b/test_pytutils_log__ensure_configured_0.py::test_ensure_configured_invalid_config
============================== 2 failed in 0.10s ===============================
"""