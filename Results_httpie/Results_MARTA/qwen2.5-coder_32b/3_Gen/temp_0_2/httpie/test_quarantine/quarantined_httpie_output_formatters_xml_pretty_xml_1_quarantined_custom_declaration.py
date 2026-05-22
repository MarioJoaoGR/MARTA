
import pytest
from xml.dom import minidom
from typing import Optional

def create_document():
    return minidom.parseString('<root>content</root>')

doc = create_document()
custom_declaration = '<?xml version="1.0" encoding="ISO-8859-1"?>'
expected_output = custom_declaration + '\n<root>content</root>'

def pretty_xml(document: 'Document',
               declaration: Optional[str] = None,
               encoding: Optional[str] = 'UTF-8',
               indent: int = 2) -> str:
    """Render the given :class:`~xml.dom.minidom.Document` `document` into a prettified string."""
    kwargs = {
        'encoding': encoding or 'UTF-8',
        'indent': ' ' * indent,
    }
    body = document.toprettyxml(**kwargs).decode(kwargs['encoding'])

    # Remove blank lines automatically added by `toprettyxml()`.
    lines = [line for line in body.splitlines() if line.strip()]

    # xml.dom automatically adds the declaration, even if
    # it is not present in the actual body. Remove it.
    if len(lines) >= 1 and parse_declaration(lines[0]):
        lines.pop(0)
        if declaration:
            lines.insert(0, declaration)

    return '\n'.join(lines)

def test_custom_declaration():
    doc = create_document()
    result = pretty_xml(doc, custom_declaration)
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_output_formatters_xml_pretty_xml_1_test_custom_declaration
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_xml_pretty_xml_1_test_custom_declaration.py:29:27: E0602: Undefined variable 'parse_declaration' (undefined-variable)


"""