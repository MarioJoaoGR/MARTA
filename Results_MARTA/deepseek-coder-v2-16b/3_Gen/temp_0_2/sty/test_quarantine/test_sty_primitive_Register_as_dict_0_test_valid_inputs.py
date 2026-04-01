
from sty.primitive import Register

def test_valid_inputs(register):
    # Call the as_dict method and check if it returns a dictionary
    result = register.as_dict()
    
    # Check that the returned object is indeed a dictionary
    assert isinstance(result, dict)
    
    # Check specific keys in the dictionary for their string representations
    assert "is_muted" in result

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/sty
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_valid_inputs ______________________
file /Users/mario/Desktop/GECAD/Test4Py/sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py, line 4
  def test_valid_inputs(register):
E       fixture 'register' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py:4
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR sty/Test4DT_tests/test_sty_primitive_Register_as_dict_0_test_valid_inputs.py::test_valid_inputs
=============================== 1 error in 0.01s ===============================
"""