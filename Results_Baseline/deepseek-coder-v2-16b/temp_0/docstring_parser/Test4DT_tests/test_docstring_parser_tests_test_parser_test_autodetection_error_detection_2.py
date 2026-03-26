
import pytest
from docstring_parser import parse, DocstringStyle
try:
    from unittest.mock import patch  # For Python 3.8+
except ImportError:
    from mock import patch  # For Python 2.7 and 3.x

def test_autodetection_error_detection():
    """Test autodection for the case where one of the parsers throws an error
    and another one succeeds.
    """
    source = """
    Does something useless

    :param 3 + 3 a: a param
    """

    # Test that one of the parsers raises an error
    with pytest.raises(Exception):  # Assuming ParseError is imported from docstring_parser or similar
        parse(source, DocstringStyle.REST)

    # Test autodetection still works after an error
    docstring = parse(source)

    assert docstring is not None
    assert docstring.style == DocstringStyle.GOOGLE
