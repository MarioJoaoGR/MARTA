
import re
import pytest
from flutes.network import _extract_google_drive_file_id

@pytest.mark.parametrize("url, expected", [
    ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing', '1aBcD2eF3gHiJkLmNoPqRsT'),
    ('https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsT', '1aBcD2eF3gHiJkLmNoPqRsT'),
    ('https://drive.google.com/file/d/invalid_id/view?usp=sharing', 'invalid_id'),  # Assuming invalid ID for testing
    ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/', '1aBcD2eF3gHiJkLmNoPqRsT'),  # Test case with trailing slash
])
def test_valid_input(url, expected):
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
collected 4 items

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_2_test_valid_input.py . [ 25%]
F..                                                                      [100%]

=================================== FAILURES ===================================
_ test_valid_input[https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsT-1aBcD2eF3gHiJkLmNoPqRsT] _

url = 'https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsT'
expected = '1aBcD2eF3gHiJkLmNoPqRsT'

    @pytest.mark.parametrize("url, expected", [
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing', '1aBcD2eF3gHiJkLmNoPqRsT'),
        ('https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsT', '1aBcD2eF3gHiJkLmNoPqRsT'),
        ('https://drive.google.com/file/d/invalid_id/view?usp=sharing', 'invalid_id'),  # Assuming invalid ID for testing
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/', '1aBcD2eF3gHiJkLmNoPqRsT'),  # Test case with trailing slash
    ])
    def test_valid_input(url, expected):
>       assert _extract_google_drive_file_id(url) == expected
E       AssertionError: assert 'tps:' == '1aBcD2eF3gHiJkLmNoPqRsT'
E         
E         - 1aBcD2eF3gHiJkLmNoPqRsT
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_2_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_2_test_valid_input.py::test_valid_input[https:/drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsT-1aBcD2eF3gHiJkLmNoPqRsT]
========================= 1 failed, 3 passed in 0.10s ==========================
"""