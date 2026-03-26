
import os
import pytest
from pytutils.log import get_config

# Test cases for the get_config function

def test_get_config_with_none_config():
    # Test case where config is None, should raise ValueError
    given = None
    env_var = None
    default = None
    
    with pytest.raises(ValueError) as excinfo:
        get_config(given=given, env_var=env_var, default=default)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_log_get_config_1.py .F              [100%]

=================================== FAILURES ===================================
______________________ test_get_config_with_invalid_json _______________________

given = '{"key": "value"', env_var = None, default = None

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

self = <json.decoder.JSONDecoder object at 0x7f2ee4399d50>
s = '{"key": "value"', idx = 0

    def raw_decode(self, s, idx=0):
        """Decode a JSON document from ``s`` (a ``str`` beginning with
        a JSON document) and return a 2-tuple of the Python
        representation and the index in ``s`` where the document ended.
    
        This can be used to decode a JSON document from a string that may
        have extraneous data at the end.
    
        """
        try:
>           obj, end = self.scan_once(s, idx)
E           json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 16 (char 15)

/usr/local/lib/python3.11/json/decoder.py:353: JSONDecodeError

During handling of the above exception, another exception occurred:

    def test_get_config_with_invalid_json():
        # Test case where config is a string that cannot be parsed as JSON, should raise ValueError
        given = '{"key": "value"'  # Invalid JSON due to missing closing brace
        env_var = None
        default = None
    
        with pytest.raises(ValueError) as excinfo:
>           get_config(given=given, env_var=env_var, default=default)

pytutils/Test4DT_tests/test_pytutils_log_get_config_1.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = '{"key": "value"', env_var = None, default = None

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
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_1.py::test_get_config_with_invalid_json
========================= 1 failed, 1 passed in 0.08s ==========================
"""