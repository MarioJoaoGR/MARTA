
import unittest
from httpie.context import Environment
import sys
import os
from unittest.mock import patch

class TestEnvironment(unittest.TestCase):
    def test_devnull(self):
        with patch('sys.stderr', new=open(os.devnull, 'w')):
            env = Environment()
            self.assertIsNotNone(env._orig_stderr)
            self.assertEqual(env._orig_stderr, sys.stderr)
            devnull = env.devnull()
            self.assertIsInstance(devnull, file)
            self.assertTrue(devnull.closed)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_context_Environment_devnull_0_test_edge_cases
httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_0_test_edge_cases.py:14:22: E1102: env.devnull is not callable (not-callable)
httpie/Test4DT_tests_codestral/test_httpie_context_Environment_devnull_0_test_edge_cases.py:15:43: E0602: Undefined variable 'file' (undefined-variable)


"""