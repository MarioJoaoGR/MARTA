
import pytest
from docstring_parser.tests.test_numpydoc import parse, compose

@pytest.mark.parametrize("source, expected", [("", "")])
def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode."""
    assert compose(parse(source)) == expected
