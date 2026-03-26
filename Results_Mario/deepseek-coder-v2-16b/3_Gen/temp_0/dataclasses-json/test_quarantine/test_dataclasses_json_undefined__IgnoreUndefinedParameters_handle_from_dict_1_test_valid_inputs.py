
import pytest
from dataclasses import fields, is_dataclass
from typing import Dict, Any
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction

class DummyClass:
    def __init__(self, param1=None):
        self.param1 = param1

@pytest.mark.parametrize("kvs", [
    ({'param1': 1, 'extra_param': 2}),
    ({'param1': 1})
])
def test_valid_inputs(self, kvs: Dict[str, Any]):
    """
    Test the `handle_from_dict` method with valid inputs.
    
    Args:
        kvs (Dict): A dictionary containing key-value pairs where keys are parameter names and values are their corresponding values.
    """
    class DummyClass:
        def __init__(self, param1=None):
            self.param1 = param1

    result = _IgnoreUndefinedParameters.handle_from_dict(DummyClass, kvs)
    assert 'extra_param' not in result, f"Unexpected parameter found: {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_inputs[kvs0] ___________________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py, line 11
  @pytest.mark.parametrize("kvs", [
      ({'param1': 1, 'extra_param': 2}),
      ({'param1': 1})
  ])
  def test_valid_inputs(self, kvs: Dict[str, Any]):
E       fixture 'self' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py:11
__________________ ERROR at setup of test_valid_inputs[kvs1] ___________________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py, line 11
  @pytest.mark.parametrize("kvs", [
      ({'param1': 1, 'extra_param': 2}),
      ({'param1': 1})
  ])
  def test_valid_inputs(self, kvs: Dict[str, Any]):
E       fixture 'self' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py:11
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py::test_valid_inputs[kvs0]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_undefined__IgnoreUndefinedParameters_handle_from_dict_1_test_valid_inputs.py::test_valid_inputs[kvs1]
============================== 2 errors in 0.03s ===============================
"""