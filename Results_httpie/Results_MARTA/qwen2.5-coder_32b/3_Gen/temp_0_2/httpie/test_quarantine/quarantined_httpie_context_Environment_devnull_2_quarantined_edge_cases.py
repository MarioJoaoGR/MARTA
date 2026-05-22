
import pytest
from unittest.mock import patch
from httpie.context import Environment

def test_devnull():
    with patch('httpie.context.sys.stderr', new=open('/dev/null', 'w')):
        env = Environment()
        assert env.stderr == open('/dev/null', 'w')

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_devnull _________________________________

    def test_devnull():
        with patch('httpie.context.sys.stderr', new=open('/dev/null', 'w')):
            env = Environment()
>           assert env.stderr == open('/dev/null', 'w')
E           AssertionError: assert <_io.TextIOWr...oding='utf-8'> == <_io.TextIOWr...oding='utf-8'>
E             
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_2_test_edge_cases.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_2_test_edge_cases.py::test_devnull
============================== 1 failed in 0.19s ===============================
"""