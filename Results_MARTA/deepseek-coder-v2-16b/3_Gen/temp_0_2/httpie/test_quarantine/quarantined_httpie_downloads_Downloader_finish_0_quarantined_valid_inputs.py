
import pytest
from unittest.mock import patch
from httpie.downloads import Downloader, DownloadStatus

def test_finish(setup_downloader):
    downloader = setup_downloader
    assert not downloader.finished

    with patch('httpie.downloads.DownloadStatus.is_finished') as mock_is_finished:
        mock_is_finished.return_value = True
        downloader.finish()

    assert downloader.finished

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_finish_0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
________________________ ERROR at setup of test_finish _________________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_finish_0_test_valid_inputs.py, line 6
  def test_finish(setup_downloader):
E       fixture 'setup_downloader' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_finish_0_test_valid_inputs.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_finish_0_test_valid_inputs.py::test_finish
=============================== 1 error in 0.14s ===============================
"""