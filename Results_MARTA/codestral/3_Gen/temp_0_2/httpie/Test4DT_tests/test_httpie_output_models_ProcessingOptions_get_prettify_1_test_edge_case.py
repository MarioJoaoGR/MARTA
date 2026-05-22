
import unittest
from httpie.output.models import ProcessingOptions, PRETTY_STDOUT_TTY_ONLY, PRETTY_MAP
from unittest.mock import patch

class TestProcessingOptionsGetPrettify(unittest.TestCase):
    def test_get_prettify_when_pretty_is_tty_only(self):
        with patch('httpie.output.models.Environment') as mock_env:
            mock_env.stdout_isatty = True
            options = ProcessingOptions()
            result = options.get_prettify(mock_env)
            self.assertEqual(result, PRETTY_MAP['all'])

    def test_get_prettify_when_pretty_is_not_tty_only(self):
        with patch('httpie.output.models.Environment') as mock_env:
            mock_env.stdout_isatty = False
            options = ProcessingOptions(prettify=["indent"])
            result = options.get_prettify(mock_env)
            self.assertEqual(result, ["indent"])
