
import pytest
import itertools
from youtube_dl.downloader.f4m import build_fragments_list

@pytest.mark.parametrize("boot_info, expected", [
    ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)]),
    ({'segments': [{'segment_run': [(1, 4294967295), (2, 4294967295)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': True}, [(1, 1), (1, 2), (2, 1), (2, 2)]),
    ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)])
])
def test_build_fragments_list(boot_info, expected):
    assert build_fragments_list(boot_info) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________ test_build_fragments_list[boot_info0-expected0] ________________

boot_info = {'fragments': [{'fragments': [{'first': 1}]}], 'live': False, 'segments': [{'segment_run': [(1, 5), (2, 3)]}]}
expected = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), ...]

    @pytest.mark.parametrize("boot_info, expected", [
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)]),
        ({'segments': [{'segment_run': [(1, 4294967295), (2, 4294967295)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': True}, [(1, 1), (1, 2), (2, 1), (2, 2)]),
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)])
    ])
    def test_build_fragments_list(boot_info, expected):
>       assert build_fragments_list(boot_info) == expected
E       assert [(1, 1), (1, ..., (2, 6), ...] == [(1, 1), (1, ..., (2, 1), ...]
E         
E         At index 5 diff: (2, 6) != (2, 1)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py:12: AssertionError
_______________ test_build_fragments_list[boot_info1-expected1] ________________

boot_info = {'fragments': [{'fragments': [{'first': 1}]}], 'live': True, 'segments': [{'segment_run': [(1, 4294967295), (2, 4294967295)]}]}
expected = [(1, 1), (1, 2), (2, 1), (2, 2)]

    @pytest.mark.parametrize("boot_info, expected", [
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)]),
        ({'segments': [{'segment_run': [(1, 4294967295), (2, 4294967295)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': True}, [(1, 1), (1, 2), (2, 1), (2, 2)]),
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)])
    ])
    def test_build_fragments_list(boot_info, expected):
>       assert build_fragments_list(boot_info) == expected
E       assert [(2, 3), (2, 4)] == [(1, 1), (1, ...2, 1), (2, 2)]
E         
E         At index 0 diff: (2, 3) != (1, 1)
E         Right contains 2 more items, first extra item: (2, 1)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py:12: AssertionError
_______________ test_build_fragments_list[boot_info2-expected2] ________________

boot_info = {'fragments': [{'fragments': [{'first': 1}]}], 'live': False, 'segments': [{'segment_run': [(1, 5), (2, 3)]}]}
expected = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), ...]

    @pytest.mark.parametrize("boot_info, expected", [
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)]),
        ({'segments': [{'segment_run': [(1, 4294967295), (2, 4294967295)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': True}, [(1, 1), (1, 2), (2, 1), (2, 2)]),
        ({'segments': [{'segment_run': [(1, 5), (2, 3)]}], 'fragments': [{'fragments': [{'first': 1}]}], 'live': False}, [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3)])
    ])
    def test_build_fragments_list(boot_info, expected):
>       assert build_fragments_list(boot_info) == expected
E       assert [(1, 1), (1, ..., (2, 6), ...] == [(1, 1), (1, ..., (2, 1), ...]
E         
E         At index 5 diff: (2, 6) != (2, 1)
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py::test_build_fragments_list[boot_info0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py::test_build_fragments_list[boot_info1-expected1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_build_fragments_list_0.py::test_build_fragments_list[boot_info2-expected2]
============================== 3 failed in 0.57s ===============================
"""