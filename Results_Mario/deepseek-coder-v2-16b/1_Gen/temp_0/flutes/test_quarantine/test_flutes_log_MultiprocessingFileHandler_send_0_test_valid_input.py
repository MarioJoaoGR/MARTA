
import multiprocessing
from unittest.mock import patch
import logging
from flutes.log import MultiprocessingFileHandler

def test_send_valid_input(logger):
    logger, handler = logger
    log_message = "This is a valid log message."
    
    # Send the log message
    handler.send(log_message)
    
    # Check if the message was added to the queue (mocking Queue's put_nowait method)
    with patch('multiprocessing.Queue.put_nowait') as mock_put:
        mock_put.assert_called_once_with(log_message)

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

flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_send_valid_input ____________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py, line 7
  def test_send_valid_input(logger):
E       fixture 'logger' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py:7
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_log_MultiprocessingFileHandler_send_0_test_valid_input.py::test_send_valid_input
=============================== 1 error in 0.07s ===============================
"""