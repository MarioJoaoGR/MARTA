
import unittest
from httpie.context import Environment
import sys
import os
from unittest.mock import patch

class TestEnvironment(unittest.TestCase):
    def test_devnull_default(self):
        with patch('sys.stderr', new=open(os.devnull, 'w')):
            env = Environment()
            self.assertIsNotNone(env.devnull)
            self.assertEqual(env.devnull.mode, 'w+')
    
    def test_devnull_custom(self):
        with patch('sys.stderr', new=open('/tmp/custom_devnull', 'w')):
            env = Environment()
            self.assertIsNotNone(env.devnull)
            self.assertEqual(env.devnull.name, '/tmp/custom_devnull')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_valid_inputs.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
_____________________ TestEnvironment.test_devnull_custom ______________________

self = <test_httpie_context_Environment_devnull_1_test_valid_inputs.TestEnvironment testMethod=test_devnull_custom>

    def test_devnull_custom(self):
        with patch('sys.stderr', new=open('/tmp/custom_devnull', 'w')):
            env = Environment()
            self.assertIsNotNone(env.devnull)
>           self.assertEqual(env.devnull.name, '/tmp/custom_devnull')
E           AssertionError: '/dev/null' != '/tmp/custom_devnull'
E           - /dev/null
E           + /tmp/custom_devnull

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_valid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_context_Environment_devnull_1_test_valid_inputs.py::TestEnvironment::test_devnull_custom
========================= 1 failed, 1 passed in 0.16s ==========================
"""