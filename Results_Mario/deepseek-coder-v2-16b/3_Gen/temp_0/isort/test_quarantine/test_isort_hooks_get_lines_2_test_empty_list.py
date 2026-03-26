
import pytest
from isort.hooks import get_lines  # Assuming the module and function are correctly imported

@pytest.fixture(autouse=True)
def mock_get_output(mocker):
    mocker.patch('isort.hooks.get_output', return_value='')

def test_empty_list():
    assert get_lines(['ls', '-l']) == []

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

isort/Test4DT_tests/test_isort_hooks_get_lines_2_test_empty_list.py E    [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_empty_list _______________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_hooks_get_lines_2_test_empty_list.py, line 9
  def test_empty_list():
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_hooks_get_lines_2_test_empty_list.py, line 5
  @pytest.fixture(autouse=True)
  def mock_get_output(mocker):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, mock_get_output, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_hooks_get_lines_2_test_empty_list.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_hooks_get_lines_2_test_empty_list.py::test_empty_list
=============================== 1 error in 0.10s ===============================
"""