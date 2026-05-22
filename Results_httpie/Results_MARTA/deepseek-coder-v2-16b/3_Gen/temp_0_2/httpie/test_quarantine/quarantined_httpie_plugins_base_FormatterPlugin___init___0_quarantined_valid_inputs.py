
import unittest
from unittest.mock import patch
from httpie.plugins.base import Environment

class TestFormatterPlugin(unittest.TestCase):
    @patch('httpie.plugins.base.Environment')
    def test_valid_inputs(self, MockEnvironment):
        # Arrange
        mock_env = MockEnvironment()
        format_options = {'style': 'pretty'}
        
        # Act
        formatter = FormatterPlugin(env=mock_env, format_options=format_options)
        
        # Assert
        self.assertTrue(formatter.enabled)
        self.assertEqual(formatter.kwargs['format_options'], format_options)
        self.assertIsInstance(formatter.env, MockEnvironment)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs.py:4:0: E0611: No name 'Environment' in module 'httpie.plugins.base' (no-name-in-module)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin___init___0_test_valid_inputs.py:14:20: E0602: Undefined variable 'FormatterPlugin' (undefined-variable)


"""