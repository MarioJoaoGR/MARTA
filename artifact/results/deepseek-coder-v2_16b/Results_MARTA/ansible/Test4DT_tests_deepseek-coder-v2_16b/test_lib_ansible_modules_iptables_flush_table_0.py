
import pytest
from ansible.modules.iptables import flush_table, push_arguments



def test_invalid_input():
    iptables_path = '/usr/sbin/iptables'
    module_obj = None  # Assuming a real module object for testing purposes
    params = {'chain': 'INPUT'}  # Missing 'table' key in params
    
    with pytest.raises(KeyError):
        flush_table(iptables_path, module_obj, params)