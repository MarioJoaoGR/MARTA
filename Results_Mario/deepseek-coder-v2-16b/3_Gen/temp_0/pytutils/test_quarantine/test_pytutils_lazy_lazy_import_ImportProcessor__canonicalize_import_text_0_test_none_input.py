
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
import pytest

def test_none_input():
    processor = ImportProcessor()
    assert processor._canonicalize_import_text(None) == []

def test_invalid_input():
    processor = ImportProcessor()
    with pytest.raises(TypeError):
        processor._canonicalize_import_text("invalid input")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /dev
configfile: null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

../../../dev FF                                                          [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        processor = ImportProcessor()
>       assert processor._canonicalize_import_text(None) == []

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0_test_none_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7fdce9b67070>
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
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        processor = ImportProcessor()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__canonicalize_import_text_0_test_none_input.py:11: Failed
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-27v_hb64'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-nke30pc0'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-znu5w34f'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input - AttributeError: 'NoneType' object has...
FAILED ../../../dev/::test_invalid_input - Failed: DID NOT RAISE <class 'Type...
======================== 2 failed, 3 warnings in 0.06s =========================
"""