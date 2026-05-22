
import unittest.mock as mock
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml, parse_declaration

def test_invalid_document():
    with mock.patch('httpie.output.formatters.xml.parse_declaration', return_value=True):
        doc = minidom.parseString('<root>content</root>')
        result = pretty_xml(doc)
    
        expected_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<root>content</root>'
        ]
        expected_result = '\n'.join(expected_lines)
    
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_invalid_document.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_document _____________________________

    def test_invalid_document():
        with mock.patch('httpie.output.formatters.xml.parse_declaration', return_value=True):
            doc = minidom.parseString('<root>content</root>')
            result = pretty_xml(doc)
    
            expected_lines = [
                '<?xml version="1.0" encoding="UTF-8"?>',
                '<root>content</root>'
            ]
            expected_result = '\n'.join(expected_lines)
    
>           assert result == expected_result, f"Expected {expected_result}, but got {result}"
E           AssertionError: Expected <?xml version="1.0" encoding="UTF-8"?>
E             <root>content</root>, but got <root>content</root>
E           assert '<root>content</root>' == '<?xml versio...ontent</root>'
E             
E             - <?xml version="1.0" encoding="UTF-8"?>
E               <root>content</root>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_invalid_document.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_pretty_xml_1_test_invalid_document.py::test_invalid_document
============================== 1 failed in 0.16s ===============================
"""