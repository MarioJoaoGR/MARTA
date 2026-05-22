
import pytest
from httpie.output.formatters.xml import XMLFormatter, parse_declaration, parse_xml, pretty_xml
from unittest.mock import patch

def test_none_input():
    formatter = XMLFormatter(format_options={'xml': {'format': True, 'indent': 2}})
    
    # Test with None input
    with pytest.raises(AttributeError):
        assert formatter.format_body(None, 'application/xml') == None
