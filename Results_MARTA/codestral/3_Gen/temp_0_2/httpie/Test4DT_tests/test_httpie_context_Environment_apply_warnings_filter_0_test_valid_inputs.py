
import unittest
from httpie.context import Environment
from unittest.mock import patch

class TestEnvironmentApplyWarningsFilter(unittest.TestCase):
    def test_apply_warnings_filter_with_low_quiet_level(self):
        env = Environment()
        env.quiet = 1  # Set a low quiet level to ensure warnings are not ignored

        with patch('httpie.context.warnings') as mock_warnings:
            env.apply_warnings_filter()
            assert mock_warnings.simplefilter.called_with("default")

    def test_apply_warnings_filter_with_high_quiet_level(self):
        env = Environment()
        env.quiet = 3  # Set a high quiet level to ensure warnings are ignored

        with patch('httpie.context.warnings') as mock_warnings:
            env.apply_warnings_filter()
            assert mock_warnings.simplefilter.called_with("ignore")

    def test_apply_warnings_filter_default(self):
        env = Environment()
        with patch('httpie.context.warnings') as mock_warnings:
            env.apply_warnings_filter()
            assert mock_warnings.simplefilter.called_with("default")
