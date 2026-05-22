
import unittest
from httpie.context import Environment
import sys
import os
from unittest.mock import patch

class TestEnvironment(unittest.TestCase):
    def test_devnull_default(self):
        with patch('sys.stdout', new=open('/tmp/fake_stdout', 'w')):
            env = Environment()
            self.assertIsNotNone(env._devnull)
            self.assertEqual(env._devnull.mode, 'w+')
            self.assertTrue(os.path.exists('/tmp/fake_stdout'))

    def test_devnull_custom(self):
        with patch('sys.stdout', new=open('/tmp/fake_stdout', 'w')):
            env = Environment(devnull=open('/tmp/fake_devnull', 'w+'))
            self.assertIsNotNone(env._devnull)
            self.assertEqual(env._devnull.name, '/tmp/fake_devnull')
            self.assertTrue(os.path.exists('/tmp/fake_devnull'))

    def test_devnull_none(self):
        with patch('sys.stdout', new=open('/tmp/fake_stdout', 'w')):
            env = Environment(devnull=None)
            self.assertIsNone(env._devnull)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py . [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_____________________ TestEnvironment.test_devnull_default _____________________

self = <test_httpie_context_Environment_devnull_0_test_valid_inputs.TestEnvironment testMethod=test_devnull_default>

    def test_devnull_default(self):
        with patch('sys.stdout', new=open('/tmp/fake_stdout', 'w')):
            env = Environment()
>           self.assertIsNotNone(env._devnull)
E           AssertionError: unexpectedly None

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_devnull_0_test_valid_inputs.py::TestEnvironment::test_devnull_default
========================= 1 failed, 2 passed in 0.13s ==========================
"""