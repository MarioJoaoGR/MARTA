
import pytest
from ansible.modules.ping import main
from ansible.module_utils.basic import AnsibleModule

def test_valid_input_default_data():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    result = main()
    assert 'ping' in result
    assert result['ping'] == 'pong'

def test_invalid_input_crash():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    with pytest.raises(Exception, match="boom"):
        main(data='crash')

def test_edge_case_none_data():
    module = AnsibleModule(argument_spec=dict(data=dict(type='str', default='pong')), supports_check_mode=True)
    result = main(data=None)
    assert 'ping' in result
    assert result['ping'] is None
