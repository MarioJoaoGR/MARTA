
import re
from typing import Optional

XML_DECLARATION_OPEN = "<?xml"
XML_DECLARATION_CLOSE = "?>"

def parse_declaration(raw_body: str) -> Optional[str]:
    body = raw_body.strip()
    if body.startswith(XML_DECLARATION_OPEN):
        end = body.find(XML_DECLARATION_CLOSE, len(XML_DECLARATION_OPEN))
        if end != -1:
            return body[:end + len(XML_DECLARATION_CLOSE)]
    return None

def test_invalid_xml_declaration():
    raw_body = '<?xml something else?>'
    assert parse_declaration(raw_body) == '<?xml something else?>'
