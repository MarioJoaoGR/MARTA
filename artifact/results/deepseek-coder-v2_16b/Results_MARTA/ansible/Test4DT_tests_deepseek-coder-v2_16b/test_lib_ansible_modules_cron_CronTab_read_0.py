
import pytest
from ansible.modules.cron import CronTab
from unittest.mock import MagicMock, patch



def test_init_with_cron_file():
    module = MagicMock()
    cron = CronTab(module, cron_file='/etc/cron.d/example')
    assert cron.user is None
    assert cron.cron_file == '/etc/cron.d/example'
    assert cron.root is False
    assert cron.lines == []

def test_init_with_both():
    module = MagicMock()
    cron = CronTab(module, user='root', cron_file='/etc/cron.d/example')
    assert cron.user == 'root'
    assert cron.cron_file == '/etc/cron.d/example'
    assert cron.root is False
    assert cron.lines == []

