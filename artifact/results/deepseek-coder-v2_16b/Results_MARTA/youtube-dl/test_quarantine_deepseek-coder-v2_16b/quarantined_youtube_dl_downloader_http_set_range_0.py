
import pytest
from youtube_dl.downloader.http import set_range
import requests

# Test 1: Setting a range from byte 100 to byte 200
def test_set_range_with_start_and_end():
    req = requests.Request('GET', 'http://example.com/file')
    set_range(req, 100, 200)
    prepared_request = req.prepare()
    assert prepared_request.headers['Range'] == 'bytes=100-200'

# Test 2: Requesting the last 500 bytes of a file
def test_set_range_with_only_start():
    req = requests.Request('GET', 'http://example.com/file')
    set_range(req, -500)
    prepared_request = req.prepare()
    assert prepared_request.headers['Range'] == 'bytes=-500'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_______ ERROR collecting test_youtube_dl_downloader_http_set_range_0.py ________
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_http_set_range_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_http_set_range_0.py:3: in <module>
    from youtube_dl.downloader.http import set_range
E   ImportError: cannot import name 'set_range' from 'youtube_dl.downloader.http' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/downloader/http.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_http_set_range_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.61s ===============================
"""