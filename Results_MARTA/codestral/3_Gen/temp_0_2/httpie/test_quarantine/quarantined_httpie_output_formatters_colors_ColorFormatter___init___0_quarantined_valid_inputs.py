
import unittest
from unittest.mock import patch, MagicMock
from httpie.output.formatters.colors import ColorFormatter
from httpie.environment import Environment
from pygments.lexers.http import PygmentsHttpLexer
from pygments.formatters.terminal import TerminalFormatter
from ..lexers.http import SimplifiedHTTPLexer

class TestColorFormatter(unittest.TestCase):
    @patch('httpie.output.formatters.colors.MetadataLexer', autospec=True)
    def test_valid_inputs(self, MockMetadataLexer):
        env = Environment()
        env.colors = 256
        
        formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized-dark')
        
        self.assertTrue(formatter.enabled)
        self.assertEqual(formatter.explicit_json, False)
        self.assertIsInstance(formatter.http_lexer, SimplifiedHTTPLexer)
        self.assertIsInstance(formatter.header_formatter, TerminalFormatter)
        self.assertIsInstance(formatter.body_formatter, TerminalFormatter)
        MockMetadataLexer.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.environment' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:5:0: E0611: No name 'environment' in module 'httpie' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:6:0: E0401: Unable to import 'pygments.lexers.http' (import-error)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:6:0: E0611: No name 'http' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:8:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)


"""