
import unittest.mock as mock
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml

def test_valid_input(self):
    with mock.patch('httpie.output.formatters.xml.pretty_xml', return_value='<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'):
        doc = minidom.parseString('<root>content</root>')
        expected_output = '<?xml version="1.0" encoding="UTF-8"?>\n<root>content</root>'
        self.assertEqual(pretty_xml(doc), expected_output)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_valid_input.py, line 6
  def test_valid_input(self):
E       fixture 'self' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_valid_input.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_valid_input.py::test_valid_input
=============================== 1 error in 0.16s ===============================
"""