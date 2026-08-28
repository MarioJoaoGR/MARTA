
import pytest
from ansible.vars.hostvars import HostVarsVars
from collections import defaultdict

# Mock Templar and STATIC_VARS for testing purposes
class MockTemplar:
    def __init__(self, variables, loader):
        self._variables = variables
        self._loader = loader

    def template(self, var, fail_on_undefined=False, static_vars=None):
        return self._variables[var] if not fail_on_undefined else None

STATIC_VARS = {}

class MockLoader:
    def get_vars(self, host):
        if host == "localhost":
            return {"cpu": 2, "memory": "4GB"}
        else:
            return {}

# Test cases for HostVarsVars class
def test_hostvars_initialization():
    variables = {'host1': {'key1': 'value1'}, 'host2': {'key2': 'value2'}}
    loader = MockLoader()
    hostvars = HostVarsVars(variables, loader)
    assert len(hostvars._vars) == 2

def test_getitem_existing_variable():
    variables = {'localhost': {'cpu': 2, 'memory': '4GB'}}
    loader = MockLoader()
    hostvars = HostVarsVars(variables, loader)