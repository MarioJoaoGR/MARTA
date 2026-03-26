
import pytest
from string_utils.manipulation import InvalidInputError

class Test__StringFormatterInit:
    def test_none_input(self):
        with pytest.raises(InvalidInputError) as exc_info:
            __StringFormatter(None)
        assert str(exc_info.value) == "Expected 'str', received 'NoneType'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringFormatter___init___1_test_none_input
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___init___1_test_none_input.py:8:12: E0602: Undefined variable '__StringFormatter' (undefined-variable)

"""