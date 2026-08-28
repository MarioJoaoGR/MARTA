# Module: ansible.plugins.action.debug
import pytest
from ansible.plugins.action import ActionModule as AnsibleActionModule
from ansible.errors import AnsibleUndefinedVariable
from ansible.utils.unicode import string_types, to_text

# Assuming self is bound to an instance of ActionModule
class TestActionModule:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.action = AnsibleActionModule()
        self.action._task = type('Task', (object,), {'args': {}})()
        self.action._display = type('Display', (object,), {'verbosity': 0})()
        self.action._templar = type('_Templar', (object,), {})()

    def test_run_with_msg_only(self):
        self.action._task.args['msg'] = 'This is a custom message'
        result = self.action.run()
        assert not result['failed']
        assert result['msg'] == 'This is a custom message'
        assert '_ansible_verbose_always' in result

    def test_run_with_var_only(self):
        self.action._task.args['var'] = '{{ some_variable }}'
        self.action._display.verbosity = 2
        result = self.action.run()
        assert not result['failed']
        assert isinstance(result[to_text(type({}))], str)

    def test_run_with_msg_and_var_incompatible(self):
        self.action._task.args['msg'] = 'This is a custom message'
        self.action._task.args['var'] = '{{ some_variable }}'
        with pytest.raises(Exception) as e:
            self.action.run()
        assert "'msg' and 'var' are incompatible options" in str(e.value)

    def test_run_with_verbosity_high_enough_for_template_processing(self):
        self.action._task.args['msg'] = 'This is a custom message'
        self.action._task.args['var'] = '{{ some_variable }}'
        self.action._display.verbosity = 3
        result = self.action.run()
        assert not result['failed']
        assert isinstance(result[to_text(type({}))], str)

    def test_run_handling_skip_logic_due_to_insufficient_verbosity(self):
        self.action._task.args['msg'] = 'This is a custom message'
        self.action._task.args['var'] = '{{ some_variable }}'
        self.action._display.verbosity = 1
        result = self.action.run()
        assert not result['failed']
        assert result['skipped']
        assert result['skipped_reason'] == "Verbosity threshold not met."
