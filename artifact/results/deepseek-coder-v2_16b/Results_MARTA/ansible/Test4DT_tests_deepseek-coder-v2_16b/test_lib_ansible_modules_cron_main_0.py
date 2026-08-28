
import pytest
from ansible.modules.cron import main
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture(scope="function")
def module():
    return AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            user=dict(type='str'),
            job=dict(type='str', aliases=['value']),
            cron_file=dict(type='path'),
            state=dict(type='str', default='present', choices=['present', 'absent']),
            backup=dict(type='bool', default=False),
            minute=dict(type='str', default='*'),
            hour=dict(type='str', default='*'),
            day=dict(type='str', default='*', aliases=['dom']),
            month=dict(type='str', default='*'),
            weekday=dict(type='str', default='*', aliases=['dow']),
            special_time=dict(type='str', choices=["reboot", "yearly", "annually", "monthly", "weekly", "daily", "hourly"]),
            disabled=dict(type='bool', default=False),
            env=dict(type='bool', default=False),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
        ),
        supports_check_mode=True,
        mutually_exclusive=[
            ['insertafter', 'insertbefore'],
        ],
    )

def test_valid_inputs(module):
    module.params = {
        'name': 'test_job',
        'user': 'root',
        'job': 'ls -alh > /dev/null',
        'state': 'present',
        'minute': '*',
        'hour': '*',
        'day': '*',
        'month': '*',
        'weekday': '*',
    }
    main()
    assert module.exit_json.called

def test_edge_cases(module):
    module.params = {
        'name': '',
        'user': None,
        'job': None,
        'state': 'absent',
        'backup': True,
        'minute': 'reboot',
        'hour': 'reboot',
        'day': 'reboot',
        'month': 'reboot',
        'weekday': 'reboot',
    }
    main()
    assert module.exit_json.called

def test_invalid_inputs(module):
    module.params = {
        'name': 'test_job',
        'user': 'root',
        'job': 'ls -alh > /dev/null',
        'state': 'invalid_state',
        'backup': True,
        'minute': 'invalid_minute',
        'hour': 'invalid_hour',
        'day': 'invalid_day',
        'month': 'invalid_month',
        'weekday': 'invalid_weekday',
    }
    with pytest.raises(SystemExit):
        main()
