
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_edge_case():
    processor = ImportProcessor(lazy_import_class=None)
    assert isinstance(processor._lazy_import_class, ImportReplacer), f"Expected _lazy_import_class to be an instance of ImportReplacer but got {type(processor._lazy_import_class)}"

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
________________________________ test_edge_case ________________________________

    def test_edge_case():
        processor = ImportProcessor(lazy_import_class=None)
>       assert isinstance(processor._lazy_import_class, ImportReplacer), f"Expected _lazy_import_class to be an instance of ImportReplacer but got {type(processor._lazy_import_class)}"
E       AssertionError: Expected _lazy_import_class to be an instance of ImportReplacer but got <class 'type'>
E       assert False
E        +  where False = isinstance(<class 'pytutils.lazy.lazy_import.ImportReplacer'>, ImportReplacer)
E        +    where <class 'pytutils.lazy.lazy_import.ImportReplacer'> = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f288a970610>._lazy_import_class

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_imports_2_test_edge_case.py:6: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-tm7a593y'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-tzgs4bjk'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-09_7l2bc'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case - AssertionError: Expected _lazy_import_...
======================== 1 failed, 3 warnings in 0.08s =========================
"""