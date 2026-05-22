
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import get_color

def make_style(name, raw_styles, shade):
    def format_value(value):
        return ' '.join(
            get_color(part, shade) or part
            for part in value.split()
        )

    bases = (pygments.style.Style,)
    data = {
        'styles': {
            key: format_value(value)
            for key, value in raw_styles.items()
        }
    }
    return type(name, bases, data)

@patch('httpie.output.formatters.colors.get_color', MagicMock(return_value='mocked_color'))
def test_valid_case():
    raw_styles = {
        Token.Keyword: "bold red",
        Token.Number: "green"
    }
    MyStyle = make_style('MyStyle', raw_styles, 2)
    
    assert isinstance(MyStyle, type)
    assert MyStyle.__name__ == 'MyStyle'
    assert MyStyle.styles[Token.Keyword] == 'mocked_color'
    assert MyStyle.styles[Token.Number] == 'green'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_make_style_0_test_valid_case
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_style_0_test_valid_case.py:13:13: E0602: Undefined variable 'pygments' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_style_0_test_valid_case.py:25:8: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_style_0_test_valid_case.py:26:8: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_style_0_test_valid_case.py:32:26: E0602: Undefined variable 'Token' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_make_style_0_test_valid_case.py:33:26: E0602: Undefined variable 'Token' (undefined-variable)


"""