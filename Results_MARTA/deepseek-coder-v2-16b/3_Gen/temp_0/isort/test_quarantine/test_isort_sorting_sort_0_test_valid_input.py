
import pytest
from isort import Config
from isort.sorting import sort, naturally

def test_valid_input(config):
    assert sort(config, ["a", "b", "c", "d"]) == ['a', 'b', 'c', 'd']
    assert sort(config, ["a", "b", "c", "d"], key=lambda x: len(x)) == ['a', 'b', 'c', 'd']

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

isort/Test4DT_tests/test_isort_sorting_sort_0_test_valid_input.py E      [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_sorting_sort_0_test_valid_input.py, line 6
  def test_valid_input(config):
E       fixture 'config' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_sorting_sort_0_test_valid_input.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_sorting_sort_0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.09s ===============================
"""