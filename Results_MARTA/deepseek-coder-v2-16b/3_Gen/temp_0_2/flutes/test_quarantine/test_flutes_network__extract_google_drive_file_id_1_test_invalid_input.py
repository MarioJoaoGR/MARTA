
import re
import pytest
from flutes.network import _extract_google_drive_file_id

@pytest.mark.parametrize("input_url, expected", [
    ('https://drive.google.com/wrongpath', ''),
    ('https://drive.google.com/file/d/', ''),
    ('https://drive.google.com/open?id=', ''),
    ('https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT', ''),
    ('https://drive.google.com/file/d/invalid_id', '')
])
def test_invalid_input(input_url, expected):
    assert _extract_google_drive_file_id(input_url) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py F [ 20%]
.FFF                                                                     [100%]

=================================== FAILURES ===================================
___________ test_invalid_input[https://drive.google.com/wrongpath-] ____________

input_url = 'https://drive.google.com/wrongpath', expected = ''

    @pytest.mark.parametrize("input_url, expected", [
        ('https://drive.google.com/wrongpath', ''),
        ('https://drive.google.com/file/d/', ''),
        ('https://drive.google.com/open?id=', ''),
        ('https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT', ''),
        ('https://drive.google.com/file/d/invalid_id', '')
    ])
    def test_invalid_input(input_url, expected):
>       assert _extract_google_drive_file_id(input_url) == expected
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py:14: AssertionError
____________ test_invalid_input[https://drive.google.com/open?id=-] ____________

input_url = 'https://drive.google.com/open?id=', expected = ''

    @pytest.mark.parametrize("input_url, expected", [
        ('https://drive.google.com/wrongpath', ''),
        ('https://drive.google.com/file/d/', ''),
        ('https://drive.google.com/open?id=', ''),
        ('https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT', ''),
        ('https://drive.google.com/file/d/invalid_id', '')
    ])
    def test_invalid_input(input_url, expected):
>       assert _extract_google_drive_file_id(input_url) == expected
E       AssertionError: assert 'tps:' == ''
E         
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py:14: AssertionError
_ test_invalid_input[https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT-] _

input_url = 'https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT'
expected = ''

    @pytest.mark.parametrize("input_url, expected", [
        ('https://drive.google.com/wrongpath', ''),
        ('https://drive.google.com/file/d/', ''),
        ('https://drive.google.com/open?id=', ''),
        ('https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT', ''),
        ('https://drive.google.com/file/d/invalid_id', '')
    ])
    def test_invalid_input(input_url, expected):
>       assert _extract_google_drive_file_id(input_url) == expected
E       AssertionError: assert '1aBcD2eF3gHiJkLmNoPqRsT' == ''
E         
E         + 1aBcD2eF3gHiJkLmNoPqRsT

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py:14: AssertionError
_______ test_invalid_input[https://drive.google.com/file/d/invalid_id-] ________

input_url = 'https://drive.google.com/file/d/invalid_id', expected = ''

    @pytest.mark.parametrize("input_url, expected", [
        ('https://drive.google.com/wrongpath', ''),
        ('https://drive.google.com/file/d/', ''),
        ('https://drive.google.com/open?id=', ''),
        ('https://example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT', ''),
        ('https://drive.google.com/file/d/invalid_id', '')
    ])
    def test_invalid_input(input_url, expected):
>       assert _extract_google_drive_file_id(input_url) == expected
E       AssertionError: assert 'invalid_id' == ''
E         
E         + invalid_id

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py::test_invalid_input[https:/drive.google.com/wrongpath-]
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py::test_invalid_input[https:/drive.google.com/open?id=-]
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py::test_invalid_input[https:/example.com/drive/file/d/1aBcD2eF3gHiJkLmNoPqRsT-]
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_1_test_invalid_input.py::test_invalid_input[https:/drive.google.com/file/d/invalid_id-]
========================= 4 failed, 1 passed in 0.10s ==========================
"""