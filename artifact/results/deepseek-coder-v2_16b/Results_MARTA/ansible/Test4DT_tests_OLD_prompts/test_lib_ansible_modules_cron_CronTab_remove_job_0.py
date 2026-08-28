
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.cron import CronTab



def test_init_with_relative_cron_file():
    module = MagicMock()
    with patch('os.path.isabs', return_value=False):  # Mocking os.path.isabs to return False
        with patch('os.path.join', return_value='/etc/cron.d/example_cronfile'):  # Mocking os.path.join to return the expected path
            cron = CronTab(module, cron_file='example_cronfile')
            assert cron.cron_file == '/etc/cron.d/example_cronfile'

