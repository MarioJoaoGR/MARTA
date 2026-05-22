
import pytest
from httpie.output.formatters.xml import XMLFormatter

@pytest.fixture(scope="function")
def setup_formatter():
    formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 4}})
    yield formatter
    del formatter

def test_none_input(setup_formatter):
    body = None
    mime = 'application/xml'
    formatted_body = setup_formatter.format_body(body, mime)
    assert formatted_body == body

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_2_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

setup_formatter = <httpie.output.formatters.xml.XMLFormatter object at 0x7f6b5c125c50>

    def test_none_input(setup_formatter):
        body = None
        mime = 'application/xml'
>       formatted_body = setup_formatter.format_body(body, mime)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_2_test_none_input.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/output/formatters/xml.py:66: in format_body
    declaration = parse_declaration(body)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

raw_body = None

    def parse_declaration(raw_body: str) -> Optional[str]:
>       body = raw_body.strip()
E       AttributeError: 'NoneType' object has no attribute 'strip'

httpie/httpie/output/formatters/xml.py:21: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_XMLFormatter_format_body_2_test_none_input.py::test_none_input
============================== 1 failed in 0.15s ===============================
"""