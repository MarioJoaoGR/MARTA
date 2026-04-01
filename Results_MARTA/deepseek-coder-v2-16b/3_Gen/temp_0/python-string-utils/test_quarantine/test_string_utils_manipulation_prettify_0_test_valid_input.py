
import pytest
from string_utils.manipulation import prettify

@pytest.mark.parametrize("input_string, expected", [
    (' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! ', 'Unprettified string, like this one, will be "prettified". It\'s awesome!'),
])
def test_valid_input(input_string, expected):
    assert prettify(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_ test_valid_input[ unprettified string ,, like this one,will be"prettified" .it\\' s awesome! -Unprettified string, like this one, will be "prettified". It's awesome!] _

input_string = ' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! '
expected = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'

    @pytest.mark.parametrize("input_string, expected", [
        (' unprettified string ,, like this one,will be"prettified" .it\\\' s awesome! ', 'Unprettified string, like this one, will be "prettified". It\'s awesome!'),
    ])
    def test_valid_input(input_string, expected):
>       assert prettify(input_string) == expected
E       assert "Unprettified...\' s awesome!" == "Unprettified...It's awesome!"
E         
E         Skipping 50 identical leading characters in diff, use -v to show
E         - ified". It's awesome!
E         + ified". It\' s awesome!
E         ?           + +

python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0_test_valid_input.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_prettify_0_test_valid_input.py::test_valid_input[ unprettified string ,, like this one,will be"prettified" .it\\' s awesome! -Unprettified string, like this one, will be "prettified". It's awesome!]
============================== 1 failed in 0.03s ===============================
"""