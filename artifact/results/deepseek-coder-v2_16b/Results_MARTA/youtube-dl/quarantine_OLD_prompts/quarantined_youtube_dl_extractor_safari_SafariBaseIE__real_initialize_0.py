
import pytest
from unittest.mock import patch, mock_open
from youtube_dl.extractor.safari import SafariBaseIE

class TestSafariBaseIE:
    @pytest.mark.parametrize("netrc_content, expected", [
        ("""machine safari
            login your_login
            password your_password""", True),
        ("machine other_machine\nlogin other_login\npassword other_password", False)
    ])
    def test_login(self, monkeypatch, netrc_content, expected):
        with patch('builtins.open', mock_open(read_data=netrc_content)):
            safari_ie = SafariBaseIE()
            assert safari_ie._login() == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ TestSafariBaseIE.test_login[machine safari\n            login your_login\n            password your_password-True] _

self = <test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.TestSafariBaseIE object at 0x7f9fad587d90>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f9fad3f41c0>
netrc_content = 'machine safari\n            login your_login\n            password your_password'
expected = True

    @pytest.mark.parametrize("netrc_content, expected", [
        ("""machine safari
            login your_login
            password your_password""", True),
        ("machine other_machine\nlogin other_login\npassword other_password", False)
    ])
    def test_login(self, monkeypatch, netrc_content, expected):
        with patch('builtins.open', mock_open(read_data=netrc_content)):
            safari_ie = SafariBaseIE()
>           assert safari_ie._login() == expected
E           assert None == True
E            +  where None = _login()
E            +    where _login = <youtube_dl.extractor.safari.SafariBaseIE object at 0x7f9fad441f60>._login

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.py:16: AssertionError
_ TestSafariBaseIE.test_login[machine other_machine\nlogin other_login\npassword other_password-False] _

self = <test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.TestSafariBaseIE object at 0x7f9fad587df0>
monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f9fad443910>
netrc_content = 'machine other_machine\nlogin other_login\npassword other_password'
expected = False

    @pytest.mark.parametrize("netrc_content, expected", [
        ("""machine safari
            login your_login
            password your_password""", True),
        ("machine other_machine\nlogin other_login\npassword other_password", False)
    ])
    def test_login(self, monkeypatch, netrc_content, expected):
        with patch('builtins.open', mock_open(read_data=netrc_content)):
            safari_ie = SafariBaseIE()
>           assert safari_ie._login() == expected
E           assert None == False
E            +  where None = _login()
E            +    where _login = <youtube_dl.extractor.safari.SafariBaseIE object at 0x7f9fad4a0820>._login

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.py::TestSafariBaseIE::test_login[machine safari\n            login your_login\n            password your_password-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariBaseIE__real_initialize_0.py::TestSafariBaseIE::test_login[machine other_machine\nlogin other_login\npassword other_password-False]
============================== 2 failed in 0.58s ===============================
"""