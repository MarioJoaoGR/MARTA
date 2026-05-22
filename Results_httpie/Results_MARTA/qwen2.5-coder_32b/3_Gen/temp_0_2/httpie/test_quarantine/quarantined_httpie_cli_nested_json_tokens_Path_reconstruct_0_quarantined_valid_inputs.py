
import unittest
from unittest.mock import patch
from httpie.cli.nested_json.tokens import Token, PathAction
from httpie.cli.nested_json.path import Path

class TestPathReconstruct(unittest.TestCase):
    def test_reconstruct_key(self):
        path = Path(kind=PathAction.KEY, accessor="foo")
        self.assertEqual(path.reconstruct(), "[foo]")

    def test_reconstruct_index(self):
        path = Path(kind=PathAction.INDEX, accessor=0)
        self.assertEqual(path.reconstruct(), "[0]")

    def test_reconstruct_append(self):
        path = Path(kind=PathAction.APPEND)
        self.assertEqual(path.reconstruct(), "[]")

    @patch('httpie.cli.nested_json.tokens.OPEN_BRACKET', '[')
    @patch('httpie.cli.nested_json.tokens.CLOSE_BRACKET', ']')
    def test_reconstruct_root(self):
        path = Path(kind=PathAction.KEY, accessor="foo", is_root=True)
        self.assertEqual(path.reconstruct(), "foo")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_cli_nested_json_tokens_Path_reconstruct_0_test_valid_inputs
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_tokens_Path_reconstruct_0_test_valid_inputs.py:5:0: E0401: Unable to import 'httpie.cli.nested_json.path' (import-error)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_nested_json_tokens_Path_reconstruct_0_test_valid_inputs.py:5:0: E0611: No name 'path' in module 'httpie.cli.nested_json' (no-name-in-module)


"""