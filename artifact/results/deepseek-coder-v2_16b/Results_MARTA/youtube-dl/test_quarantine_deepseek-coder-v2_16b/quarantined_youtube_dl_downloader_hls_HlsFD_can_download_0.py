
import pytest
from youtube_dl.downloader.hls import HlsFD



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_no_encryption _________________________

    def test_valid_case_no_encryption():
        manifest_content = """#EXTM3U
        #EXT-X-VERSION:3
        #EXT-X-TARGETDURATION:10
        #EXTINF:9.021,extra_fragment.ts"""
    
        info_dict = {
            'url': 'http://example.com/manifest.m3u8',
            'is_live': False
        }
    
>       hls_fd = HlsFD()
E       TypeError: FileDownloader.__init__() missing 2 required positional arguments: 'ydl' and 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py:16: TypeError
________________________ test_edge_case_empty_manifest _________________________

    def test_edge_case_empty_manifest():
        manifest_content = ''
    
        info_dict = {
            'url': 'http://example.com/manifest.m3u8',
            'is_live': False
        }
    
>       hls_fd = HlsFD()
E       TypeError: FileDownloader.__init__() missing 2 required positional arguments: 'ydl' and 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py:28: TypeError
___________________________ test_invalid_encryption ____________________________

    def test_invalid_encryption():
        manifest_content = """#EXTM3U
        #EXT-X-VERSION:3
        #EXT-X-KEY:METHOD=AES-128,URI="http://example.com/key"
        #EXT-X-BYTERANGE:1000@0"""
    
        info_dict = {
            'url': 'http://example.com/manifest.m3u8',
            'is_live': False
        }
    
>       hls_fd = HlsFD()
E       TypeError: FileDownloader.__init__() missing 2 required positional arguments: 'ydl' and 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py:43: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py::test_valid_case_no_encryption
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py::test_edge_case_empty_manifest
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_hls_HlsFD_can_download_0.py::test_invalid_encryption
============================== 3 failed in 0.57s ===============================
"""