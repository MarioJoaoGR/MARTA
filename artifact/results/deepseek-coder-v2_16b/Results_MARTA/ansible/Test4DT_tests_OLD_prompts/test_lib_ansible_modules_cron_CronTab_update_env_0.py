
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab

def test_valid_case():
    module = MagicMock()
    module.get_bin_path.return_value = 'crontab'

    with patch('os.path.isabs', return_value=False):
        with patch('os.path.join', return_value='/etc/cron.d/example'):
            cron = CronTab(module, user='user123', cron_file='example')

            assert cron.user == 'user123'
            assert cron.cron_file == '/etc/cron.d/example'
            assert cron.root is False
            assert cron.lines is not None
