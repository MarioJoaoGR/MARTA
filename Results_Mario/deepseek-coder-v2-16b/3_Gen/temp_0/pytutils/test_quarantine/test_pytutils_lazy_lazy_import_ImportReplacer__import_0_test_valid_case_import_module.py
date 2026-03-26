
from pytutils.lazy.lazy_import import ImportReplacer

def test_valid_case_import_module():
    scope = globals()
    replacer = ImportReplacer(scope=scope, name='foo', module_path=['foo'])

    # Ensure the module is imported correctly
    assert 'foo' in scope
    assert isinstance(scope['foo'], type(ImportReplacer))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

../../../dev F                                                           [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_import_module _________________________

    def test_valid_case_import_module():
        scope = globals()
        replacer = ImportReplacer(scope=scope, name='foo', module_path=['foo'])
    
        # Ensure the module is imported correctly
        assert 'foo' in scope
>       assert isinstance(scope['foo'], type(ImportReplacer))

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportReplacer__import_0_test_valid_case_import_module.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/lazy/lazy_import.py:182: in __getattribute__
    obj = object.__getattribute__(self, '_resolve')()
pytutils/pytutils/lazy/lazy_import.py:159: in _resolve
    obj = factory(self, scope, name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportReplacer object at 0x7efc7f401480>
scope = {'@py_builtins': <module 'builtins' (built-in)>, '@pytest_ar': <module '_pytest.assertion.rewrite' from '/usr/local/li...ass 'AssertionError'>, 'AttributeError': <class 'AttributeError'>, 'BaseException': <class 'BaseException'>, ...}, ...}
name = 'foo'

    def _import(self, scope, name):
        children = object.__getattribute__(self, '_import_replacer_children')
        member = object.__getattribute__(self, '_member')
        module_path = object.__getattribute__(self, '_module_path')
        module_python_path = '.'.join(module_path)
        if member is not None:
            module = __import__(module_python_path, scope, scope, [member], level=0)
            return getattr(module, member)
        else:
>           module = __import__(module_python_path, scope, scope, [], level=0)
E           ModuleNotFoundError: No module named 'foo'

pytutils/pytutils/lazy/lazy_import.py:277: ModuleNotFoundError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-zt7649_4'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-9vqekn_3'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-xvszu3qf'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_case_import_module - ModuleNotFoundError: No...
======================== 1 failed, 3 warnings in 0.06s =========================
"""