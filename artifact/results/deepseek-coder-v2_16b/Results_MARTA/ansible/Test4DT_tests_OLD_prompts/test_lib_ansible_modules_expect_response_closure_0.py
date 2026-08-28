
import pytest
from unittest.mock import patch, MagicMock
from ansible.modules.expect import response_closure

@pytest.fixture(scope="function")
def setup():
    module = MagicMock()
    responses = ["Response 1", "Response 2", "Response 3"]
    resp_func = response_closure(module, "What is your favorite color?", responses)
    return module, resp_func

def test_response_closure_basic(setup):
    module, resp_func = setup
    info = {'child_result_list': ['blue', 'green']}
    assert resp_func(info) == b"Response 1\n"
