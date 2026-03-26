
import logging
from pytutils.log import configure, DEFAULT_CONFIG, get_config
import os
import pytest

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Setup code before each test
    if 'LOGGING' in os.environ:
        del os.environ['LOGGING']
    
    yield  # This is where the tests are run
    
    # Teardown code after each test
    pass

def test_invalid_env_var():
    """
    Test that verifies the configuration falls back to default when env var is invalid.
    """
    os.environ['LOGGING'] = 'invalid_json'  # Set an invalid environment variable
    
    log = logging.getLogger(__name__)
    configure()
    
    with pytest.raises(Exception):
        log.info('test')  # This should raise an exception because the configuration is invalid

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_invalid_env_var.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_env_var _____________________________

given = None, env_var = 'LOGGING'
default = {'disable_existing_loggers': False, 'formatters': {'colored': {'()': 'colorlog.ColoredFormatter', 'datefmt': '%H:%M:%S...red', 'level': 10}}, 'loggers': {'importmagic': {'level': 20}, 'parso': {'level': 20}, 'requests': {'level': 20}}, ...}

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

pytutils/pytutils/log.py:120: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/json/__init__.py:346: in loads
    return _default_decoder.decode(s)
/usr/local/lib/python3.11/json/decoder.py:337: in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <json.decoder.JSONDecoder object at 0x7f27f39366d0>, s = 'invalid_json'
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

/usr/local/lib/python3.11/json/decoder.py:355: JSONDecodeError

During handling of the above exception, another exception occurred:

    def test_invalid_env_var():
        """
        Test that verifies the configuration falls back to default when env var is invalid.
        """
        os.environ['LOGGING'] = 'invalid_json'  # Set an invalid environment variable
    
        log = logging.getLogger(__name__)
>       configure()

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_invalid_env_var.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:93: in configure
    cfg = get_config(config, env_var, default)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = 'LOGGING'
default = {'disable_existing_loggers': False, 'formatters': {'colored': {'()': 'colorlog.ColoredFormatter', 'datefmt': '%H:%M:%S...red', 'level': 10}}, 'loggers': {'importmagic': {'level': 20}, 'parso': {'level': 20}, 'requests': {'level': 20}}, ...}

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

pytutils/pytutils/log.py:125: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_invalid_env_var.py::test_invalid_env_var
============================== 1 failed in 0.10s ===============================
"""