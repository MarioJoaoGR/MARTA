
import pytest
from ansible.playbook.helpers import load_list_of_tasks
from ansible.errors import AnsibleParserError


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_helpers_load_list_of_tasks_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_inputs_happy_path _________________________

    def test_valid_inputs_happy_path():
        ds = [{'name': 'task1'}, {'block': True}, {'name': 'task2'}]
        play = {}
>       tasks = load_list_of_tasks(ds, play)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_helpers_load_list_of_tasks_1.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/helpers.py:122: in load_list_of_tasks
    (action, args, delegate_to) = args_parser.parse(skip_action_validation=True)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.parsing.mod_args.ModuleArgsParser object at 0x7fddc05cd180>
skip_action_validation = True

    def parse(self, skip_action_validation=False):
        '''
        Given a task in one of the supported forms, parses and returns
        returns the action, arguments, and delegate_to values for the
        task, dealing with all sorts of levels of fuzziness.
        '''
    
        thing = None
    
        action = None
        delegate_to = self._task_ds.get('delegate_to', Sentinel)
        args = dict()
    
        # This is the standard YAML form for command-type modules. We grab
        # the args and pass them in as additional arguments, which can/will
        # be overwritten via dict updates from the other arg sources below
        additional_args = self._task_ds.get('args', dict())
    
        # We can have one of action, local_action, or module specified
        # action
        if 'action' in self._task_ds:
            # an old school 'action' statement
            thing = self._task_ds['action']
            action, args = self._normalize_parameters(thing, action=action, additional_args=additional_args)
    
        # local_action
        if 'local_action' in self._task_ds:
            # local_action is similar but also implies a delegate_to
            if action is not None:
                raise AnsibleParserError("action and local_action are mutually exclusive", obj=self._task_ds)
            thing = self._task_ds.get('local_action', '')
            delegate_to = 'localhost'
            action, args = self._normalize_parameters(thing, action=action, additional_args=additional_args)
    
        # module: <stuff> is the more new-style invocation
    
        # filter out task attributes so we're only querying unrecognized keys as actions/modules
        non_task_ds = dict((k, v) for k, v in iteritems(self._task_ds) if (k not in self._task_attrs) and (not k.startswith('with_')))
    
        # walk the filtered input dictionary to see if we recognize a module name
        for item, value in iteritems(non_task_ds):
            context = None
            is_action_candidate = False
            if item in BUILTIN_TASKS:
                is_action_candidate = True
            elif skip_action_validation:
                is_action_candidate = True
            else:
                context = action_loader.find_plugin_with_context(item, collection_list=self._collection_list)
                if not context.resolved:
                    context = module_loader.find_plugin_with_context(item, collection_list=self._collection_list)
    
                is_action_candidate = context.resolved and bool(context.redirect_list)
    
            if is_action_candidate:
                # finding more than one module name is a problem
                if action is not None:
                    raise AnsibleParserError("conflicting action statements: %s, %s" % (action, item), obj=self._task_ds)
    
                if context is not None and context.resolved:
                    self.resolved_action = context.resolved_fqcn
    
                action = item
                thing = value
                action, args = self._normalize_parameters(thing, action=action, additional_args=additional_args)
    
        # if we didn't see any module in the task at all, it's not a task really
        if action is None:
            if non_task_ds:  # there was one non-task action, but we couldn't find it
                bad_action = list(non_task_ds.keys())[0]
                raise AnsibleParserError("couldn't resolve module/action '{0}'. This often indicates a "
                                         "misspelling, missing collection, or incorrect module path.".format(bad_action),
                                         obj=self._task_ds)
            else:
>               raise AnsibleParserError("no module/action detected in task.",
E               ansible.errors.AnsibleParserError: no module/action detected in task.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/parsing/mod_args.py:334: AnsibleParserError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        ds = [{'invalid': 'data'}]
        play = {}
        with pytest.raises(AnsibleParserError) as excinfo:
            load_list_of_tasks(ds, play)
>       assert "no module/action detected in task" in str(excinfo.value), "Expected an error about missing module/action"
E       AssertionError: Expected an error about missing module/action
E       assert 'no module/action detected in task' in "this task 'invalid' has extra params, which is only allowed in the following modules: ansible.builtin.raw, ansible.le...legacy.include, ansible.windows.win_shell, ansible.legacy.shell, ansible.legacy.import_role, ansible.builtin.win_shell"
E        +  where "this task 'invalid' has extra params, which is only allowed in the following modules: ansible.builtin.raw, ansible.le...legacy.include, ansible.windows.win_shell, ansible.legacy.shell, ansible.legacy.import_role, ansible.builtin.win_shell" = str(this task 'invalid' has extra params, which is only allowed in the following modules: ansible.builtin.raw, ansible.leg....legacy.include, ansible.windows.win_shell, ansible.legacy.shell, ansible.legacy.import_role, ansible.builtin.win_shell)
E        +    where this task 'invalid' has extra params, which is only allowed in the following modules: ansible.builtin.raw, ansible.leg....legacy.include, ansible.windows.win_shell, ansible.legacy.shell, ansible.legacy.import_role, ansible.builtin.win_shell = <ExceptionInfo this task 'invalid' has extra params, which is only allowed in the following modules: ansible.builtin.r...nclude, ansible.windows.win_shell, ansible.legacy.shell, ansible.legacy.import_role, ansible.builtin.win_shell tblen=3>.value

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_helpers_load_list_of_tasks_1.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_helpers_load_list_of_tasks_1.py::test_valid_inputs_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_helpers_load_list_of_tasks_1.py::test_invalid_inputs
============================== 2 failed in 0.49s ===============================
"""