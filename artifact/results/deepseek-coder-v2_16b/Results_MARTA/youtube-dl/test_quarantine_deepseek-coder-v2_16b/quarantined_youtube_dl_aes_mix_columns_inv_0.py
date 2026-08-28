
import pytest
from youtube_dl.aes import mix_columns_inv

# Test default matrix case

# Test custom matrix case
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_mix_columns_inv_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_mix_columns_inv_default_matrix ______________________

    def test_mix_columns_inv_default_matrix():
        data = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        result = mix_columns_inv(data)
>       assert result == data
E       assert [49, 42, 63, 32, 77, 110, ...] == [3, 4, 5, 6, 7, 8, ...]
E         
E         At index 0 diff: 49 != 3
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_mix_columns_inv_0.py:9: AssertionError
______________________ test_mix_columns_inv_custom_matrix ______________________

    def test_mix_columns_inv_custom_matrix():
        data = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        custom_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
>       result = mix_columns_inv(data, custom_matrix)
E       TypeError: mix_columns_inv() takes 1 positional argument but 2 were given

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_mix_columns_inv_0.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_mix_columns_inv_0.py::test_mix_columns_inv_default_matrix
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_mix_columns_inv_0.py::test_mix_columns_inv_custom_matrix
============================== 2 failed in 0.57s ===============================
"""