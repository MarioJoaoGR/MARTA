
import unittest
from unittest.mock import patch
from httpie.internal.update_warnings import Environment, fetch_updates

class TestFetchUpdates(unittest.TestCase):
    @patch('httpie.internal.update_warnings.spawn_daemon')
    def test_fetch_updates_lazy_mode(self, mock_spawn_daemon):
        env = Environment()
        fetch_updates(env)
        mock_spawn_daemon.assert_called_with('fetch_updates')

    @patch('httpie.internal.update_warnings._fetch_updates')
    def test_fetch_updates_eager_mode(self, mock__fetch_updates):
        env = Environment()
        fetch_updates(env, lazy=False)
        mock__fetch_updates.assert_called_with(env)
