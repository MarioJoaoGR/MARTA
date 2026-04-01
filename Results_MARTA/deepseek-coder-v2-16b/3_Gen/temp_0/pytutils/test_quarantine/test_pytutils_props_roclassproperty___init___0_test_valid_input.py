
from pytutils.props import roclassproperty
import unittest

class TestRoClassProperty(unittest.TestCase):
    def setUp(self):
        self.my_prop = roclassproperty(lambda cls: "This is a read-only property")

    def test_valid_input(self):
        class MyClass:
            prop = self.my_prop

        obj = MyClass()
        self.assertEqual(obj.prop, "This is a read-only property")
        
        with self.assertRaises(AttributeError):
            obj.prop = "Attempt to modify the property"

if __name__ == '__main__':
    unittest.main()

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
_____________________ TestRoClassProperty.test_valid_input _____________________

self = <Test4DT_tests.test_pytutils_props_roclassproperty___init___0_test_valid_input.TestRoClassProperty testMethod=test_valid_input>

    def test_valid_input(self):
        class MyClass:
            prop = self.my_prop
    
        obj = MyClass()
        self.assertEqual(obj.prop, "This is a read-only property")
    
>       with self.assertRaises(AttributeError):
E       AssertionError: AttributeError not raised

pytutils/Test4DT_tests/test_pytutils_props_roclassproperty___init___0_test_valid_input.py:16: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-b5y2vno2'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-k7nfmq8b'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-sd4zyfz0'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::TestRoClassProperty::test_valid_input - AssertionError:...
======================== 1 failed, 3 warnings in 0.09s =========================
"""