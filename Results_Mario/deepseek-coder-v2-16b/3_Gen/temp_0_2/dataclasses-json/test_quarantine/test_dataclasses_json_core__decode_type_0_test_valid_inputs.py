
import pytest
from dataclasses import dataclass
from decimal import Decimal
from datetime import datetime
from uuid import UUID
from dataclasses_json.core import _decode_type

@pytest.mark.parametrize("type_, value, infer_missing, expected", [
    (int, "123", False, 123),
    (float, "123.45", False, 123.45),
    (str, 123, False, "123"),
    (bool, "True", False, True),
    (Decimal, "123.45", False, Decimal("123.45")),
    (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
    (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
    (str, None, True, ""),  # Default value for string when missing and infer_missing is True
])
def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
    assert _decode_type(type_, value, infer_missing) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 8 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py E [ 12%]
EEEEEEE                                                                  [100%]

==================================== ERRORS ====================================
____________ ERROR at setup of test_valid_inputs[int-123-False-123] ____________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
________ ERROR at setup of test_valid_inputs[float-123.45-False-123.45] ________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
____________ ERROR at setup of test_valid_inputs[str-123-False-123] ____________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
__________ ERROR at setup of test_valid_inputs[bool-True-False-True] ___________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
_____ ERROR at setup of test_valid_inputs[Decimal-123.45-False-expected4] ______
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
_ ERROR at setup of test_valid_inputs[datetime-2023-10-10T10:10:10-False-expected5] _
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
_ ERROR at setup of test_valid_inputs[UUID-123e4567-e89b-12d3-a456-426614174000-False-expected6] _
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
_____________ ERROR at setup of test_valid_inputs[str-None-True-] ______________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py, line 9
  @pytest.mark.parametrize("type_, value, infer_missing, expected", [
      (int, "123", False, 123),
      (float, "123.45", False, 123.45),
      (str, 123, False, "123"),
      (bool, "True", False, True),
      (Decimal, "123.45", False, Decimal("123.45")),
      (datetime, "2023-10-10T10:10:10", False, datetime(2023, 10, 10, 10, 10, 10)),
      (UUID, "123e4567-e89b-12d3-a456-426614174000", False, UUID("123e4567-e89b-12d3-a456-426614174000")),
      (str, None, True, ""),  # Default value for string when missing and infer_missing is True
  ])
  def test_valid_inputs(_decode_type, type_, value, infer_missing, expected):
E       fixture '_decode_type' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[int-123-False-123]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[float-123.45-False-123.45]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[str-123-False-123]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[bool-True-False-True]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[Decimal-123.45-False-expected4]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[datetime-2023-10-10T10:10:10-False-expected5]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[UUID-123e4567-e89b-12d3-a456-426614174000-False-expected6]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_type_0_test_valid_inputs.py::test_valid_inputs[str-None-True-]
============================== 8 errors in 0.03s ===============================
"""