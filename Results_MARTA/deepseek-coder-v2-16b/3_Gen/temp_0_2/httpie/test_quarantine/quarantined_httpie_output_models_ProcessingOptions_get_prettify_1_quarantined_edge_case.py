
import pytest
from unittest.mock import patch
from httpie.output.models import Environment, ProcessingOptions, PRETTY_STDOUT_TTY_ONLY, PRETTY_MAP

class TestProcessingOptionsGetPrettify:
    def test_get_prettify_when_tty_false(self):
        options = ProcessingOptions()
        with patch('httpie.output.models.Environment') as mock_env:
            mock_env.stdout_isatty = lambda: False
            result = options.get_prettify(mock_env())
            assert result == PRETTY_MAP['none']

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______ TestProcessingOptionsGetPrettify.test_get_prettify_when_tty_false _______

self = <test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.TestProcessingOptionsGetPrettify object at 0x7f7e4913f490>

    def test_get_prettify_when_tty_false(self):
        options = ProcessingOptions()
        with patch('httpie.output.models.Environment') as mock_env:
            mock_env.stdout_isatty = lambda: False
            result = options.get_prettify(mock_env())
>           assert result == PRETTY_MAP['none']
E           AssertionError: assert ['format', 'colors'] == []
E             
E             Left contains 2 more items, first extra item: 'format'
E             Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py::TestProcessingOptionsGetPrettify::test_get_prettify_when_tty_false
============================== 1 failed in 0.18s ===============================
"""