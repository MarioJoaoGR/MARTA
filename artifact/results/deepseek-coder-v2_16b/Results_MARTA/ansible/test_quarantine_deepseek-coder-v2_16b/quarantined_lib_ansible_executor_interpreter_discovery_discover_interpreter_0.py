
import pytest
from ansible.executor.interpreter_discovery import discover_interpreter

@pytest.mark.parametrize("action, interpreter_name, discovery_mode, task_vars, expected", [
    (None, 'python', '', {'inventory_hostname': 'host1'}, '/usr/bin/python'),
    (None, 'python', 'auto_legacy_silent', {'inventory_hostname': 'host1'}, '/usr/bin/python'),
])
def test_valid_case(action, interpreter_name, discovery_mode, task_vars, expected):
    result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)
    assert result == expected

@pytest.mark.parametrize("action, interpreter_name, discovery_mode", [
    (None, 'python', 'invalid_mode'),
])
def test_invalid_input(action, interpreter_name, discovery_mode):
    with pytest.raises(NotImplementedError):
        discover_interpreter(action, interpreter_name, discovery_mode, {'inventory_hostname': 'host1'})
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery_discover_interpreter_0.py F [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
___________ test_valid_case[None-python--task_vars0-/usr/bin/python] ___________

action = None, interpreter_name = 'python', discovery_mode = ''
task_vars = {'inventory_hostname': 'host1'}, expected = '/usr/bin/python'

    @pytest.mark.parametrize("action, interpreter_name, discovery_mode, task_vars, expected", [
        (None, 'python', '', {'inventory_hostname': 'host1'}, '/usr/bin/python'),
        (None, 'python', 'auto_legacy_silent', {'inventory_hostname': 'host1'}, '/usr/bin/python'),
    ])
    def test_valid_case(action, interpreter_name, discovery_mode, task_vars, expected):
>       result = discover_interpreter(action, interpreter_name, discovery_mode, task_vars)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery_discover_interpreter_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

action = None, interpreter_name = 'python', discovery_mode = ''
task_vars = {'inventory_hostname': 'host1'}

    def discover_interpreter(action, interpreter_name, discovery_mode, task_vars):
        # interpreter discovery is a 2-step process with the target. First, we use a simple shell-agnostic bootstrap to
        # get the system type from uname, and find any random Python that can get us the info we need. For supported
        # target OS types, we'll dispatch a Python script that calls plaform.dist() (for older platforms, where available)
        # and brings back /etc/os-release (if present). The proper Python path is looked up in a table of known
        # distros/versions with included Pythons; if nothing is found, depending on the discovery mode, either the
        # default fallback of /usr/bin/python is used (if we know it's there), or discovery fails.
    
        # FUTURE: add logical equivalence for "python3" in the case of py3-only modules?
        if interpreter_name != 'python':
            raise ValueError('Interpreter discovery not supported for {0}'.format(interpreter_name))
    
        host = task_vars.get('inventory_hostname', 'unknown')
        res = None
        platform_type = 'unknown'
        found_interpreters = [u'/usr/bin/python']  # fallback value
        is_auto_legacy = discovery_mode.startswith('auto_legacy')
        is_silent = discovery_mode.endswith('_silent')
    
        try:
            platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP', variables=task_vars)
            bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables=task_vars)
    
            display.vvv(msg=u"Attempting {0} interpreter discovery".format(interpreter_name), host=host)
    
            # not all command -v impls accept a list of commands, so we have to call it once per python
            command_list = ["command -v '%s'" % py for py in bootstrap_python_list]
            shell_bootstrap = "echo PLATFORM; uname; echo FOUND; {0}; echo ENDFOUND".format('; '.join(command_list))
    
            # FUTURE: in most cases we probably don't want to use become, but maybe sometimes we do?
            res = action._low_level_execute_command(shell_bootstrap, sudoable=False)
    
            raw_stdout = res.get('stdout', u'')
    
            match = foundre.match(raw_stdout)
    
            if not match:
                display.debug(u'raw interpreter discovery output: {0}'.format(raw_stdout), host=host)
                raise ValueError('unexpected output from Python interpreter discovery')
    
            platform_type = match.groups()[0].lower().strip()
    
            found_interpreters = [interp.strip() for interp in match.groups()[1].splitlines() if interp.startswith('/')]
    
            display.debug(u"found interpreters: {0}".format(found_interpreters), host=host)
    
            if not found_interpreters:
                if not is_silent:
                    action._discovery_warnings.append(u'No python interpreters found for '
                                                      u'host {0} (tried {1})'.format(host, bootstrap_python_list))
                # this is lame, but returning None or throwing an exception is uglier
                return u'/usr/bin/python'
    
            if platform_type != 'linux':
                raise NotImplementedError('unsupported platform for extended discovery: {0}'.format(to_native(platform_type)))
    
            platform_script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')
    
            # FUTURE: respect pipelining setting instead of just if the connection supports it?
            if action._connection.has_pipelining:
                res = action._low_level_execute_command(found_interpreters[0], sudoable=False, in_data=platform_script)
            else:
                # FUTURE: implement on-disk case (via script action or ?)
                raise NotImplementedError('pipelining support required for extended interpreter discovery')
    
            platform_info = json.loads(res.get('stdout'))
    
            distro, version = _get_linux_distro(platform_info)
    
            if not distro or not version:
                raise NotImplementedError('unable to get Linux distribution/version info')
    
            version_map = platform_python_map.get(distro.lower().strip())
            if not version_map:
                raise NotImplementedError('unsupported Linux distribution: {0}'.format(distro))
    
            platform_interpreter = to_text(_version_fuzzy_match(version, version_map), errors='surrogate_or_strict')
    
            # provide a transition period for hosts that were using /usr/bin/python previously (but shouldn't have been)
            if is_auto_legacy:
                if platform_interpreter != u'/usr/bin/python' and u'/usr/bin/python' in found_interpreters:
                    if not is_silent:
                        action._discovery_warnings.append(
                            u"Distribution {0} {1} on host {2} should use {3}, but is using "
                            u"/usr/bin/python for backward compatibility with prior Ansible releases. "
                            u"See {4} for more information"
                            .format(distro, version, host, platform_interpreter,
                                    get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
                    return u'/usr/bin/python'
    
            if platform_interpreter not in found_interpreters:
                if platform_interpreter not in bootstrap_python_list:
                    # sanity check to make sure we looked for it
                    if not is_silent:
                        action._discovery_warnings \
                            .append(u"Platform interpreter {0} on host {1} is missing from bootstrap list"
                                    .format(platform_interpreter, host))
    
                if not is_silent:
                    action._discovery_warnings \
                        .append(u"Distribution {0} {1} on host {2} should use {3}, but is using {4}, since the "
                                u"discovered platform python interpreter was not present. See {5} "
                                u"for more information."
                                .format(distro, version, host, platform_interpreter, found_interpreters[0],
                                        get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
                return found_interpreters[0]
    
            return platform_interpreter
        except NotImplementedError as ex:
            display.vvv(msg=u'Python interpreter discovery fallback ({0})'.format(to_text(ex)), host=host)
        except Exception as ex:
            if not is_silent:
                display.warning(msg=u'Unhandled error in Python interpreter discovery for host {0}: {1}'.format(host, to_text(ex)))
                display.debug(msg=u'Interpreter discovery traceback:\n{0}'.format(to_text(format_exc())), host=host)
                if res and res.get('stderr'):
                    display.vvv(msg=u'Interpreter discovery remote stderr:\n{0}'.format(to_text(res.get('stderr'))), host=host)
    
        if not is_silent:
>           action._discovery_warnings \
                .append(u"Platform {0} on host {1} is using the discovered Python interpreter at {2}, but future installation of "
                        u"another Python interpreter could change the meaning of that path. See {3} "
                        u"for more information."
                        .format(platform_type, host, found_interpreters[0],
                                get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
E           AttributeError: 'NoneType' object has no attribute '_discovery_warnings'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/interpreter_discovery.py:156: AttributeError
----------------------------- Captured stderr call -----------------------------
[WARNING]: Unhandled error in Python interpreter discovery for host host1:
'NoneType' object has no attribute '_low_level_execute_command'
_________________ test_invalid_input[None-python-invalid_mode] _________________

action = None, interpreter_name = 'python', discovery_mode = 'invalid_mode'

    @pytest.mark.parametrize("action, interpreter_name, discovery_mode", [
        (None, 'python', 'invalid_mode'),
    ])
    def test_invalid_input(action, interpreter_name, discovery_mode):
        with pytest.raises(NotImplementedError):
>           discover_interpreter(action, interpreter_name, discovery_mode, {'inventory_hostname': 'host1'})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery_discover_interpreter_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

action = None, interpreter_name = 'python', discovery_mode = 'invalid_mode'
task_vars = {'inventory_hostname': 'host1'}

    def discover_interpreter(action, interpreter_name, discovery_mode, task_vars):
        # interpreter discovery is a 2-step process with the target. First, we use a simple shell-agnostic bootstrap to
        # get the system type from uname, and find any random Python that can get us the info we need. For supported
        # target OS types, we'll dispatch a Python script that calls plaform.dist() (for older platforms, where available)
        # and brings back /etc/os-release (if present). The proper Python path is looked up in a table of known
        # distros/versions with included Pythons; if nothing is found, depending on the discovery mode, either the
        # default fallback of /usr/bin/python is used (if we know it's there), or discovery fails.
    
        # FUTURE: add logical equivalence for "python3" in the case of py3-only modules?
        if interpreter_name != 'python':
            raise ValueError('Interpreter discovery not supported for {0}'.format(interpreter_name))
    
        host = task_vars.get('inventory_hostname', 'unknown')
        res = None
        platform_type = 'unknown'
        found_interpreters = [u'/usr/bin/python']  # fallback value
        is_auto_legacy = discovery_mode.startswith('auto_legacy')
        is_silent = discovery_mode.endswith('_silent')
    
        try:
            platform_python_map = C.config.get_config_value('INTERPRETER_PYTHON_DISTRO_MAP', variables=task_vars)
            bootstrap_python_list = C.config.get_config_value('INTERPRETER_PYTHON_FALLBACK', variables=task_vars)
    
            display.vvv(msg=u"Attempting {0} interpreter discovery".format(interpreter_name), host=host)
    
            # not all command -v impls accept a list of commands, so we have to call it once per python
            command_list = ["command -v '%s'" % py for py in bootstrap_python_list]
            shell_bootstrap = "echo PLATFORM; uname; echo FOUND; {0}; echo ENDFOUND".format('; '.join(command_list))
    
            # FUTURE: in most cases we probably don't want to use become, but maybe sometimes we do?
            res = action._low_level_execute_command(shell_bootstrap, sudoable=False)
    
            raw_stdout = res.get('stdout', u'')
    
            match = foundre.match(raw_stdout)
    
            if not match:
                display.debug(u'raw interpreter discovery output: {0}'.format(raw_stdout), host=host)
                raise ValueError('unexpected output from Python interpreter discovery')
    
            platform_type = match.groups()[0].lower().strip()
    
            found_interpreters = [interp.strip() for interp in match.groups()[1].splitlines() if interp.startswith('/')]
    
            display.debug(u"found interpreters: {0}".format(found_interpreters), host=host)
    
            if not found_interpreters:
                if not is_silent:
                    action._discovery_warnings.append(u'No python interpreters found for '
                                                      u'host {0} (tried {1})'.format(host, bootstrap_python_list))
                # this is lame, but returning None or throwing an exception is uglier
                return u'/usr/bin/python'
    
            if platform_type != 'linux':
                raise NotImplementedError('unsupported platform for extended discovery: {0}'.format(to_native(platform_type)))
    
            platform_script = pkgutil.get_data('ansible.executor.discovery', 'python_target.py')
    
            # FUTURE: respect pipelining setting instead of just if the connection supports it?
            if action._connection.has_pipelining:
                res = action._low_level_execute_command(found_interpreters[0], sudoable=False, in_data=platform_script)
            else:
                # FUTURE: implement on-disk case (via script action or ?)
                raise NotImplementedError('pipelining support required for extended interpreter discovery')
    
            platform_info = json.loads(res.get('stdout'))
    
            distro, version = _get_linux_distro(platform_info)
    
            if not distro or not version:
                raise NotImplementedError('unable to get Linux distribution/version info')
    
            version_map = platform_python_map.get(distro.lower().strip())
            if not version_map:
                raise NotImplementedError('unsupported Linux distribution: {0}'.format(distro))
    
            platform_interpreter = to_text(_version_fuzzy_match(version, version_map), errors='surrogate_or_strict')
    
            # provide a transition period for hosts that were using /usr/bin/python previously (but shouldn't have been)
            if is_auto_legacy:
                if platform_interpreter != u'/usr/bin/python' and u'/usr/bin/python' in found_interpreters:
                    if not is_silent:
                        action._discovery_warnings.append(
                            u"Distribution {0} {1} on host {2} should use {3}, but is using "
                            u"/usr/bin/python for backward compatibility with prior Ansible releases. "
                            u"See {4} for more information"
                            .format(distro, version, host, platform_interpreter,
                                    get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
                    return u'/usr/bin/python'
    
            if platform_interpreter not in found_interpreters:
                if platform_interpreter not in bootstrap_python_list:
                    # sanity check to make sure we looked for it
                    if not is_silent:
                        action._discovery_warnings \
                            .append(u"Platform interpreter {0} on host {1} is missing from bootstrap list"
                                    .format(platform_interpreter, host))
    
                if not is_silent:
                    action._discovery_warnings \
                        .append(u"Distribution {0} {1} on host {2} should use {3}, but is using {4}, since the "
                                u"discovered platform python interpreter was not present. See {5} "
                                u"for more information."
                                .format(distro, version, host, platform_interpreter, found_interpreters[0],
                                        get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
                return found_interpreters[0]
    
            return platform_interpreter
        except NotImplementedError as ex:
            display.vvv(msg=u'Python interpreter discovery fallback ({0})'.format(to_text(ex)), host=host)
        except Exception as ex:
            if not is_silent:
                display.warning(msg=u'Unhandled error in Python interpreter discovery for host {0}: {1}'.format(host, to_text(ex)))
                display.debug(msg=u'Interpreter discovery traceback:\n{0}'.format(to_text(format_exc())), host=host)
                if res and res.get('stderr'):
                    display.vvv(msg=u'Interpreter discovery remote stderr:\n{0}'.format(to_text(res.get('stderr'))), host=host)
    
        if not is_silent:
>           action._discovery_warnings \
                .append(u"Platform {0} on host {1} is using the discovered Python interpreter at {2}, but future installation of "
                        u"another Python interpreter could change the meaning of that path. See {3} "
                        u"for more information."
                        .format(platform_type, host, found_interpreters[0],
                                get_versioned_doclink('reference_appendices/interpreter_discovery.html')))
E           AttributeError: 'NoneType' object has no attribute '_discovery_warnings'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/executor/interpreter_discovery.py:156: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery_discover_interpreter_0.py::test_valid_case[None-python--task_vars0-/usr/bin/python]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_interpreter_discovery_discover_interpreter_0.py::test_invalid_input[None-python-invalid_mode]
========================= 2 failed, 1 passed in 0.31s ==========================
"""