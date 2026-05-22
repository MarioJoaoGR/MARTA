
import pytest
from xml.dom import minidom
from httpie.output.formatters.xml import pretty_xml

def test_invalid_input():
    with pytest.raises(TypeError):
        # Mock the document to be a non-XML string
        mock_document = "non-XML string"
    
        # Call the function with invalid input
        pretty_xml(mock_document)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_pretty_xml_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            # Mock the document to be a non-XML string
            mock_document = "non-XML string"
    
            # Call the function with invalid input
>           pretty_xml(mock_document)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_pretty_xml_0_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

document = 'non-XML string', declaration = None, encoding = 'utf-8', indent = 2

    def pretty_xml(document: 'Document',
                   declaration: Optional[str] = None,
                   encoding: Optional[str] = UTF8,
                   indent: int = 2) -> str:
        """Render the given :class:`~xml.dom.minidom.Document` `document` into a prettified string."""
        kwargs = {
            'encoding': encoding or UTF8,
            'indent': ' ' * indent,
        }
>       body = document.toprettyxml(**kwargs).decode(kwargs['encoding'])
E       AttributeError: 'str' object has no attribute 'toprettyxml'

httpie/httpie/output/formatters/xml.py:38: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_pretty_xml_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""