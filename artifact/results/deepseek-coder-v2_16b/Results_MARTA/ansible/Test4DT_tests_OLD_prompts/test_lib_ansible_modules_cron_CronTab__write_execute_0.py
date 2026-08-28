
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.cron import CronTab


def test_specific_cron_file():
    module = MagicMock()
    module.get_bin_path.return_value = 'crontab'

    with patch('os.path.isabs', return_value=False):
        cron_tab = CronTab(module, cron_file='/etc/cron.d/example')

    assert cron_tab.cron_file == '/etc/cron.d/example', "Cron file should be set to /etc/cron.d/example"

