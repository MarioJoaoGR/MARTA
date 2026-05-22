
import pytest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from httpie.core.models import Environment
from pygments.style import ClassNotFound
from pygments.styles import Solarized256Style

@pytest.fixture
def setup_color_formatter():
    env = MagicMock(spec=Environment)
    env.colors = 256
    return ColorFormatter(env=env, color_scheme='solarized-dark')

def test_get_style_class_valid_scheme(setup_color_formatter):
    with patch('pygments.styles.get_style_by_name', return_value=Solarized256Style):
        style_class = setup_color_formatter.get_style_class('solarized-dark')
        assert isinstance(style_class, type) and issubclass(style_class, pygments.style.Style)

def test_get_style_class_invalid_scheme(setup_color_formatter):
    with patch('pygments.styles.get_style_by_name', side_effect=ClassNotFound):
        style_class = setup_color_formatter.get_style_class('non-existent-scheme')
        assert style_class == Solarized256Style

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input.py:5:0: E0401: Unable to import 'httpie.core.models' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input.py:5:0: E0611: No name 'models' in module 'httpie.core' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input.py:6:0: E0611: No name 'ClassNotFound' in module 'pygments.style' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input.py:7:0: E0611: No name 'Solarized256Style' in module 'pygments.styles' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_style_class_0_test_invalid_input.py:18:73: E0602: Undefined variable 'pygments' (undefined-variable)


"""