
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from httpie.environment import Environment
from pygments.lexers import PygmentsHttpLexer
from pygments.formatters import TerminalFormatter
from pygments.style import ClassNotFound
from pygments.styles import get_style_by_name

def test_get_style_class():
    with patch('pygments.styles.get_style_by_name', return_value=MagicMock()):
        color_scheme = 'solarized-dark'
        style_class = ColorFormatter.get_style_class(color_scheme)
        assert isinstance(style_class, type(get_style_by_name('solarized-dark')))

    with patch('pygments.styles.get_style_by_name', side_effect=ClassNotFound):
        color_scheme = 'non-existent-style'
        style_class = ColorFormatter.get_style_class(color_scheme)
        assert style_class == Solarized256Style

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:6:0: E0611: No name 'PygmentsHttpLexer' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:7:0: E0611: No name 'TerminalFormatter' in module 'pygments.formatters' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:8:0: E0611: No name 'ClassNotFound' in module 'pygments.style' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_valid_input.py:20:30: E0602: Undefined variable 'Solarized256Style' (undefined-variable)


"""