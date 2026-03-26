
import pytest
import os
from pytutils.log import get_config

def test_valid_inputs():
    # Test when given is a valid dictionary
    given = {"key": "value"}
    config = get_config(given=given)
    assert config == given

    # Test when env_var is set and contains valid JSON
    os.environ['CONFIG'] = '{"env_key": "env_value"}'
    config = get_config(env_var='CONFIG')
    assert config == {'env_key': 'env_value'}
    del os.environ['CONFIG']

    # Test when default is provided and contains valid JSON
    config = get_config(default={'default_key': 'default_value'})
    assert config == {'default_key': 'default_value'}

    # Test when given is a string that can be parsed as JSON
    given_str = '{"string_key": "string_value"}'
    config = get_config(given=given_str)
    assert config == {'string_key': 'string_value'}

    # Test when given is a string that cannot be parsed (should raise ValueError)
    with pytest.raises(ValueError):
        bad_str = 'invalid_json'
        get_config(given=bad_str)

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

pytutils/Test4DT_tests/test_pytutils_log_get_config_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

given = 'invalid_json', env_var = None, default = None

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

self = <json.decoder.JSONDecoder object at 0x7f0bd0146110>, s = 'invalid_json'
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

    def test_valid_inputs():
        # Test when given is a valid dictionary
        given = {"key": "value"}
        config = get_config(given=given)
        assert config == given
    
        # Test when env_var is set and contains valid JSON
        os.environ['CONFIG'] = '{"env_key": "env_value"}'
        config = get_config(env_var='CONFIG')
        assert config == {'env_key': 'env_value'}
        del os.environ['CONFIG']
    
        # Test when default is provided and contains valid JSON
        config = get_config(default={'default_key': 'default_value'})
        assert config == {'default_key': 'default_value'}
    
        # Test when given is a string that can be parsed as JSON
        given_str = '{"string_key": "string_value"}'
        config = get_config(given=given_str)
        assert config == {'string_key': 'string_value'}
    
        # Test when given is a string that cannot be parsed (should raise ValueError)
        with pytest.raises(ValueError):
            bad_str = 'invalid_json'
>           get_config(given=bad_str)

pytutils/Test4DT_tests/test_pytutils_log_get_config_0_test_valid_inputs.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = 'invalid_json', env_var = None, default = None

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
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""