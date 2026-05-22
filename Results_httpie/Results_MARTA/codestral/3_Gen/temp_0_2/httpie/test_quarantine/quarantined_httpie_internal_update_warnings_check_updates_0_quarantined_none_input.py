
import json
from datetime import datetime, timedelta
from unittest.mock import patch
from httpie.internal.update_warnings import WARN_INTERVAL, LogLevel
from httpie.core import Environment

def check_updates(env: Environment) -> None:
    if env.config.get('disable_update_warnings'):
        return None

    file = env.config.version_info_file
    update_status = _get_update_status(env)

    if not update_status:
        return None

    # If the user quickly spawns multiple httpie processes
    # we don't want to end in a race.
    with patch('httpie.core.open_with_lockfile', create=True):
        with open_with_lockfile(file) as stream:
            version_info = json.load(stream)

    # We don't want to spam the user with too many warnings,
    # so we'll only warn every once a while (WARN_INTERNAL).
    current_date = datetime.now()
    last_warned_date = version_info['last_warned_date']
    if last_warned_date is not None:
        earliest_warn_date = (
            datetime.fromisoformat(last_warned_date) + WARN_INTERVAL
        )
        if current_date < earliest_warn_date:
            return None

    env.log_error(update_status, level=LogLevel.INFO)
    version_info['last_warned_date'] = current_date.isoformat()

    with open_with_lockfile(file, 'w') as stream:
        json.dump(version_info, stream)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_internal_update_warnings_check_updates_0_test_none_input
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings_check_updates_0_test_none_input.py:13:20: E0602: Undefined variable '_get_update_status' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings_check_updates_0_test_none_input.py:21:13: E0602: Undefined variable 'open_with_lockfile' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_internal_update_warnings_check_updates_0_test_none_input.py:38:9: E0602: Undefined variable 'open_with_lockfile' (undefined-variable)


"""