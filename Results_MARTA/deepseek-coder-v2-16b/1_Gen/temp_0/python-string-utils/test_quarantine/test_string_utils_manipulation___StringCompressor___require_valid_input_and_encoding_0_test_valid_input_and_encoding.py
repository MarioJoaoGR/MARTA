
from string_utils.manipulation import __StringCompressor
import pytest

def is_string(value):
    return isinstance(value, str)

class InvalidInputError(Exception):
    pass

@pytest.mark.parametrize("input_string, encoding", [
    ("example", "utf-8"),  # Valid input and encoding
    pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
    pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
    pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
    pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
])
def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
    with pytest.raises(InvalidInputError) if not is_string(input_string) else None:
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
    
    with pytest.raises(ValueError) if len(input_string) == 0 or not is_string(encoding) else None:
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py E [ 20%]
EEEE                                                                     [100%]

==================================== ERRORS ====================================
________ ERROR at setup of test_valid_input_and_encoding[example-utf-8] ________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py, line 11
  @pytest.mark.parametrize("input_string, encoding", [
      ("example", "utf-8"),  # Valid input and encoding
      pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
      pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
      pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
      pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
  ])
  def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
E       fixture '__StringCompressor' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:11
__________ ERROR at setup of test_valid_input_and_encoding[example-] ___________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py, line 11
  @pytest.mark.parametrize("input_string, encoding", [
      ("example", "utf-8"),  # Valid input and encoding
      pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
      pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
      pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
      pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
  ])
  def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
E       fixture '__StringCompressor' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:11
___________ ERROR at setup of test_valid_input_and_encoding[-utf-8] ____________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py, line 11
  @pytest.mark.parametrize("input_string, encoding", [
      ("example", "utf-8"),  # Valid input and encoding
      pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
      pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
      pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
      pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
  ])
  def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
E       fixture '__StringCompressor' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:11
__________ ERROR at setup of test_valid_input_and_encoding[123-utf-8] __________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py, line 11
  @pytest.mark.parametrize("input_string, encoding", [
      ("example", "utf-8"),  # Valid input and encoding
      pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
      pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
      pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
      pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
  ])
  def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
E       fixture '__StringCompressor' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:11
________ ERROR at setup of test_valid_input_and_encoding[example-None] _________
file /Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py, line 11
  @pytest.mark.parametrize("input_string, encoding", [
      ("example", "utf-8"),  # Valid input and encoding
      pytest.param("example", "", marks=pytest.mark.xfail(raises=ValueError)),  # Invalid empty string for input
      pytest.param("", "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid empty string for input_string
      pytest.param(123, "utf-8", marks=pytest.mark.xfail(raises=InvalidInputError)),  # Invalid type for input_string
      pytest.param("example", None, marks=pytest.mark.xfail(raises=ValueError))  # Invalid type for encoding
  ])
  def test_valid_input_and_encoding(__StringCompressor, input_string, encoding):
E       fixture '__StringCompressor' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:11
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[example-utf-8]
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[example-]
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[-utf-8]
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[123-utf-8]
ERROR python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[example-None]
============================== 5 errors in 0.02s ===============================

"""