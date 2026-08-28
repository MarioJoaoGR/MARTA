
import pytest
from youtube_dl.aes import key_schedule_core, rotate, sub_bytes, SBOX, RCON


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_key_schedule_core_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        data = [1, 2, 3]
        rcon_iteration = 0
        result = key_schedule_core(data, rcon_iteration)
        expected = [(SBOX[1] ^ RCON[0]), SBOX[2], 3]
>       assert result == expected
E       assert [250, 123, 124] == [241, 119, 3]
E         
E         At index 0 diff: 250 != 241
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_key_schedule_core_0.py:10: AssertionError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        with pytest.raises(TypeError):
            key_schedule_core(None, 0)
        with pytest.raises(TypeError):
>           key_schedule_core([], 0)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_key_schedule_core_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/aes.py:294: in key_schedule_core
    data = rotate(data)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

data = []

    def rotate(data):
>       return data[1:] + [data[0]]
E       IndexError: list index out of range

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/aes.py:290: IndexError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_key_schedule_core_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_aes_key_schedule_core_0.py::test_edge_case
============================== 2 failed in 0.57s ===============================
"""