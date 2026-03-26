
import pytest
from flutes.log import MultiprocessingFileHandler
import logging
import multiprocessing as mp
import threading

def test_invalid_input(setup_logger):
    logger, handler = setup_logger
    
    # Send an invalid log message (non-string)
    with pytest.raises(TypeError):
        logger.error(12345)  # This should raise a TypeError as the log message is not a string

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_2_test_invalid_input.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_invalid_input _____________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_2_test_invalid_input.py, line 8
  def test_invalid_input(setup_logger):
E       fixture 'setup_logger' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_2_test_invalid_input.py:8
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_2_test_invalid_input.py::test_invalid_input
=============================== 1 error in 0.10s ===============================
"""