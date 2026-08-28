
import pytest
from youtube_dl.extractor.nrk import NRKRadioPodkastIE

@pytest.fixture(scope="module")
def extractor():
    return NRKRadioPodkastIE()


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKRadioPodkastIE__real_extract_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

extractor = <youtube_dl.extractor.nrk.NRKRadioPodkastIE object at 0x7f5e513dbe50>

    def test_valid_case(extractor):
        url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
        info_dict = extractor._real_extract(url)
        assert isinstance(info_dict, dict), "Expected a dictionary"
        assert 'id' in info_dict, "Expected 'id' in info_dict"
>       assert info_dict['id'] == 'MUHH48000314AA', f"Expected id to be MUHH48000314AA, but got {info_dict['id']}"
E       AssertionError: Expected id to be MUHH48000314AA, but got l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8
E       assert 'l_96f4f1b0-d...-b0de54fe6af8' == 'MUHH48000314AA'
E         
E         - MUHH48000314AA
E         + l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKRadioPodkastIE__real_extract_0.py:14: AssertionError
________________________________ test_edge_case ________________________________

extractor = <youtube_dl.extractor.nrk.NRKRadioPodkastIE object at 0x7f5e513dbe50>

    def test_edge_case(extractor):
        url = 'https://radio.nrk.no/podcast/ulrikkes_univers/l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8'
        info_dict = extractor._real_extract(url)
        assert isinstance(info_dict, dict), "Expected a dictionary"
        assert 'id' in info_dict, "Expected 'id' in info_dict"
>       assert info_dict['id'] == 'MUHH48000314AA', f"Expected id to be MUHH48000314AA, but got {info_dict['id']}"
E       AssertionError: Expected id to be MUHH48000314AA, but got l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8
E       assert 'l_96f4f1b0-d...-b0de54fe6af8' == 'MUHH48000314AA'
E         
E         - MUHH48000314AA
E         + l_96f4f1b0-de54-4e6a-b4f1-b0de54fe6af8

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKRadioPodkastIE__real_extract_0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKRadioPodkastIE__real_extract_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKRadioPodkastIE__real_extract_0.py::test_edge_case
============================== 2 failed in 0.54s ===============================
"""