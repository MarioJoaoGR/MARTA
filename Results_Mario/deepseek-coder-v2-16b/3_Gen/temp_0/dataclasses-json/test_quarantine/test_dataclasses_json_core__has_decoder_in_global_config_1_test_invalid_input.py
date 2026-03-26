
import pytest
from dataclasses_json.core import cfg  # Assuming cfg is defined in dataclasses_json.core

@pytest.mark.parametrize("type_, expected", [
    ("example_decoder", True),
    ("nonexistent_decoder", False)
])
def test_invalid_input(_has_decoder_in_global_config, type_, expected):
    # Mocking the cfg object and its global_config.decoders attribute
    class MockCfg:
        global_config = type('GlobalConfig', (), {'decoders': ['example_decoder']})()
    
    cfg.global_config.decoders = ['example_decoder']  # Setting up the mock configuration
    
    result = _has_decoder_in_global_config(type_)
    assert result == expected

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
__________ ERROR at setup of test_invalid_input[example_decoder-True] __________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py, line 5
  @pytest.mark.parametrize("type_, expected", [
      ("example_decoder", True),
      ("nonexistent_decoder", False)
  ])
  def test_invalid_input(_has_decoder_in_global_config, type_, expected):
E       fixture '_has_decoder_in_global_config' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py:5
_______ ERROR at setup of test_invalid_input[nonexistent_decoder-False] ________
file /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py, line 5
  @pytest.mark.parametrize("type_, expected", [
      ("example_decoder", True),
      ("nonexistent_decoder", False)
  ])
  def test_invalid_input(_has_decoder_in_global_config, type_, expected):
E       fixture '_has_decoder_in_global_config' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py::test_invalid_input[example_decoder-True]
ERROR dataclasses-json/Test4DT_tests/test_dataclasses_json_core__has_decoder_in_global_config_1_test_invalid_input.py::test_invalid_input[nonexistent_decoder-False]
============================== 2 errors in 0.02s ===============================
"""