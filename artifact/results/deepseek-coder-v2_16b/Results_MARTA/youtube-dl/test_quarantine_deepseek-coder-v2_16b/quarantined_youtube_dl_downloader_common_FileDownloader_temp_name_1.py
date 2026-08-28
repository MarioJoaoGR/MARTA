
import pytest
from youtube_dl.downloader.common import FileDownloader
from youtube_dl import YoutubeDL
import os


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_temp_name_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_temp_name_default ____________________________

    def test_temp_name_default():
        ydl = YoutubeDL()
        params = {}
        downloader = FileDownloader(ydl, params)
        filename = "samplefile"
>       assert downloader.temp_name(filename) == f"{filename}.part"
E       AssertionError: assert 'samplefile' == 'samplefile.part'
E         
E         - samplefile.part
E         ?           -----
E         + samplefile

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_temp_name_1.py:12: AssertionError
______________________ test_temp_name_with_existing_file _______________________

    def test_temp_name_with_existing_file():
        ydl = YoutubeDL()
        params = {}
        downloader = FileDownloader(ydl, params)
        filename = "samplefile"
>       open(filename, 'a').close()  # Create an empty file named samplefile
E       IsADirectoryError: [Errno 21] Is a directory: 'samplefile'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_temp_name_1.py:19: IsADirectoryError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_temp_name_1.py::test_temp_name_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_temp_name_1.py::test_temp_name_with_existing_file
============================== 2 failed in 0.58s ===============================
"""