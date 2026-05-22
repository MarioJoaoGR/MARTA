
import pytest
from httpie.output.processing import Formatting, Environment
from unittest.mock import patch

@pytest.fixture
def setup_formatting():
    return Formatting(groups=['html', 'csv'], env=Environment())

def test_valid_input(setup_formatting):
    formatting = setup_formatting
    assert isinstance(formatting, Formatting)
    assert len(formatting.enabled_plugins) > 0

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_valid_input ______________________

    @pytest.fixture
    def setup_formatting():
>       return Formatting(groups=['html', 'csv'], env=Environment())

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.output.processing.Formatting object at 0x7fa5e5410a90>
groups = ['html', 'csv']
env = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7fa5e4a78900>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>
kwargs = {}
available_plugins = {'colors': [<class 'httpie.output.formatters.colors.ColorFormatter'>], 'format': [<class 'httpie.output.formatters.hea...rmatter'>, <class 'httpie.output.formatters.json.JSONFormatter'>, <class 'httpie.output.formatters.xml.XMLFormatter'>]}
group = 'html'

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
E           KeyError: 'html'

httpie/httpie/output/processing.py:39: KeyError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_processing_Formatting___init___0_test_valid_input.py::test_valid_input
=============================== 1 error in 0.31s ===============================
"""