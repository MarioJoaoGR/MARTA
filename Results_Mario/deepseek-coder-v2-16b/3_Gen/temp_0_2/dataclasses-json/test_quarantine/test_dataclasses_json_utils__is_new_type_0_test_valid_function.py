
import pytest
from dataclasses_json.utils import _is_new_type
from unittest.mock import Mock, patch

@pytest.mark.parametrize("type_, expected", [
    (Mock(spec=lambda: None), False),  # Not a function or class
    (Mock(spec=lambda: None, __supertype__=None), True),  # Class without __supertype__
    (Mock(spec=lambda: None, __supertype__="NewStyleClass"), True),  # Class with __supertype__
])
def test_valid_function(_is_new_type, type_, expected):
    with patch('inspect.isfunction', return_value=True):
        assert _is_new_type(type_) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_valid_function[type_0-False] ______________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py, line 6
  @pytest.mark.parametrize("type_, expected", [
      (Mock(spec=lambda: None), False),  # Not a function or class
      (Mock(spec=lambda: None, __supertype__=None), True),  # Class without __supertype__
      (Mock(spec=lambda: None, __supertype__="NewStyleClass"), True),  # Class with __supertype__
  ])
  def test_valid_function(_is_new_type, type_, expected):
E       fixture '_is_new_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py:6
______________ ERROR at setup of test_valid_function[type_1-True] ______________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py, line 6
  @pytest.mark.parametrize("type_, expected", [
      (Mock(spec=lambda: None), False),  # Not a function or class
      (Mock(spec=lambda: None, __supertype__=None), True),  # Class without __supertype__
      (Mock(spec=lambda: None, __supertype__="NewStyleClass"), True),  # Class with __supertype__
  ])
  def test_valid_function(_is_new_type, type_, expected):
E       fixture '_is_new_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py:6
______________ ERROR at setup of test_valid_function[type_2-True] ______________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py, line 6
  @pytest.mark.parametrize("type_, expected", [
      (Mock(spec=lambda: None), False),  # Not a function or class
      (Mock(spec=lambda: None, __supertype__=None), True),  # Class without __supertype__
      (Mock(spec=lambda: None, __supertype__="NewStyleClass"), True),  # Class with __supertype__
  ])
  def test_valid_function(_is_new_type, type_, expected):
E       fixture '_is_new_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py::test_valid_function[type_0-False]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py::test_valid_function[type_1-True]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_new_type_0_test_valid_function.py::test_valid_function[type_2-True]
============================== 3 errors in 0.02s ===============================
"""