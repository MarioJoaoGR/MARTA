
import unittest
from httpie.output.formatters.colors import ColorFormatter
from httpie.core.models import Environment, MetadataLexer
from pygments.lexers.http import PygmentsHttpLexer
from pygments.formatters.terminal import TerminalFormatter
from ..lexers.http import SimplifiedHTTPLexer

class TestColorFormatterInit(unittest.TestCase):
    def test_valid_inputs(self):
        env = Environment()
        env.colors = 256  # Assuming the environment supports 256 colors for this test
        
        with unittest.mock.patch('httpie.output.formatters.colors.ColorFormatter.get_formatters', return_value=(TerminalFormatter(), TerminalFormatter(), False)):
            formatter = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized-dark')
            
            self.assertTrue(formatter.enabled)
            self.assertEqual(formatter.explicit_json, True)
            self.assertIsInstance(formatter.header_formatter, TerminalFormatter)
            self.assertIsInstance(formatter.body_formatter, TerminalFormatter)
            self.assertIsInstance(formatter.http_lexer, SimplifiedHTTPLexer)
            self.assertIsInstance(formatter.metadata_lexer, MetadataLexer)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:4:0: E0401: Unable to import 'httpie.core.models' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:4:0: E0611: No name 'models' in module 'httpie.core' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:5:0: E0401: Unable to import 'pygments.lexers.http' (import-error)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:5:0: E0611: No name 'http' in module 'pygments.lexers' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_formatters_colors_ColorFormatter___init___0_test_valid_inputs.py:7:0: E0402: Attempted relative import beyond top-level package (relative-beyond-top-level)


"""