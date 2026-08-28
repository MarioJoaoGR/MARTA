
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab



def test_valid_initialization():
    module_mock = MagicMock()
    with patch('os.getuid', return_value=0):  # Mock os.getuid to simulate root user
        cron = CronTab(module_mock, user='testuser', cron_file='/etc/cron.d/testfile')
        assert cron.user == 'testuser'
        assert cron.cron_file == '/etc/cron.d/testfile'