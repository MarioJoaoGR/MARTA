
import pytest
from youtube_dl.socks import InvalidVersionError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_InvalidVersionError___init___0.py F [100%]

=================================== FAILURES ===================================
__________________________ test_invalid_version_error __________________________

    def test_invalid_version_error():
        expected_version = 0x12
        got_version = 0x34
    
        with pytest.raises(InvalidVersionError) as excinfo:
            raise InvalidVersionError(expected_version, got_version)
    
>       assert str(excinfo.value) == 'Invalid response version from server. Expected 18 got 52'
E       AssertionError: assert '[Errno 0] In...ted 12 got 34' == 'Invalid resp...ted 18 got 52'
E         
E         - Invalid response version from server. Expected 18 got 52
E         ?                                                 ^     ^^
E         + [Errno 0] Invalid response version from server. Expected 12 got 34
E         ? ++++++++++                                                ^     ^^

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_InvalidVersionError___init___0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_InvalidVersionError___init___0.py::test_invalid_version_error
============================== 1 failed in 1.02s ===============================
"""