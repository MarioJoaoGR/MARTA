
import pytest
from python_string_utils import InvalidInputError, process_string

class TestStringUtilsErrors:
    def test_invalid_input_error_with_non_string(self):
        with pytest.raises(InvalidInputError) as excinfo:
            process_string(12345)
        assert str(excinfo.value) == 'Expected "str", received "int"'

    def test_invalid_input_error_with_none(self):
        with pytest.raises(InvalidInputError) as excinfo:
            process_string(None)
        assert str(excinfo.value) == 'Expected "str", received "NoneType"'

    def test_invalid_input_error_with_list(self):
        with pytest.raises(InvalidInputError) as excinfo:
            process_string([1, 2, 3])
        assert str(excinfo.value) == 'Expected "str", received "list"'

    def test_invalid_input_error_with_dict(self):
        with pytest.raises(InvalidInputError) as excinfo:
            process_string({'key': 'value'})
        assert str(excinfo.value) == 'Expected "str", received "dict"'

    def test_invalid_input_error_with_custom_object(self):
        class CustomObject:
            pass
        custom_obj = CustomObject()
        with pytest.raises(InvalidInputError) as excinfo:
            process_string(custom_obj)
        assert str(excinfo.value) == 'Expected "str", received "CustomObject"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___0
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0.py:3:0: E0401: Unable to import 'python_string_utils' (import-error)

"""