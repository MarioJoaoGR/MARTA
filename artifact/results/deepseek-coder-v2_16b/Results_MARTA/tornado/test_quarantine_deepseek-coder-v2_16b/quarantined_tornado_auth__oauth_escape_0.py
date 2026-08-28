
import pytest
import urllib.parse
from typing import Union

def _oauth_escape(val: Union[str, bytes]) -> str:
    if isinstance(val, str):
        val = val.encode("utf-8")
    return urllib.parse.quote(val, safe="~")

@pytest.mark.parametrize("input_value, expected", [
    ("Hello, World!", 'Hello%2C+World%21'),
    (b"Hello, World!", 'Hello%2C+World%21'),
])
def test_valid_input(input_value, expected):
    assert _oauth_escape(input_value) == expected
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth_escape_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________ test_valid_input[Hello, World!-Hello%2C+World%21_0] ______________

input_value = 'Hello, World!', expected = 'Hello%2C+World%21'

    @pytest.mark.parametrize("input_value, expected", [
        ("Hello, World!", 'Hello%2C+World%21'),
        (b"Hello, World!", 'Hello%2C+World%21'),
    ])
    def test_valid_input(input_value, expected):
>       assert _oauth_escape(input_value) == expected
E       AssertionError: assert 'Hello%2C%20World%21' == 'Hello%2C+World%21'
E         
E         - Hello%2C+World%21
E         ?         ^
E         + Hello%2C%20World%21
E         ?         ^^^

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth_escape_0.py:16: AssertionError
_____________ test_valid_input[Hello, World!-Hello%2C+World%21_1] ______________

input_value = b'Hello, World!', expected = 'Hello%2C+World%21'

    @pytest.mark.parametrize("input_value, expected", [
        ("Hello, World!", 'Hello%2C+World%21'),
        (b"Hello, World!", 'Hello%2C+World%21'),
    ])
    def test_valid_input(input_value, expected):
>       assert _oauth_escape(input_value) == expected
E       AssertionError: assert 'Hello%2C%20World%21' == 'Hello%2C+World%21'
E         
E         - Hello%2C+World%21
E         ?         ^
E         + Hello%2C%20World%21
E         ?         ^^^

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth_escape_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth_escape_0.py::test_valid_input[Hello, World!-Hello%2C+World%21_0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth_escape_0.py::test_valid_input[Hello, World!-Hello%2C+World%21_1]
============================== 2 failed in 0.07s ===============================
"""