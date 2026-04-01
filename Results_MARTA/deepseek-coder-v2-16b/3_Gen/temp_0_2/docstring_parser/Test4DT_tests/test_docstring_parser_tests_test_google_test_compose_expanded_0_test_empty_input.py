
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.mark.parametrize("source, expected", [("", "")])
def test_compose_expanded(source: str, expected: str) -> None:
    """Test compose in expanded mode."""
    assert (
        compose(parse(source), rendering_style=RenderingStyle.EXPANDED)
        == expected
    )
