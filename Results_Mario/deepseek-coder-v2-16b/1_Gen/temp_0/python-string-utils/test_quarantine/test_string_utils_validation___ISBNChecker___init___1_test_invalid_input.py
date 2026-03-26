
import pytest
from string_utils.validation import is_string, InvalidInputError

class __ISBNChecker:
    """
    A class for checking and normalizing ISBN numbers.

    The `__ISBNChecker` class is designed to validate and optionally normalize ISBN-10 and ISBN-13 numbers by removing hyphens. It accepts an input string representing the potential ISBN number, along with a boolean flag to control normalization.

    Parameters:
        input_string (str): A string that represents the ISBN number. This should be either an ISBN-10 or ISBN-13 number.
        normalize (bool, optional): If set to `True` (default), hyphens will be removed from the input string before processing. If set to `False`, the input string is used as provided without modification.

    Raises:
        InvalidInputError: If the provided `input_string` is not a string, this error will be raised.

    Returns:
        None directly. However, the class instance stores the normalized or unmodified ISBN number in the attribute `self.input_string`.

    Example Usage:
        >>> checker = __ISBNChecker("978-0-13-235088-4")
        >>> print(checker.input_string)  # Output: "9780132350884"
        
        >>> checker = __ISBNChecker("0-13-235088-4", normalize=False)
        >>> print(checker.input_string)  # Output: "0132350884"
    """
    def __init__(self, input_string: str, normalize: bool = True):
        if not is_string(input_string):
            raise InvalidInputError(input_string)

        self.input_string = input_string.replace('-', '') if normalize else input_string

@pytest.mark.parametrize("input_string, normalize, expected", [
    ("978-0-13-235088-4", True, "9780132350884"),
    ("0-13-235088-4", False, "0132350884"),
    (12345, True, pytest.raises(InvalidInputError)),
    ("978-0-13-235088-4", False, "978-0-13-235088-4")
])
def test_invalid_input(__ISBNChecker, input_string, normalize, expected):
    if isinstance(expected, pytest.raises):
        with pytest.raises(InvalidInputError):
            __ISBNChecker(input_string, normalize)
    else:
        checker = __ISBNChecker(input_string, normalize)
        assert checker.input_string == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py E [ 25%]
EEE                                                                      [100%]

==================================== ERRORS ====================================
__ ERROR at setup of test_invalid_input[978-0-13-235088-4-True-9780132350884] __
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py, line 34
  @pytest.mark.parametrize("input_string, normalize, expected", [
      ("978-0-13-235088-4", True, "9780132350884"),
      ("0-13-235088-4", False, "0132350884"),
      (12345, True, pytest.raises(InvalidInputError)),
      ("978-0-13-235088-4", False, "978-0-13-235088-4")
  ])
  def test_invalid_input(__ISBNChecker, input_string, normalize, expected):
E       fixture '__ISBNChecker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py:34
_____ ERROR at setup of test_invalid_input[0-13-235088-4-False-0132350884] _____
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py, line 34
  @pytest.mark.parametrize("input_string, normalize, expected", [
      ("978-0-13-235088-4", True, "9780132350884"),
      ("0-13-235088-4", False, "0132350884"),
      (12345, True, pytest.raises(InvalidInputError)),
      ("978-0-13-235088-4", False, "978-0-13-235088-4")
  ])
  def test_invalid_input(__ISBNChecker, input_string, normalize, expected):
E       fixture '__ISBNChecker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py:34
__________ ERROR at setup of test_invalid_input[12345-True-expected2] __________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py, line 34
  @pytest.mark.parametrize("input_string, normalize, expected", [
      ("978-0-13-235088-4", True, "9780132350884"),
      ("0-13-235088-4", False, "0132350884"),
      (12345, True, pytest.raises(InvalidInputError)),
      ("978-0-13-235088-4", False, "978-0-13-235088-4")
  ])
  def test_invalid_input(__ISBNChecker, input_string, normalize, expected):
E       fixture '__ISBNChecker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py:34
_ ERROR at setup of test_invalid_input[978-0-13-235088-4-False-978-0-13-235088-4] _
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py, line 34
  @pytest.mark.parametrize("input_string, normalize, expected", [
      ("978-0-13-235088-4", True, "9780132350884"),
      ("0-13-235088-4", False, "0132350884"),
      (12345, True, pytest.raises(InvalidInputError)),
      ("978-0-13-235088-4", False, "978-0-13-235088-4")
  ])
  def test_invalid_input(__ISBNChecker, input_string, normalize, expected):
E       fixture '__ISBNChecker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py:34
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py::test_invalid_input[978-0-13-235088-4-True-9780132350884]
ERROR python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py::test_invalid_input[0-13-235088-4-False-0132350884]
ERROR python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py::test_invalid_input[12345-True-expected2]
ERROR python-string-utils/Test4DT_tests/test_string_utils_validation___ISBNChecker___init___1_test_invalid_input.py::test_invalid_input[978-0-13-235088-4-False-978-0-13-235088-4]
============================== 4 errors in 0.02s ===============================

"""