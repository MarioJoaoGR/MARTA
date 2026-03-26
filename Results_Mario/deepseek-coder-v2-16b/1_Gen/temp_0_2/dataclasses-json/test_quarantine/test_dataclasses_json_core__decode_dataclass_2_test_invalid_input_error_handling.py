
import pytest
from dataclasses import dataclass
from dataclasses_json.core import _decode_dataclass

@dataclass
class Example:
    name: str
    age: int
    email: str = None

def test_invalid_input_error_handling(mock_dataclass):
    # Test with invalid data type for the dataclass fields
    invalid_data = {
        "name": 123,  # Invalid: should be a string
        "age": "twenty",  # Invalid: should be an integer
        "email": "invalid-email"  # Valid: can be None or omitted
    }
    
    with pytest.raises(ValueError) as exc_info:
        _decode_dataclass(mock_dataclass, invalid_data, infer_missing=False)
    
    assert str(exc_info.value) == (
        "value of non-optional type name detected when decoding Example"
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_invalid_input_error_handling.py E [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_invalid_input_error_handling ______________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_invalid_input_error_handling.py, line 12
  def test_invalid_input_error_handling(mock_dataclass):
E       fixture 'mock_dataclass' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_invalid_input_error_handling.py:12
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__decode_dataclass_2_test_invalid_input_error_handling.py::test_invalid_input_error_handling
=============================== 1 error in 0.03s ===============================
"""