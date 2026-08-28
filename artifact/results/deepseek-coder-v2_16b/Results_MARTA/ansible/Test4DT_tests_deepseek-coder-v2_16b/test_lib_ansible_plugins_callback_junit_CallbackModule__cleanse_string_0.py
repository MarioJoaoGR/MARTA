
import pytest
from ansible.plugins.callback import junit as junit_module
import os

@pytest.fixture(scope="function")
def setup_real_instance():
    callback = junit_module.CallbackModule()
    return callback

def test_valid_inputs(setup_real_instance):
    callback = setup_real_instance
    assert isinstance(callback, junit_module.CallbackModule), "Instance is not of type CallbackModule"
    assert os.getenv('JUNIT_OUTPUT_DIR', os.path.expanduser('~/.ansible.log')) == callback._output_dir, "Output directory does not match expected value"
