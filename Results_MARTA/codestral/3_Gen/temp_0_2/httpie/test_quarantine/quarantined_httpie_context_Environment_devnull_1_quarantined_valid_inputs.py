
import unittest
from httpie.context import Environment
from unittest.mock import patch, PropertyMock
import sys
import os

class TestEnvironment(unittest.TestCase):
    def test_devnull_default(self):
        with patch('sys.stdout', new_callable=lambda: open(os.devnull, 'w')):
            env = Environment()
            self.assertIsNotNone(env.devnull())

    def test_devnull_custom(self):
        custom_file = open('/tmp/custom_devnull', 'w')
        with patch('sys.stdout', new_callable=lambda: custom_file):
            env = Environment()
            self.assertEqual(env.devnull(), custom_file)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_context_Environment_devnull_1_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_1_test_valid_inputs.py:12:33: E1102: env.devnull is not callable (not-callable)
httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_1_test_valid_inputs.py:18:29: E1102: env.devnull is not callable (not-callable)


"""