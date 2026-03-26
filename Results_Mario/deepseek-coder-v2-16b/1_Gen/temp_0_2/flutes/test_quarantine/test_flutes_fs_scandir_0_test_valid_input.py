
import pytest
from pathlib import Path
from flutes.fs import scandir

@pytest.mark.parametrize("input_path", [Path('/some/valid/directory'), '/some/valid/directory'])
def test_valid_input(input_path, valid_directory):
    assert isinstance(input_path, (str, Path))
    entries = list(scandir(input_path))
    assert len(entries) > 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py EE     [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_valid_input[input_path0] ________________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py, line 6
  @pytest.mark.parametrize("input_path", [Path('/some/valid/directory'), '/some/valid/directory'])
  def test_valid_input(input_path, valid_directory):
E       fixture 'valid_directory' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py:6
__________ ERROR at setup of test_valid_input[/some/valid/directory] ___________
file /projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py, line 6
  @pytest.mark.parametrize("input_path", [Path('/some/valid/directory'), '/some/valid/directory'])
  def test_valid_input(input_path, valid_directory):
E       fixture 'valid_directory' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py::test_valid_input[input_path0]
ERROR flutes/Test4DT_tests/test_flutes_fs_scandir_0_test_valid_input.py::test_valid_input[/some/valid/directory]
============================== 2 errors in 0.08s ===============================
"""