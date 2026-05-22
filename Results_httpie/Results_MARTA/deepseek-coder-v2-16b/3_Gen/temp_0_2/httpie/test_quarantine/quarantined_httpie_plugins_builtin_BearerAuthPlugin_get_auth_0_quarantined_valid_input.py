
import pytest
from httpie.plugins.builtin import BearerAuthPlugin

@pytest.fixture
def plugin():
    return BearerAuthPlugin("your_bearer_token")

def test_get_auth(plugin):
    auth = plugin.get_auth()
    assert isinstance(auth, HTTPBearerAuth)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_plugins_builtin_BearerAuthPlugin_get_auth_0_test_valid_input
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_plugins_builtin_BearerAuthPlugin_get_auth_0_test_valid_input.py:11:28: E0602: Undefined variable 'HTTPBearerAuth' (undefined-variable)


"""