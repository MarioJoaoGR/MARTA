
import pytest
from pathlib import Path
from typing import Iterator
from flutes.fs import scandir

@pytest.fixture
def valid_directory():
    return Path('/some/valid/directory')

def test_valid_input(valid_directory, mocker):
    mock_scandir = mocker.patch('os.scandir')
    
    # Mock the entries to be returned by os.scandir
    entry1 = mocker.Mock()
    entry1.path = '/some/valid/directory/file1'
    entry2 = mocker.Mock()
    entry2.path = '/some/valid/directory/file2'
    
    mock_scandir.return_value.__iter__.return_value = [entry1, entry2]
    
    # Call the function under test
    result = list(scandir(valid_directory))
    
    # Assert the results
    assert len(result) == 2
    assert Path(result[0]) == Path('/some/valid/directory/file1')
    assert Path(result[1]) == Path('/some/valid/directory/file2')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_valid_input.py E      [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_valid_input.py, line 11
  def test_valid_input(valid_directory, mocker):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory, valid_directory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_valid_input.py:11
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_fs_scandir_1_test_valid_input.py::test_valid_input
=============================== 1 error in 0.09s ===============================

"""