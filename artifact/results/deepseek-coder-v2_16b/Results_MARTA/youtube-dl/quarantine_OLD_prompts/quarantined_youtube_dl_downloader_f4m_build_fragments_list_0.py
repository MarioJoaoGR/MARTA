
import pytest
from unittest.mock import patch
from youtube_dl.downloader.f4m import build_fragments_list


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        boot_info = {
            'segments': [{'segment_run': [(1, 5), (2, 3)]}],
            'fragments': [{'fragments': [{'first': 1}]}],
            'live': False
        }
>       assert build_fragments_list(boot_info) == [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)]
E       assert [(1, 1), (1, ..., (2, 6), ...] == [(1, 1), (1, ..., (2, 1), ...]
E         
E         At index 5 diff: (2, 6) != (2, 1)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py:12: AssertionError
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        boot_info = {'segments': 'invalid', 'fragments': 'invalid'}
        with pytest.raises(KeyError):
>           build_fragments_list(boot_info)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

boot_info = {'fragments': 'invalid', 'segments': 'invalid'}

    def build_fragments_list(boot_info):
        """ Return a list of (segment, fragment) for each fragment in the video """
        res = []
        segment_run_table = boot_info['segments'][0]
>       fragment_run_entry_table = boot_info['fragments'][0]['fragments']
E       TypeError: string indices must be integers

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/downloader/f4m.py:192: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py::test_error_handling
============================== 2 failed in 0.57s ===============================
"""