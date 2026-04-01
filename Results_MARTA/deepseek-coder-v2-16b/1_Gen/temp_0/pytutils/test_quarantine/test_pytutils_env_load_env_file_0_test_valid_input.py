
import os
import typing
import collections
import pytest
from pytutils.env import load_env_file

@pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
def test_valid_input(lines, mocker):
    # Mock os.environ to simulate environment variables
    mock_environ = mocker.patch('os.environ', {})
    
    expected_output = collections.OrderedDict([
        ('TEST', os.path.expanduser('${HOME}/yeee-$PATH')),
        ('THISIS', os.path.expanduser('~/a/test')),
        ('YOLO', os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST'))
    ])
    
    result = load_env_file(lines)
    
    assert result == expected_output
    assert mock_environ == {
        'TEST': os.path.expanduser('${HOME}/yeee-$PATH'),
        'THISIS': os.path.expanduser('~/a/test'),
        'YOLO': os.path.expanduser('~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST')
    }

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
__________________ ERROR at setup of test_valid_input[lines0] __________________
file /projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py, line 8
  @pytest.mark.parametrize("lines", [['TEST=${HOME}/yeee-$PATH', 'THISIS=~/a/test', 'YOLO=~/swaggins/$NONEXISTENT_VAR_THAT_DOES_NOT_EXIST']])
  def test_valid_input(lines, mocker):
E       fixture 'mocker' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py:8
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR pytutils/Test4DT_tests/test_pytutils_env_load_env_file_0_test_valid_input.py::test_valid_input[lines0]
=============================== 1 error in 0.04s ===============================
"""