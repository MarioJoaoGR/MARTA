
import os
import typing
import collections
import pytest
from pytutils.env import load_env_file

@pytest.fixture(scope="module")
def setup():
    # Mocking os.environ to avoid actual environment variable expansion during tests
    original_environ = os.environ
    os.environ = {}
    yield {"lines": ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']}
    # Restore the original environment variables after the test
    os.environ = original_environ

def test_valid_input(setup):
    lines = setup["lines"]
    result = load_env_file(lines, write_environ=dict())
    
    expected = collections.OrderedDict([
        ('TEST', f'{os.path.expanduser("~")}/yeee-{os.getenv("PATH", "")}'),
        ('THISIS', os.path.expanduser("~/a/test")),
        ('YOLO', os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))
    ])
    
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
_______________________________ test_valid_input _______________________________

setup = {'lines': ['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']}

    def test_valid_input(setup):
        lines = setup["lines"]
        result = load_env_file(lines, write_environ=dict())
    
        expected = collections.OrderedDict([
            ('TEST', f'{os.path.expanduser("~")}/yeee-{os.getenv("PATH", "")}'),
            ('THISIS', os.path.expanduser("~/a/test")),
            ('YOLO', os.path.expanduser("~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST"))
        ])
    
>       assert result == expected
E       AssertionError: assert OrderedDict([..._NOT_EXIST')]) == OrderedDict([..._NOT_EXIST')])
E         
E         Omitting 2 identical items, use -vv to show
E         Differing items:
E         {'TEST': '${HOME}/yeee-$PATH'} != {'TEST': '/home/joaovitorino/yeee-'}
E         Use -v to get more diff

pytutils/Test4DT_tests/test_pytutils_env_load_env_file_2_test_valid_input.py:27: AssertionError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-rj85tsew'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-6tkagcjt'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-0jr6gb5o'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_valid_input - AssertionError: assert OrderedDict([...
======================== 1 failed, 3 warnings in 0.06s =========================
"""