
import pytest
from youtube_dl import YTDL
from file_downloader import FileDownloader

# Test 1: Initialize FileDownloader with valid parameters
def test_file_downloader_init():
    ydl = YTDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    assert isinstance(downloader, FileDownloader), "FileDownloader instance creation failed"
    assert downloader.params == params, "Parameters not correctly set in FileDownloader instance"

# Test 2: Report file already downloaded scenario
def test_report_file_already_downloaded():
    ydl = YTDL()
    params = {
        'verbose': True,
        'ratelimit': 10240,
        'retries': 3,
        'buffersize': 8192,
        'test': False
    }
    downloader = FileDownloader(ydl, params)
    file_name = "somefile.mp4"
    with pytest.raises(SystemExit):
        downloader.report_file_already_downloaded(file_name)

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
_ ERROR collecting test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py:3: in <module>
    from youtube_dl import YTDL
E   ImportError: cannot import name 'YTDL' from 'youtube_dl' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/__init__.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.62s ===============================
"""