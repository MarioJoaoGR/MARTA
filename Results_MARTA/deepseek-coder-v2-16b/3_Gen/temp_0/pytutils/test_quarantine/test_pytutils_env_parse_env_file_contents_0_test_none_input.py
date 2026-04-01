
import pytest
from unittest.mock import patch
import re
import typing
from pytutils.env import parse_env_file_contents

@pytest.mark.parametrize("lines", [None])
def test_none_input(lines):
    with patch('pytutils.env.re') as mock_re:
        mock_re.match.side_effect = lambda pattern, string: None if string == '' else re.match(pattern, string)
        gen = parse_env_file_contents(lines)
        assert list(gen) == []

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
____________________________ test_none_input[None] _____________________________

lines = None

    @pytest.mark.parametrize("lines", [None])
    def test_none_input(lines):
        with patch('pytutils.env.re') as mock_re:
            mock_re.match.side_effect = lambda pattern, string: None if string == '' else re.match(pattern, string)
            gen = parse_env_file_contents(lines)
>           assert list(gen) == []

pytutils/Test4DT_tests/test_pytutils_env_parse_env_file_contents_0_test_none_input.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

lines = None

    def parse_env_file_contents(lines: typing.Iterable[str] = None) -> typing.Generator[typing.Tuple[str, str], None, None]:
        """
        Parses env file content.
    
        From honcho.
    
        >>> lines = ['TEST=${HOME}/yeee', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']
        >>> load_env_file(lines, write_environ=dict())
        OrderedDict([('TEST', '.../yeee'),
                 ('THISIS', '.../a/test'),
                 ('YOLO',
                  '.../swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')])
    
        """
>       for line in lines:
E       TypeError: 'NoneType' object is not iterable

pytutils/pytutils/env.py:27: TypeError
=============================== warnings summary ===============================
../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:477: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/nodeids: [Errno 13] Permission denied: '/dev/pytest-cache-files-obldywoo'
    config.cache.set("cache/nodeids", sorted(self.cached_nodeids))

../../../usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429
  /usr/local/lib/python3.11/site-packages/_pytest/cacheprovider.py:429: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/lastfailed: [Errno 13] Permission denied: '/dev/pytest-cache-files-6tzr_2c0'
    config.cache.set("cache/lastfailed", self.lastfailed)

../../../usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51
  /usr/local/lib/python3.11/site-packages/_pytest/stepwise.py:51: PytestCacheWarning: could not create cache path /dev/.pytest_cache/v/cache/stepwise: [Errno 13] Permission denied: '/dev/pytest-cache-files-_poq9ew3'
    session.config.cache.set(STEPWISE_CACHE_DIR, [])

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED ../../../dev/::test_none_input[None] - TypeError: 'NoneType' object is...
======================== 1 failed, 3 warnings in 0.05s =========================
"""