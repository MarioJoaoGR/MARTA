
import re
import pytest
from flutes.network import _extract_google_drive_file_id

@pytest.mark.parametrize("url, expected", [
    ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
    ('https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
    ('https://example.com/somepath/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
    ('https://drive.google.com/file/d/invalid_id/view', 'invalid_id'),  # Invalid ID for testing
    ('https://drive.google.com/file/d//view', ''),  # Empty ID for testing
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
collected 5 items

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_valid_input.py . [ 20%]
F...                                                                     [100%]

=================================== FAILURES ===================================
_ test_valid_input[https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0-1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0] _

url = 'https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'
expected = '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'

    @pytest.mark.parametrize("url, expected", [
        ('https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
        ('https://drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
        ('https://example.com/somepath/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0', '1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0'),
        ('https://drive.google.com/file/d/invalid_id/view', 'invalid_id'),  # Invalid ID for testing
        ('https://drive.google.com/file/d//view', ''),  # Empty ID for testing
    ])
    def test_valid_input(url, expected):
>       assert _extract_google_drive_file_id(url) == expected
E       AssertionError: assert 'tps:' == '1aBcD2eF3gHi...oPqRsTuVwXyZ0'
E         
E         - 1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0
E         + tps:

flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_valid_input.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__extract_google_drive_file_id_0_test_valid_input.py::test_valid_input[https:/drive.google.com/open?id=1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0-1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0]
========================= 1 failed, 4 passed in 0.09s ==========================
"""