
import os
import pickle
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from flutes.fs import cache

def test_valid_inputs(cache_decorator):
    @cache_decorator("my_cache.pkl", verbose=False)
    def expensive_function(x):
        return x * 2

    # First call should execute the function and save to cache
    result = expensive_function(5)
    assert result == 10

    # Second call should load from cache without executing the function
    with patch('builtins.open', new=MagicMock()) as mock_file:
        mock_file.return_value.__enter__.return_value.read = MagicMock(return_value=pickle.dumps(10))
        result = expensive_function(5)
        assert result == 10
        mock_file.assert_called_once_with("my_cache.pkl", "rb")

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

flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_inputs.py E       [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_inputs.py, line 9
  def test_valid_inputs(cache_decorator):
E       fixture 'cache_decorator' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_inputs.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_fs_cache_0_test_valid_inputs.py::test_valid_inputs
=============================== 1 error in 0.07s ===============================
"""