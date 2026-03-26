
from pytutils.lazy.lazy_import import ImportProcessor, ImportReplacer
import pytest

def test_none_input():
    processor = ImportProcessor()
    from_str = None
    
    with pytest.raises(ValueError):
        processor._convert_from_str(from_str)

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
        from_str = None
    
        with pytest.raises(ValueError):
>           processor._convert_from_str(from_str)

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_import_ImportProcessor__convert_from_str_3_test_none_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <pytutils.lazy.lazy_import.ImportProcessor object at 0x7fef4b544100>
from_str = None

    def _convert_from_str(self, from_str):
        """This converts a 'from foo import bar' string into an import map.
    
        :param from_str: The import string to process
        """
>       if not from_str.startswith('from '):
E       AttributeError: 'NoneType' object has no attribute 'startswith'

pytutils/pytutils/lazy/lazy_import.py:390: AttributeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-ccxjnpjw'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-7son4yh2'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-iru197_t'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input - AttributeError: 'NoneType' object has...
======================== 1 failed, 3 warnings in 0.07s =========================
"""