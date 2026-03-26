
import pytest
import os
from pytutils.log import get_config

@pytest.mark.parametrize("given, env_var, default", [
    (None, 'INVALID_ENV', {'default': 'value'}),
    ({}, 'INVALID_ENV', None),
    ('invalid_json', None, None),
    ('{"key": "value"}', 'INVALID_ENV', None)
])
def test_invalid_inputs(given, env_var, default):
    os.environ['INVALID_ENV'] = 'invalid_value'
    
    with pytest.raises(ValueError):
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
collected 4 items

pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________ test_invalid_inputs[None-INVALID_ENV-default0] ________________

given = None, env_var = 'INVALID_ENV', default = {'default': 'value'}

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

self = <json.decoder.JSONDecoder object at 0x7f7adf182d50>, s = 'invalid_value'
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

given = None, env_var = 'INVALID_ENV', default = {'default': 'value'}

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', {'default': 'value'}),
        ({}, 'INVALID_ENV', None),
        ('invalid_json', None, None),
        ('{"key": "value"}', 'INVALID_ENV', None)
    ])
    def test_invalid_inputs(given, env_var, default):
        os.environ['INVALID_ENV'] = 'invalid_value'
    
        with pytest.raises(ValueError):
>           get_config(given=given, env_var=env_var, default=default)

pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = None, env_var = 'INVALID_ENV', default = {'default': 'value'}

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
_________________ test_invalid_inputs[given1-INVALID_ENV-None] _________________

given = {}, env_var = 'INVALID_ENV', default = None

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

self = <json.decoder.JSONDecoder object at 0x7f7adf182d50>, s = 'invalid_value'
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

given = {}, env_var = 'INVALID_ENV', default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', {'default': 'value'}),
        ({}, 'INVALID_ENV', None),
        ('invalid_json', None, None),
        ('{"key": "value"}', 'INVALID_ENV', None)
    ])
    def test_invalid_inputs(given, env_var, default):
        os.environ['INVALID_ENV'] = 'invalid_value'
    
        with pytest.raises(ValueError):
>           get_config(given=given, env_var=env_var, default=default)

pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = {}, env_var = 'INVALID_ENV', default = None

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
_________________ test_invalid_inputs[invalid_json-None-None] __________________

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

self = <json.decoder.JSONDecoder object at 0x7f7adf182d50>, s = 'invalid_json'
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

given = 'invalid_json', env_var = None, default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', {'default': 'value'}),
        ({}, 'INVALID_ENV', None),
        ('invalid_json', None, None),
        ('{"key": "value"}', 'INVALID_ENV', None)
    ])
    def test_invalid_inputs(given, env_var, default):
        os.environ['INVALID_ENV'] = 'invalid_value'
    
        with pytest.raises(ValueError):
>           get_config(given=given, env_var=env_var, default=default)

pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py:16: 
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
____________ test_invalid_inputs[{"key": "value"}-INVALID_ENV-None] ____________

given = '{"key": "value"}', env_var = 'INVALID_ENV', default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'INVALID_ENV', {'default': 'value'}),
        ({}, 'INVALID_ENV', None),
        ('invalid_json', None, None),
        ('{"key": "value"}', 'INVALID_ENV', None)
    ])
    def test_invalid_inputs(given, env_var, default):
        os.environ['INVALID_ENV'] = 'invalid_value'
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py:15: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py::test_invalid_inputs[None-INVALID_ENV-default0]
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py::test_invalid_inputs[given1-INVALID_ENV-None]
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py::test_invalid_inputs[invalid_json-None-None]
FAILED pytutils/Test4DT_tests/test_pytutils_log_get_config_5_test_invalid_inputs.py::test_invalid_inputs[{"key": "value"}-INVALID_ENV-None]
============================== 4 failed in 0.12s ===============================
"""