
# Module: ansible.plugins.callback.default
import pytest
from ansible.plugins.callback import default

# Assuming C.COLOR_SKIP is defined somewhere in your code or environment
C = {}  # Placeholder for actual color definitions if needed

class MyCallbackModule(default.CallbackModule):
    def __init__(self):
        super(MyCallbackModule, self).__init__()

@pytest.fixture
def callback_module():
    return MyCallbackModule()

@pytest.fixture
def included_file():
    return type('IncludedFile', (object,), {'_filename': 'example.yml', '_hosts': [{'name': 'host1'}, {'name': 'host2'}], '_vars': {'item': 'example_item'}})()

def test_v2_playbook_on_include(callback_module, included_file):
    # Call the method with the included file object
    callback_module.v2_playbook_on_include(included_file)
    
    # Assert that the message was printed correctly
    expected_message = 'included: example.yml for host1, host2 => (item=example_item)'
    assert callback_module._display.messages[-1][0] == expected_message  # Corrected to match tuple structure
