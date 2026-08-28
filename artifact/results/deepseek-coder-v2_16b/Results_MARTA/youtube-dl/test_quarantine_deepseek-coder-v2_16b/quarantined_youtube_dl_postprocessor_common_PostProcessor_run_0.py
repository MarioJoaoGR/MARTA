
import pytest
from youtube_dl.postprocessor.common import PostProcessor, PostProcessingError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_postprocessor_common_PostProcessor_run_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        post_processor = PostProcessor()
        information = {'filepath': None}
>       with pytest.raises(PostProcessingError):
E       Failed: DID NOT RAISE <class 'youtube_dl.utils.PostProcessingError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_postprocessor_common_PostProcessor_run_0.py:8: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        post_processor = PostProcessor()
        information = {'filepath': 'invalid_path'}
>       with pytest.raises(PostProcessingError):
E       Failed: DID NOT RAISE <class 'youtube_dl.utils.PostProcessingError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_postprocessor_common_PostProcessor_run_0.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_postprocessor_common_PostProcessor_run_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_postprocessor_common_PostProcessor_run_0.py::test_invalid_input
============================== 2 failed in 0.55s ===============================
"""