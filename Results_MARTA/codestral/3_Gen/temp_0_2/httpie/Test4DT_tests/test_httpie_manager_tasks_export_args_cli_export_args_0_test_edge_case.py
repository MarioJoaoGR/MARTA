
import unittest
from unittest.mock import patch
from httpie.manager.tasks.export_args import cli_export_args, Environment, ExitStatus, argparse

class TestCliExportArgs(unittest.TestCase):
    @patch('httpie.manager.tasks.export_args.FORMAT_TO_CONTENT_TYPE', {'json': 'application/json'})
    def test_cli_export_args_json(self):
        env = Environment()
        args = argparse.Namespace(format='json')
        result = cli_export_args(env, args)
        self.assertEqual(result, ExitStatus.SUCCESS)

    @patch('httpie.manager.tasks.export_args.FORMAT_TO_CONTENT_TYPE', {'json': 'application/json'})
    def test_cli_export_args_invalid_format(self):
        env = Environment()
        args = argparse.Namespace(format='invalid')
        with self.assertRaises(NotImplementedError):
            cli_export_args(env, args)
