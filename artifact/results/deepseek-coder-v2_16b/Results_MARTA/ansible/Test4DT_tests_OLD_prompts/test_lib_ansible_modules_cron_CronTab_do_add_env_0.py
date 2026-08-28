
import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab




def test_do_add_env():
    module = MagicMock()
    module.get_bin_path.return_value = 'crontab'

    with patch('os.path.isabs', return_value=False):
        crontab = CronTab(module, user="testuser", cron_file="/etc/cron.d/testcron")

        # Initial lines in the cron file
        initial_lines = ["line1", "line2"]

        # Adding a new environment variable declaration
        new_declaration = 'NEW_ENV="value"'
        crontab.do_add_env(initial_lines, new_declaration)

        assert new_declaration in initial_lines