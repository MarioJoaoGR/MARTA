
import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.task_include import TaskInclude



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_load_with_valid_data ___________________________

    def test_load_with_valid_data():
        data = {
            'file': 'path/to/task',
            '_raw_params': {'action': 'some_action', 'args': {'arg1': 'value1'}}
        }
>       task = TaskInclude.load(data=data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task_include.py:57: in load
    ti.load_data(data, variable_manager=variable_manager, loader=loader),
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:269: in load_data
    ds = self.preprocess_data(ds)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task_include.py:91: in preprocess_data
    ds = super(TaskInclude, self).preprocess_data(ds)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task.py:207: in preprocess_data
    (action, args, delegate_to) = args_parser.parse()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.parsing.mod_args.ModuleArgsParser object at 0x7f8dc5901660>
skip_action_validation = False

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
                raise AnsibleParserError("no module/action detected in task.",
                                         obj=self._task_ds)
        elif args.get('_raw_params', '') != '' and action not in RAW_PARAM_MODULES:
            templar = Templar(loader=None)
            raw_params = args.pop('_raw_params')
            if templar.is_template(raw_params):
                args['_variable_params'] = raw_params
            else:
>               raise AnsibleParserError("this task '%s' has extra params, which is only allowed in the following modules: %s" % (action,
                                                                                                                                  ", ".join(RAW_PARAM_MODULES)),
                                         obj=self._task_ds)
E               ansible.errors.AnsibleParserError: this task 'file' has extra params, which is only allowed in the following modules: ansible.legacy.import_role, ansible.legacy.shell, ansible.legacy.set_fact, ansible.builtin.include_role, ansible.legacy.add_host, ansible.builtin.include_tasks, ansible.legacy.include_vars, ansible.builtin.command, ansible.builtin.win_shell, ansible.builtin.win_command, ansible.builtin.raw, include, ansible.builtin.set_fact, ansible.legacy.group_by, command, ansible.builtin.add_host, ansible.builtin.group_by, ansible.legacy.include, shell, include_vars, ansible.legacy.script, group_by, ansible.legacy.include_role, ansible.builtin.import_tasks, ansible.windows.win_command, import_role, win_shell, import_tasks, ansible.builtin.meta, ansible.legacy.win_command, ansible.builtin.shell, raw, ansible.legacy.include_tasks, set_fact, ansible.builtin.import_role, add_host, ansible.legacy.raw, meta, ansible.legacy.win_shell, ansible.legacy.import_tasks, ansible.windows.win_shell, script, ansible.legacy.command, ansible.builtin.script, include_tasks, include_role, ansible.builtin.include_vars, ansible.builtin.include, win_command, ansible.legacy.meta

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/parsing/mod_args.py:342: AnsibleParserError
___________________ test_check_options_with_invalid_options ____________________

    def test_check_options_with_invalid_options():
        ti = TaskInclude()
        with pytest.raises(AnsibleParserError):
>           validated_task = ti.check_options(task={'invalid': 'option'}, data={})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = TASK: None, task = {'invalid': 'option'}, data = {}

    def check_options(self, task, data):
        '''
        Method for options validation to use in 'load_data' for TaskInclude and HandlerTaskInclude
        since they share the same validations. It is not named 'validate_options' on purpose
        to prevent confusion with '_validate_*" methods. Note that the task passed might be changed
        as a side-effect of this method.
        '''
>       my_arg_names = frozenset(task.args.keys())
E       AttributeError: 'dict' object has no attribute 'args'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task_include.py:70: AttributeError
____________________ test_check_options_with_valid_options _____________________

    def test_check_options_with_valid_options():
        ti = TaskInclude()
        task = {'action': 'some_action', '_raw_params': {'args': {'arg1': 'value1'}}}
>       validated_task = ti.check_options(task=task, data={})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = TASK: None
task = {'_raw_params': {'args': {'arg1': 'value1'}}, 'action': 'some_action'}
data = {}

    def check_options(self, task, data):
        '''
        Method for options validation to use in 'load_data' for TaskInclude and HandlerTaskInclude
        since they share the same validations. It is not named 'validate_options' on purpose
        to prevent confusion with '_validate_*" methods. Note that the task passed might be changed
        as a side-effect of this method.
        '''
>       my_arg_names = frozenset(task.args.keys())
E       AttributeError: 'dict' object has no attribute 'args'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/task_include.py:70: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py::test_load_with_valid_data
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py::test_check_options_with_invalid_options
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_task_include_TaskInclude_load_2.py::test_check_options_with_valid_options
============================== 3 failed in 1.01s ===============================
"""