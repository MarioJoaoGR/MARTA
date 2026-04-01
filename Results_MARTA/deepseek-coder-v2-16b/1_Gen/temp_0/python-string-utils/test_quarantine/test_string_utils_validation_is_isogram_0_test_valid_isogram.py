
from string_utils.validation import is_isogram

def test_valid_isogram():
    assert is_isogram('dermatoglyphics') == True
    assert is_isogram('hello') == False
    assert is_isogram(' ') == False
    assert is_isogram('') == False
    assert is_isogram('lumberjacks') == True
    assert is_isogram('subdermatoglyphic') == True
    assert is_isogram('Alphabet') == False

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_valid_isogram.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_isogram ______________________________

    def test_valid_isogram():
        assert is_isogram('dermatoglyphics') == True
        assert is_isogram('hello') == False
        assert is_isogram(' ') == False
        assert is_isogram('') == False
        assert is_isogram('lumberjacks') == True
        assert is_isogram('subdermatoglyphic') == True
>       assert is_isogram('Alphabet') == False
E       AssertionError: assert True == False
E        +  where True = is_isogram('Alphabet')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_valid_isogram.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_valid_isogram.py::test_valid_isogram
============================== 1 failed in 0.03s ===============================

"""