
import os
import pytest
from pytutils.log import get_config

@pytest.mark.parametrize("given, env_var, default", [
    (None, 'LOG_CONFIG', None),
    ('invalid_json', 'LOG_CONFIG', None),
    (None, 'NON_EXISTENT_ENV_VAR', {'default': 'config'}),
    (None, None, None)
])
def test_invalid_inputs(monkeypatch, given, env_var, default):
    if given is not None:
        monkeypatch.setenv('LOG_CONFIG', given)
    elif env_var is not None:
        monkeypatch.delenv('LOG_CONFIG', raising=False)

    with pytest.raises(ValueError):
        get_config(given, env_var, default)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

../../../dev .FF.                                                        [100%]

=================================== FAILURES ===================================
______________ test_invalid_inputs[invalid_json-LOG_CONFIG-None] _______________

given = 'invalid_json', env_var = 'LOG_CONFIG', default = None

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

self = <json.decoder.JSONDecoder object at 0x7f930c6f9890>, s = 'invalid_json'
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

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f930a9dab10>
given = 'invalid_json', env_var = 'LOG_CONFIG', default = None

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'LOG_CONFIG', None),
        ('invalid_json', 'LOG_CONFIG', None),
        (None, 'NON_EXISTENT_ENV_VAR', {'default': 'config'}),
        (None, None, None)
    ])
    def test_invalid_inputs(monkeypatch, given, env_var, default):
        if given is not None:
            monkeypatch.setenv('LOG_CONFIG', given)
        elif env_var is not None:
            monkeypatch.delenv('LOG_CONFIG', raising=False)
    
        with pytest.raises(ValueError):
>           get_config(given, env_var, default)

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_inputs.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

given = 'invalid_json', env_var = 'LOG_CONFIG', default = None

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
___________ test_invalid_inputs[None-NON_EXISTENT_ENV_VAR-default2] ____________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f930ae6b9d0>
given = None, env_var = 'NON_EXISTENT_ENV_VAR', default = {'default': 'config'}

    @pytest.mark.parametrize("given, env_var, default", [
        (None, 'LOG_CONFIG', None),
        ('invalid_json', 'LOG_CONFIG', None),
        (None, 'NON_EXISTENT_ENV_VAR', {'default': 'config'}),
        (None, None, None)
    ])
    def test_invalid_inputs(monkeypatch, given, env_var, default):
        if given is not None:
            monkeypatch.setenv('LOG_CONFIG', given)
        elif env_var is not None:
            monkeypatch.delenv('LOG_CONFIG', raising=False)
    
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

pytutils/Test4DT_tests/test_pytutils_log_get_config_2_test_invalid_inputs.py:18: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-bscea9ap'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ie9kv1w1'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-jueww45v'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_invalid_inputs[invalid_json-LOG_CONFIG-None] - Typ...
FAILED ../../../dev/::test_invalid_inputs[None-NON_EXISTENT_ENV_VAR-default2]
=================== 2 failed, 2 passed, 3 warnings in 0.10s ====================
"""