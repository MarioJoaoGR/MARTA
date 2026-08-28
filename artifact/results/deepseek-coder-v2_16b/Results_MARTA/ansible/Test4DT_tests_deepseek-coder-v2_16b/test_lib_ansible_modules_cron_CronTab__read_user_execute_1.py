
import pytest
from ansible.modules.cron import CronTab
from unittest.mock import patch, MagicMock
import os
import platform
import pwd
import shlex

@pytest.fixture(scope="module")
def cron_tab():
    module = MagicMock()
    return CronTab(module)


def test_init_with_absolute_cron_file():
    module = MagicMock()
    cron_file = "/path/to/cronfile"
    cron = CronTab(module, cron_file=cron_file)
    assert cron.cron_file == cron_file
    assert cron.b_cron_file == to_bytes(cron_file, errors='surrogate_or_strict')



def to_bytes(path, errors):
    return bytes(path, 'utf-8')