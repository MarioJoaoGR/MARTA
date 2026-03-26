
import pytest
from string_utils.manipulation import __StringFormatter, InvalidInputError
from uuid import uuid4

def is_string(input_str):
    return isinstance(input_str, str)

class TestStringFormatter:
    
    @pytest.fixture
    def valid_formatter(self):
        return __StringFormatter("Hello, World!")
    
    def test_valid_input(self, valid_formatter):
        assert valid_formatter.input_string == "Hello, World!"
    
    def test_invalid_input(self):
        with pytest.raises(InvalidInputError):
            __StringFormatter(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py E [ 50%]
F                                                                        [100%]

==================================== ERRORS ====================================
____________ ERROR at setup of TestStringFormatter.test_valid_input ____________

self = <Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.TestStringFormatter object at 0x1042ec280>

    @pytest.fixture
    def valid_formatter(self):
>       return __StringFormatter("Hello, World!")
E       NameError: name '_TestStringFormatter__StringFormatter' is not defined

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py:13: NameError
=================================== FAILURES ===================================
____________________ TestStringFormatter.test_invalid_input ____________________

self = <Test4DT_tests.test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.TestStringFormatter object at 0x1042ed930>

    def test_invalid_input(self):
        with pytest.raises(InvalidInputError):
>           __StringFormatter(12345)
E           NameError: name '_TestStringFormatter__StringFormatter' is not defined

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py:20: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py::TestStringFormatter::test_invalid_input
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___placeholder_key_0_test_valid_input.py::TestStringFormatter::test_valid_input
========================== 1 failed, 1 error in 0.03s ==========================
"""