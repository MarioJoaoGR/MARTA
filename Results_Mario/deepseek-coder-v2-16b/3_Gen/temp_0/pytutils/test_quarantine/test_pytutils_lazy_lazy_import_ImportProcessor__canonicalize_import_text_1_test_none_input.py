
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer

def test_none_input():
    processor = ImportProcessor()
    result = processor._canonicalize_import_text(None)
    assert result == []

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
_______________________________ test_none_input ________________________________

    def test_none_input():
        processor = ImportProcessor()
>       result = processor._canonicalize_import_text(None)

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_1_test_none_input.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7f34a657caf0>
text = None

    def _canonicalize_import_text(self, text):
        """Take a list of imports, and split it into regularized form.
    
        This is meant to take regular import text, and convert it to
        the forms that the rest of the converters prefer.
        """
        out = []
        cur = None
        continuing = False
    
>       for line in text.split('\n'):
E       AttributeError: 'NoneType' object has no attribute 'split'

pytutils/pytutils/lazy/lazy_import.py:425: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-g2b4l0by'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-ghhhn8x1'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-87oyqqzw'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input - AttributeError: 'NoneType' object has...
======================== 1 failed, 3 warnings in 0.08s =========================
"""