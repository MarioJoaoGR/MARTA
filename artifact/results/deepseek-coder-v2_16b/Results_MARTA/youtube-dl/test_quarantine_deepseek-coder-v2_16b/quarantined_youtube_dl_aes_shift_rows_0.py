
import pytest
from youtube_dl.aes import shift_rows


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_shift_rows_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_output = [0, 5, 10, 15, 1, 6, 11, 12, 2, 7, 8, 13, 3, 4, 9, 14]
>       assert shift_rows(input_data) == expected_output
E       assert [0, 5, 10, 15, 4, 9, ...] == [0, 5, 10, 15, 1, 6, ...]
E         
E         At index 4 diff: 4 != 1
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_shift_rows_0.py:8: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        input_data = []
>       assert shift_rows(input_data) == []

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_shift_rows_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

data = []

    def shift_rows(data):
        data_shifted = []
        for column in range(4):
            for row in range(4):
>               data_shifted.append(data[((column + row) & 0b11) * 4 + row])
E               IndexError: list index out of range

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/aes.py:338: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_shift_rows_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_shift_rows_0.py::test_edge_case
============================== 2 failed in 0.56s ===============================
"""