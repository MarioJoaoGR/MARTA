
import pytest
from flutes.fs import copy_tree
from pathlib import Path
import os
import shutil

def test_invalid_inputs(temp_dir):
    src_dir = temp_dir / "src"
    dst_dir = temp_dir / "dst"
    
    # Test with invalid source path (not a directory)
    with pytest.raises(FileNotFoundError):
        copy_tree("invalid/path", dst_dir, overwrite=False)
    
    # Create the source directory for valid tests
    src_dir.mkdir()
    
    # Test with invalid destination path (not a directory)
    with pytest.raises(NotADirectoryError):
        copy_tree(src_dir, "invalid/path", overwrite=False)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_invalid_inputs _____________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py, line 8
  def test_invalid_inputs(temp_dir):
E       fixture 'temp_dir' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py:8
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_fs_copy_tree_0_test_invalid_inputs.py::test_invalid_inputs
=============================== 1 error in 0.10s ===============================
"""