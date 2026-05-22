
import json
from datetime import datetime, timedelta
from unittest.mock import patch
from httpie.internal.update_warnings import Environment, LogLevel, WARN_INTERVAL

def check_updates(env: Environment) -> None:
    if env.config.get('disable_update_warnings'):
        return None

    file = env.config.version_info_file
    update_status = _get_update_status(env)

    if not update_status:
        return None

    with patch('httpie.internal.update_warnings.open_with_lockfile', autospec=True):
        with open_with_lockfile(file) as stream:
            version_info = json.load(stream)

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
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_internal_update_warnings_check_updates_0_test_invalid_input
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings_check_updates_0_test_invalid_input.py:12:20: E0602: Undefined variable '_get_update_status' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings_check_updates_0_test_invalid_input.py:18:13: E0602: Undefined variable 'open_with_lockfile' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_internal_update_warnings_check_updates_0_test_invalid_input.py:33:9: E0602: Undefined variable 'open_with_lockfile' (undefined-variable)


"""