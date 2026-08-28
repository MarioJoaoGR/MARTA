
import pytest
from apimd.parser import Parser

def test_invalid_inputs():
    source_code = 'invalid code'
    parser = Parser()

    with pytest.raises(SyntaxError) as excinfo:
        parser.parse('pkg_name', source_code)

    assert "invalid syntax" in str(excinfo.value)



