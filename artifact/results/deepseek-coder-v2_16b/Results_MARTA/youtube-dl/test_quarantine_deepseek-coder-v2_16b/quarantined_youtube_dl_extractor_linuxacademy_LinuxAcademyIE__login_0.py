
import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

@pytest.fixture(scope="module")
def linuxacademy():
    return LinuxAcademyIE()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_credentials ____________________________

linuxacademy = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f91dda63910>

    def test_valid_credentials(linuxacademy):
>       with pytest.monkeypatch.context() as m:
E       AttributeError: module 'pytest' has no attribute 'monkeypatch'. Did you mean: 'MonkeyPatch'?

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:10: AttributeError
___________________________ test_missing_credentials ___________________________

linuxacademy = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f91dda63910>

    def test_missing_credentials(linuxacademy):
>       with pytest.monkeypatch.context() as m:
E       AttributeError: module 'pytest' has no attribute 'monkeypatch'. Did you mean: 'MonkeyPatch'?

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:23: AttributeError
___________________________ test_invalid_credentials ___________________________

linuxacademy = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f91dda63910>

    def test_invalid_credentials(linuxacademy):
>       with pytest.monkeypatch.context() as m:
E       AttributeError: module 'pytest' has no attribute 'monkeypatch'. Did you mean: 'MonkeyPatch'?

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:34: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_valid_credentials
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_missing_credentials
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_invalid_credentials
============================== 3 failed in 0.55s ===============================
"""