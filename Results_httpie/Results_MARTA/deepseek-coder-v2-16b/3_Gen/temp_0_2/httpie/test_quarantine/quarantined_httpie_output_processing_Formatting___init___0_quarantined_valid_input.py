
import unittest
from httpie.output.processing import Formatting, Environment, plugin_manager
from unittest.mock import patch

class TestFormattingInit(unittest.TestCase):
    @patch('httpie.output.processing.plugin_manager.get_formatters_grouped')
    def test_valid_input(self, mock_get_formatters):
        # Mock data for testing
        groups = ['html', 'csv']
        env = Environment()
        kwargs = {'some_kwarg': 'value'}
        
        # Define the expected behavior of the mocked function
        mock_get_formatters.return_value = {
            'html': [lambda: None, lambda: None],
            'csv': [lambda: None]
        }
        
        # Create an instance of Formatting with valid input
        formatting = Formatting(groups=groups, env=env, **kwargs)
        
        # Assert that the enabled_plugins list is not empty after initialization
        self.assertIsNotNone(formatting.enabled_plugins)
        self.assertTrue(len(formatting.enabled_plugins) > 0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_____________________ TestFormattingInit.test_valid_input ______________________

self = <test_httpie_output_processing_Formatting___init___0_test_valid_input.TestFormattingInit testMethod=test_valid_input>
mock_get_formatters = <MagicMock name='get_formatters_grouped' id='140239863277840'>

    @patch('httpie.output.processing.plugin_manager.get_formatters_grouped')
    def test_valid_input(self, mock_get_formatters):
        # Mock data for testing
        groups = ['html', 'csv']
        env = Environment()
        kwargs = {'some_kwarg': 'value'}
    
        # Define the expected behavior of the mocked function
        mock_get_formatters.return_value = {
            'html': [lambda: None, lambda: None],
            'csv': [lambda: None]
        }
    
        # Create an instance of Formatting with valid input
>       formatting = Formatting(groups=groups, env=env, **kwargs)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7f8c233c8790>
groups = ['html', 'csv']
env = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f8c23345c60>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {'some_kwarg': 'value'}
available_plugins = {'csv': [<function TestFormattingInit.test_valid_input.<locals>.<lambda> at 0x7f8c233bb920>], 'html': [<function TestF...cals>.<lambda> at 0x7f8c233bb7e0>, <function TestFormattingInit.test_valid_input.<locals>.<lambda> at 0x7f8c233bb880>]}
group = 'html'
cls = <function TestFormattingInit.test_valid_input.<locals>.<lambda> at 0x7f8c233bb7e0>

    def __init__(self, groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors
    
        """
        available_plugins = plugin_manager.get_formatters_grouped()
        self.enabled_plugins = []
        for group in groups:
            for cls in available_plugins[group]:
>               p = cls(env=env, **kwargs)
E               TypeError: TestFormattingInit.test_valid_input.<locals>.<lambda>() got an unexpected keyword argument 'env'

httpie/httpie/output/processing.py:40: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py::TestFormattingInit::test_valid_input
============================== 1 failed in 0.18s ===============================
"""