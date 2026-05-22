
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from httpie.environment import Environment
from pygments.lexers.http import PygmentsHttpLexer
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.style import Style

class TestColorFormatter(unittest.TestCase):
    @patch('httpie.output.formatters.colors.PIE_STYLES', {'solarized-dark': ('header_style', 'body_style')})
    def test_get_formatters(self):
        env = Environment()
        env.colors = 256
        color_scheme = 'solarized-dark'
        
        formatter = ColorFormatter(env=env, color_scheme=color_scheme)
        
        header_formatter, body_formatter, precise = formatter.get_formatters(color_scheme)
        
        self.assertIsInstance(header_formatter, Terminal256Formatter)
        self.assertIsInstance(body_formatter, Terminal256Formatter)
        self.assertTrue(precise)

    def test_init_no_colors(self):
        env = Environment()
        env.colors = False
        color_scheme = 'auto'
        
        formatter = ColorFormatter(env=env, color_scheme=color_scheme)
        
        self.assertFalse(formatter.enabled)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_ColorFormatter_get_formatters_0_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_formatters_0_test_edge_case.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_formatters_0_test_edge_case.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_formatters_0_test_edge_case.py:6:0: E0401: Unable to import 'pygments.lexers.http' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter_get_formatters_0_test_edge_case.py:6:0: E0611: No name 'http' in module 'pygments.lexers' (no-name-in-module)


"""