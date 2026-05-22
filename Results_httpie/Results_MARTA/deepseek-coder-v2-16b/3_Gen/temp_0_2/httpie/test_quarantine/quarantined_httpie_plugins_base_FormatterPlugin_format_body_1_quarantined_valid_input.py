
from httpie.plugins.base import FormatterPlugin
from unittest.mock import patch, MagicMock

def test_valid_input():
    with patch('httpie.plugins.base.FormatterPlugin', autospec=True) as mock_formatter:
        # Arrange
        formatter = FormatterPlugin(format_options={'indent': 4})

        # Act
        formatted_content = formatter.format_body('some text', 'text/plain')

        # Assert
        assert formatted_content == 'some text'
        mock_formatter.assert_called_once_with(format_options={'indent': 4})

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_body_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.plugins.base.FormatterPlugin', autospec=True) as mock_formatter:
            # Arrange
            formatter = FormatterPlugin(format_options={'indent': 4})
    
            # Act
            formatted_content = formatter.format_body('some text', 'text/plain')
    
            # Assert
            assert formatted_content == 'some text'
>           mock_formatter.assert_called_once_with(format_options={'indent': 4})

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_body_1_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='FormatterPlugin' spec='FormatterPlugin' id='140613223719184'>
args = (), kwargs = {'format_options': {'indent': 4}}
msg = "Expected 'FormatterPlugin' to be called once. Called 0 times."

    def assert_called_once_with(self, /, *args, **kwargs):
        """assert that the mock was called exactly once and that that call was
        with the specified arguments."""
        if not self.call_count == 1:
            msg = ("Expected '%s' to be called once. Called %s times.%s"
                   % (self._mock_name or 'mock',
                      self.call_count,
                      self._calls_repr()))
>           raise AssertionError(msg)
E           AssertionError: Expected 'FormatterPlugin' to be called once. Called 0 times.

/usr/local/lib/python3.11/unittest/mock.py:950: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_base_FormatterPlugin_format_body_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.14s ===============================
"""