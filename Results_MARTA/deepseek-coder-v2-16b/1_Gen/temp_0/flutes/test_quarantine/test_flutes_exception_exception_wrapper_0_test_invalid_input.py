
import pytest
from flutes.exception import exception_wrapper

def test_invalid_input(mock_handler):
    @exception_wrapper(mock_handler)
    def foo(one, two, *args, three=None, **kwargs):
        raise ValueError("Test exception")
    
    with pytest.raises(ValueError):
        foo(1, "2", "arg1", "arg2", four=4)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_invalid_input _____________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py, line 5
  def test_invalid_input(mock_handler):
E       fixture 'mock_handler' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_exception_exception_wrapper_0_test_invalid_input.py::test_invalid_input
=============================== 1 error in 0.08s ===============================
"""