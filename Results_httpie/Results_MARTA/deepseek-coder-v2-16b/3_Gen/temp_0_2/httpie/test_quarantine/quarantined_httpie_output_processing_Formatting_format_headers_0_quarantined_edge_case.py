
import pytest
from httpie.output.processing import Formatting
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_formatting():
    return Formatting(groups=['test'], env=MagicMock())

def test_format_headers(setup_formatting):
    formatting = setup_formatting
    headers = "Test: header"
    
    with patch('httpie.output.processing.plugin_manager') as mock_plugin_manager:
        mock_formatter = MagicMock()
        mock_formatter.format_headers.return_value = "Formatted: Test: header"
        
        mock_plugin_manager.get_formatters_grouped.return_value = {'test': [mock_formatter]}
        
        result = formatting.format_headers(headers)
        
        assert result == "Formatted: Test: header"
        mock_formatter.format_headers.assert_called_once_with(headers)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_headers_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
____________________ ERROR at setup of test_format_headers _____________________

    @pytest.fixture
    def setup_formatting():
>       return Formatting(groups=['test'], env=MagicMock())

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_headers_0_test_edge_case.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7f13e80c2710>
groups = ['test'], env = <MagicMock id='139723463549008'>, kwargs = {}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.hea...rmatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>, <class 'httpie.output.formatters.xml.XMLFormatter'>]}
group = 'test'

    def __init__(self, groups: List[str], env=Environment(), **kwargs):
        """
        :param groups: names of processor groups to be applied
        :param env: Environment
        :param kwargs: additional keyword arguments for processors
    
        """
        available_plugins = plugin_manager.get_formatters_grouped()
        self.enabled_plugins = []
        for group in groups:
>           for cls in available_plugins[group]:
E           KeyError: 'test'

httpie/httpie/output/processing.py:39: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_processing_Formatting_format_headers_0_test_edge_case.py::test_format_headers
=============================== 1 error in 0.26s ===============================
"""