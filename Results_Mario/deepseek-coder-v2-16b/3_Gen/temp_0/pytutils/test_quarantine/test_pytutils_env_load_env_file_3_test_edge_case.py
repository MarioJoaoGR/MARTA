
import pytest
from pytutils.env import load_env_file, parse_env_file_contents, expand
import os
import collections
import typing

def test_edge_case():
    # Test None input
    with pytest.raises(TypeError):
        load_env_file(None)
    
    # Test empty list input
    assert load_env_file([]) == collections.OrderedDict()
    
    # Test boundary value input (one line)
    lines = ['TEST=${HOME}/yeee-$PATH']
    result = load_env_file(lines)
    expected = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee-$PATH'))])
    assert result == expected

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
        # Test None input
        with pytest.raises(TypeError):
            load_env_file(None)
    
        # Test empty list input
        assert load_env_file([]) == collections.OrderedDict()
    
        # Test boundary value input (one line)
        lines = ['TEST=${HOME}/yeee-$PATH']
        result = load_env_file(lines)
        expected = collections.OrderedDict([('TEST', os.path.expanduser('${HOME}/yeee-$PATH'))])
>       assert result == expected
E       AssertionError: assert OrderedDict([.../sbin:/bin')]) == OrderedDict([...yeee-$PATH')])
E         
E         Differing items:
E         {'TEST': '/home/joaovitorino/yeee-/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'} != {'TEST': '${HOME}/yeee-$PATH'}
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_env_load_env_file_3_test_edge_case.py:20: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-nfs9rsho'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-bg9717m1'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-o4ci74ya'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_edge_case - AssertionError: assert OrderedDict([.....
======================== 1 failed, 3 warnings in 0.07s =========================
"""