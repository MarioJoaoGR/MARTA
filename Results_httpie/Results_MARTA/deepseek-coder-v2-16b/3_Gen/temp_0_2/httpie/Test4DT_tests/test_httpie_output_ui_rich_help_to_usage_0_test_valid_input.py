
import pytest
from unittest.mock import patch
from httpie.output.ui.rich_help import ParserSpec, RenderableType, STYLE_BOLD, STYLE_USAGE_OPTIONAL, STYLE_USAGE_ERROR, STYLE_USAGE_REGULAR, STYLE_USAGE_MISSING

@pytest.mark.parametrize("spec, program_name, whitelist, expected", [
    # Add your test cases here with different spec, program_name, and whitelist values
])
def test_valid_input(spec, program_name, whitelist, expected):
    from httpie.output.ui.rich_help import to_usage
    
    with patch('httpie.output.ui.rich_help.ParserSpec', spec), \
         patch('httpie.output.ui.rich_help.RenderableType', expected):
        result = to_usage(spec, program_name=program_name, whitelist=whitelist)
        assert str(result) == expected
