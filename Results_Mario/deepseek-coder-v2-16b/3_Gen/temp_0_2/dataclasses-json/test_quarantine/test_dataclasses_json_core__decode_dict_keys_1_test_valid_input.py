
import pytest
from dataclasses_json.core import _decode_dict_keys, _get_type_origin
from typing import TypeVar, Any, Tuple, Dict, Union
from decimal import Decimal
from datetime import datetime
from unittest.mock import patch

@pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
    (int, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),
    (Decimal, {"123.45": "value", "678.90": "another_value"}, True, {Decimal("123.45"): "value", Decimal("678.90"): "another_value"}),
    (datetime, {"2022-01-01": "value"}, False, {datetime(2022, 1, 1): "value"})
])
def test_valid_input(_decode_dict_keys, key_type, xs, infer_missing, expected):
    with patch('dataclasses_json.core._get_type_origin', return_value=tuple) as mock_get_type_origin:
        result = _decode_dict_keys(key_type, xs, infer_missing)
        assert result == expected
        mock_get_type_origin.assert_called_once_with(key_type)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
_________ ERROR at setup of test_valid_input[int-xs0-False-expected0] __________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py, line 9
  @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
      (int, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),
      (Decimal, {"123.45": "value", "678.90": "another_value"}, True, {Decimal("123.45"): "value", Decimal("678.90"): "another_value"}),
      (datetime, {"2022-01-01": "value"}, False, {datetime(2022, 1, 1): "value"})
  ])
  def test_valid_input(_decode_dict_keys, key_type, xs, infer_missing, expected):
E       fixture '_decode_dict_keys' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:9
________ ERROR at setup of test_valid_input[Decimal-xs1-True-expected1] ________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py, line 9
  @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
      (int, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),
      (Decimal, {"123.45": "value", "678.90": "another_value"}, True, {Decimal("123.45"): "value", Decimal("678.90"): "another_value"}),
      (datetime, {"2022-01-01": "value"}, False, {datetime(2022, 1, 1): "value"})
  ])
  def test_valid_input(_decode_dict_keys, key_type, xs, infer_missing, expected):
E       fixture '_decode_dict_keys' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:9
_______ ERROR at setup of test_valid_input[datetime-xs2-False-expected2] _______
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py, line 9
  @pytest.mark.parametrize("key_type, xs, infer_missing, expected", [
      (int, {1: "value1", 2: "value2"}, False, {1: "value1", 2: "value2"}),
      (Decimal, {"123.45": "value", "678.90": "another_value"}, True, {Decimal("123.45"): "value", Decimal("678.90"): "another_value"}),
      (datetime, {"2022-01-01": "value"}, False, {datetime(2022, 1, 1): "value"})
  ])
  def test_valid_input(_decode_dict_keys, key_type, xs, infer_missing, expected):
E       fixture '_decode_dict_keys' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[int-xs0-False-expected0]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[Decimal-xs1-True-expected1]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dict_keys_1_test_valid_input.py::test_valid_input[datetime-xs2-False-expected2]
============================== 3 errors in 0.03s ===============================
"""