
import pytest
from httpie.output.formatters.xml import parse_declaration, XML_DECLARATION_OPEN, XML_DECLARATION_CLOSE

class TestParseDeclaration:
    def test_valid_xml_declaration(self):
        # Valid XML declaration
        assert parse_declaration('<?xml version="1.0" encoding="UTF-8"?>') == '<?xml version="1.0" encoding="UTF-8"?>'
