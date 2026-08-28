
import pytest
from youtube_dl.socks import sockssocket



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_sockssocket_instantiation ________________________

    def test_sockssocket_instantiation():
>       sock = socksocket()
E       NameError: name 'socksocket' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py:6: NameError
____________________ test_socks5_auth_no_acceptable_method _____________________

    def test_socks5_auth_no_acceptable_method():
>       sock = socksocket()
E       NameError: name 'socksocket' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py:10: NameError
__________________________ test_socks5_auth_user_pass __________________________

    def test_socks5_auth_user_pass():
>       sock = socksocket()
E       NameError: name 'socksocket' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py:16: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py::test_sockssocket_instantiation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py::test_socks5_auth_no_acceptable_method
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_socks_sockssocket__socks5_auth_0.py::test_socks5_auth_user_pass
============================== 3 failed in 0.56s ===============================
"""