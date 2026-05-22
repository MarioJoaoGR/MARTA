
import pytest
from httpie.output.models import ProcessingOptions, Environment, PRETTY_STDOUT_TTY_ONLY, PRETTY_MAP

def test_get_prettify():
    # Create a mock environment with stdout being a TTY
    env = Environment(stdout_isatty=True)
    
    # Create a ProcessingOptions instance with default prettify settings
    options = ProcessingOptions()
    
    # Test the get_prettify method when prettify is set to PRETTY_STDOUT_TTY_ONLY
    assert options.get_prettify(env) == ['all']

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_get_prettify _______________________________

    def test_get_prettify():
        # Create a mock environment with stdout being a TTY
        env = Environment(stdout_isatty=True)
    
        # Create a ProcessingOptions instance with default prettify settings
        options = ProcessingOptions()
    
        # Test the get_prettify method when prettify is set to PRETTY_STDOUT_TTY_ONLY
>       assert options.get_prettify(env) == ['all']
E       AssertionError: assert ['format', 'colors'] == ['all']
E         
E         At index 0 diff: 'format' != 'all'
E         Left contains one more item: 'colors'
E         Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_models_ProcessingOptions_get_prettify_1_test_edge_case.py::test_get_prettify
============================== 1 failed in 0.26s ===============================
"""