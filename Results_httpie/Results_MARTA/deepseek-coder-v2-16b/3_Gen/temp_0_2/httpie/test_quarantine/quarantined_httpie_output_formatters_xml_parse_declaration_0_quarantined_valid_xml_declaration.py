
import pytest
from unittest.mock import patch
from xml.etree.ElementTree import ParseError
from lxml import etree

def parse_declaration(raw_body: str) -> Optional[str]:
    body = raw_body.strip()
    if body.startswith('<?xml'):
        end = body.find('?>')
        if end != -1:
            return body[:end + 2]
    return None

# Test valid XML declaration with version and encoding
def test_valid_xml_declaration():
    raw_body = '<?xml version="1.0" encoding="UTF-8"?>'
    result = parse_declaration(raw_body)
    assert result == '<?xml version="1.0" encoding="UTF-8"?>'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_xml_parse_declaration_0_test_valid_xml_declaration
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_parse_declaration_0_test_valid_xml_declaration.py:5:0: E0401: Unable to import 'lxml' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_xml_parse_declaration_0_test_valid_xml_declaration.py:7:40: E0602: Undefined variable 'Optional' (undefined-variable)


"""