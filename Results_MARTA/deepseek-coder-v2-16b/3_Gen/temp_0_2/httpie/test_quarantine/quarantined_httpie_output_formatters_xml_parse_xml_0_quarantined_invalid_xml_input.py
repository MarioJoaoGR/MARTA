
import pytest
from unittest.mock import patch
from defusedxml.minidom import parseString
from httpie.output.formatters.xml import parse_xml

@pytest.mark.parametrize("data", [("<root><element>value</element></root>",), ("invalid_xml",)])
def test_parse_xml(data):
    if data[0] == "invalid_xml":
        with pytest.raises(Exception):
            parse_xml(data[0])
    else:
        doc = parse_xml(data[0])
        assert isinstance(doc, parseString)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_parse_xml_0_test_invalid_xml_input.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_parse_xml[data0] _____________________________

data = ('<root><element>value</element></root>',)

    @pytest.mark.parametrize("data", [("<root><element>value</element></root>",), ("invalid_xml",)])
    def test_parse_xml(data):
        if data[0] == "invalid_xml":
            with pytest.raises(Exception):
                parse_xml(data[0])
        else:
            doc = parse_xml(data[0])
>           assert isinstance(doc, parseString)
E           TypeError: isinstance() arg 2 must be a type, a tuple of types, or a union

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_parse_xml_0_test_invalid_xml_input.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_parse_xml_0_test_invalid_xml_input.py::test_parse_xml[data0]
========================= 1 failed, 1 passed in 0.14s ==========================
"""