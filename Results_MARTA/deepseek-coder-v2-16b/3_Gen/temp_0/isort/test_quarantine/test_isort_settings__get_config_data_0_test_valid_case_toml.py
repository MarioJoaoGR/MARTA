
import pytest
from isort.settings import _get_config_data
import os
import tomllib
import configparser

def test_valid_case_toml(tmp_path, valid_file_path):
    # Create a temporary file for testing
    config_file = tmp_path / "config.toml" if valid_file_path == ".toml" else tmp_path / "config.editorconfig"
    config_file.write_text("[section1]\nkey1=value1\n[section2]\nkey2=value2")
    
    # Call the function with a mock file path and sections
    result = _get_config_data(str(config_file), ("section1", "section2"))
    
    # Check if the result is as expected
    assert result == {'section1': {'key1': 'value1'}, 'section2': {'key2': 'value2'}}

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_valid_case_toml ____________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py, line 8
  def test_valid_case_toml(tmp_path, valid_file_path):
E       fixture 'valid_file_path' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py:8
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_settings__get_config_data_0_test_valid_case_toml.py::test_valid_case_toml
=============================== 1 error in 0.10s ===============================
"""