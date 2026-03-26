
import re
import pytest
from flutes.network import _extract_google_drive_file_id

@pytest.mark.parametrize("url, expected", [
    ('https://example.com/wrong/url', ''),
    ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing', '1aBcD2eF3gHiJkLmNoPqRsT'),
    ('https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT', '1aBcD2eF3gHiJkLmNoPqRsT')
])
def test_extract_google_drive_file_id(url, expected):
    assert _extract_google_drive_file_id(url) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
______ test_extract_google_drive_file_id[https://example.com/wrong/url-] _______

url = 'https://example.com/wrong/url', expected = ''

    @pytest.mark.parametrize("url, expected", [
        ('https://example.com/wrong/url', ''),
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing', '1aBcD2eF3gHiJkLmNoPqRsT'),
        ('https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT', '1aBcD2eF3gHiJkLmNoPqRsT')
    ])
    def test_extract_google_drive_file_id(url, expected):
>       assert _extract_google_drive_file_id(url) == expected
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py:12: AssertionError
_ test_extract_google_drive_file_id[https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT-1aBcD2eF3gHiJkLmNoPqRsT] _

url = 'https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT'
expected = '1aBcD2eF3gHiJkLmNoPqRsT'

    @pytest.mark.parametrize("url, expected", [
        ('https://example.com/wrong/url', ''),
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing', '1aBcD2eF3gHiJkLmNoPqRsT'),
        ('https://drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT', '1aBcD2eF3gHiJkLmNoPqRsT')
    ])
    def test_extract_google_drive_file_id(url, expected):
>       assert _extract_google_drive_file_id(url) == expected
E       AssertionError: assert 'tps:' == '1aBcD2eF3gHiJkLmNoPqRsT'
E         
E         - 1aBcD2eF3gHiJkLmNoPqRsT
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py::test_extract_google_drive_file_id[https:/example.com/wrong/url-]
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_invalid_input_wrong_domain.py::test_extract_google_drive_file_id[https:/drive.google.com/drive/folders/1aBcD2eF3gHiJkLmNoPqRsT-1aBcD2eF3gHiJkLmNoPqRsT]
========================= 2 failed, 1 passed in 0.11s ==========================
"""