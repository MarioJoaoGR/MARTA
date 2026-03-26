
import sys
from isort.format import BasicPrinter

def test_print_success(printer, capsys):
    printer.output = sys.stdout
    printer.print_success('The operation was successful!')
    captured = capsys.readouterr()
    assert "SUCCESS: The operation was successful!" in captured.out

def test_print_error(printer, capsys):
    printer.output = sys.stderr
    printer.print_error('An error happened.')
    captured = capsys.readouterr()
    assert "ERROR: An error happened." in captured.err

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_print_success _____________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py, line 5
  def test_print_success(printer, capsys):
E       fixture 'printer' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py:5
______________________ ERROR at setup of test_print_error ______________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py, line 11
  def test_print_error(printer, capsys):
E       fixture 'printer' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py:11
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py::test_print_success
ERROR isort/Test4DT_tests/test_isort_format_BasicPrinter_error_1_test_edge_case.py::test_print_error
============================== 2 errors in 0.10s ===============================
"""