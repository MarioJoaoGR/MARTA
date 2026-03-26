
import pytest
import collections
from pytutils.trees import tree

@pytest.fixture(scope="module")
def nested_tree():
    return tree()

def test_valid_input(nested_tree):
    assert isinstance(nested_tree, collections.defaultdict)
    assert isinstance(nested_tree['key'], collections.defaultdict)
    assert len(nested_tree) == 0

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
_______________________________ test_valid_input _______________________________

nested_tree = defaultdict(<function tree at 0x7f2d872bce00>, {'key': defaultdict(<function tree at 0x7f2d872bce00>, {})})

    def test_valid_input(nested_tree):
        assert isinstance(nested_tree, collections.defaultdict)
        assert isinstance(nested_tree['key'], collections.defaultdict)
>       assert len(nested_tree) == 0
E       AssertionError: assert 1 == 0
E        +  where 1 = len(defaultdict(<function tree at 0x7f2d872bce00>, {'key': defaultdict(<function tree at 0x7f2d872bce00>, {})}))

pytutils/Test4DT_tests/test_pytutils_trees_tree_0_test_valid_input.py:13: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-di3k4fbt'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-tx65lr53'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-x6fqz4ho'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - AssertionError: assert 1 == 0
======================== 1 failed, 3 warnings in 0.05s =========================
"""