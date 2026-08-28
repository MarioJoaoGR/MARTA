
import pytest
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError, AnsibleError

# Test case for updating configuration data with invalid type

# Test case for updating configuration data with None input

# Test case for updating configuration data with empty dictionary
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________ test_update_config_data_with_invalid_type ___________________

self = <ansible.config.manager.ConfigManager object at 0x7f09961d5780>
defs = {'log_level': {'type': 'invalid'}}, configfile = None

    def update_config_data(self, defs=None, configfile=None):
        ''' really: update constants '''
    
        if defs is None:
            defs = self._base_defs
    
        if configfile is None:
            configfile = self._config_file
    
        if not isinstance(defs, dict):
            raise AnsibleOptionsError("Invalid configuration definition type: %s for %s" % (type(defs), defs))
    
        # update the constant for config file
        self.data.update_setting(Setting('CONFIG_FILE', configfile, '', 'string'))
    
        origin = None
        # env and config defs can have several entries, ordered in list from lowest to highest precedence
        for config in defs:
            if not isinstance(defs[config], dict):
                raise AnsibleOptionsError("Invalid configuration definition '%s': type is %s" % (to_native(config), type(defs[config])))
    
            # get value and origin
            try:
>               value, origin = self.get_config_value_and_origin(config, configfile)

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:592: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7f09961d5780>
config = 'log_level', cfile = None, plugin_type = None, plugin_name = None
keys = None, variables = None, direct = None

    def get_config_value_and_origin(self, config, cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None):
        ''' Given a config key figure out the actual value and report on the origin of the settings '''
        if cfile is None:
            # use default config
            cfile = self._config_file
    
        # Note: sources that are lists listed in low to high precedence (last one wins)
        value = None
        origin = None
    
        defs = self.get_configuration_definitions(plugin_type, plugin_name)
        if config in defs:
    
            aliases = defs[config].get('aliases', [])
    
            # direct setting via plugin arguments, can set to None so we bypass rest of processing/defaults
            direct_aliases = []
            if direct:
                direct_aliases = [direct[alias] for alias in aliases if alias in direct]
            if direct and config in direct:
                value = direct[config]
                origin = 'Direct'
            elif direct and direct_aliases:
                value = direct_aliases[0]
                origin = 'Direct'
    
            else:
                # Use 'variable overrides' if present, highest precedence, but only present when querying running play
                if variables and defs[config].get('vars'):
                    value, origin = self._loop_entries(variables, defs[config]['vars'])
                    origin = 'var: %s' % origin
    
                # use playbook keywords if you have em
                if value is None and keys:
                    if config in keys:
                        value = keys[config]
                        keyword = config
    
                    elif aliases:
                        for alias in aliases:
                            if alias in keys:
                                value = keys[alias]
                                keyword = alias
                                break
    
                    if value is not None:
                        origin = 'keyword: %s' % keyword
    
                if value is None and 'cli' in defs[config]:
                    # avoid circular import .. until valid
                    from ansible import context
                    value, origin = self._loop_entries(context.CLIARGS, defs[config]['cli'])
                    origin = 'cli: %s' % origin
    
                # env vars are next precedence
                if value is None and defs[config].get('env'):
                    value, origin = self._loop_entries(py3compat.environ, defs[config]['env'])
                    origin = 'env: %s' % origin
    
                # try config file entries next, if we have one
                if self._parsers.get(cfile, None) is None:
                    self._parse_config_file(cfile)
    
                if value is None and cfile is not None:
                    ftype = get_config_type(cfile)
                    if ftype and defs[config].get(ftype):
                        if ftype == 'ini':
                            # load from ini config
                            try:  # FIXME: generalize _loop_entries to allow for files also, most of this code is dupe
                                for ini_entry in defs[config]['ini']:
                                    temp_value = get_ini_config_value(self._parsers[cfile], ini_entry)
                                    if temp_value is not None:
                                        value = temp_value
                                        origin = cfile
                                        if 'deprecated' in ini_entry:
                                            self.DEPRECATED.append(('[%s]%s' % (ini_entry['section'], ini_entry['key']), ini_entry['deprecated']))
                            except Exception as e:
                                sys.stderr.write("Error while loading ini config %s: %s" % (cfile, to_native(e)))
                        elif ftype == 'yaml':
                            # FIXME: implement, also , break down key from defs (. notation???)
                            origin = cfile
    
                # set default if we got here w/o a value
                if value is None:
                    if defs[config].get('required', False):
                        if not plugin_type or config not in INTERNAL_DEFS.get(plugin_type, {}):
                            raise AnsibleError("No setting was provided for required configuration %s" %
                                               to_native(_get_entry(plugin_type, plugin_name, config)))
                    else:
                        value = defs[config].get('default')
                        origin = 'default'
                        # skip typing as this is a templated default that will be resolved later in constants, which has needed vars
                        if plugin_type is None and isinstance(value, string_types) and (value.startswith('{{') and value.endswith('}}')):
                            return value, origin
    
            # ensure correct type, can raise exceptions on mismatched types
            try:
                value = ensure_type(value, defs[config].get('type'), origin=origin)
            except ValueError as e:
                if origin.startswith('env:') and value == '':
                    # this is empty env var for non string so we can set to default
                    origin = 'default'
                    value = ensure_type(defs[config].get('default'), defs[config].get('type'), origin=origin)
                else:
                    raise AnsibleOptionsError('Invalid type for configuration option %s: %s' %
                                              (to_native(_get_entry(plugin_type, plugin_name, config)), to_native(e)))
    
            # deal with restricted values
            if value is not None and 'choices' in defs[config] and defs[config]['choices'] is not None:
                invalid_choices = True  # assume the worst!
                if defs[config].get('type') == 'list':
                    # for a list type, compare all values in type are allowed
                    invalid_choices = not all(choice in defs[config]['choices'] for choice in value)
                else:
                    # these should be only the simple data types (string, int, bool, float, etc) .. ignore dicts for now
                    invalid_choices = value not in defs[config]['choices']
    
                if invalid_choices:
                    raise AnsibleOptionsError('Invalid value "%s" for configuration option "%s", valid values are: %s' %
                                              (value, to_native(_get_entry(plugin_type, plugin_name, config)), defs[config]['choices']))
    
            # deal with deprecation of the setting
            if 'deprecated' in defs[config] and origin != 'default':
                self.DEPRECATED.append((config, defs[config].get('deprecated')))
        else:
>           raise AnsibleError('Requested entry (%s) was not defined in configuration.' % to_native(_get_entry(plugin_type, plugin_name, config)))
E           ansible.errors.AnsibleError: Requested entry (setting: log_level ) was not defined in configuration.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:558: AnsibleError

During handling of the above exception, another exception occurred:

    def test_update_config_data_with_invalid_type():
        config_manager = ConfigManager()
        with pytest.raises(AnsibleOptionsError):
>           config_manager.update_config_data(defs={'log_level': {'type': 'invalid'}})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7f09961d5780>
defs = {'log_level': {'type': 'invalid'}}, configfile = None

    def update_config_data(self, defs=None, configfile=None):
        ''' really: update constants '''
    
        if defs is None:
            defs = self._base_defs
    
        if configfile is None:
            configfile = self._config_file
    
        if not isinstance(defs, dict):
            raise AnsibleOptionsError("Invalid configuration definition type: %s for %s" % (type(defs), defs))
    
        # update the constant for config file
        self.data.update_setting(Setting('CONFIG_FILE', configfile, '', 'string'))
    
        origin = None
        # env and config defs can have several entries, ordered in list from lowest to highest precedence
        for config in defs:
            if not isinstance(defs[config], dict):
                raise AnsibleOptionsError("Invalid configuration definition '%s': type is %s" % (to_native(config), type(defs[config])))
    
            # get value and origin
            try:
                value, origin = self.get_config_value_and_origin(config, configfile)
            except Exception as e:
                # Printing the problem here because, in the current code:
                # (1) we can't reach the error handler for AnsibleError before we
                #     hit a different error due to lack of working config.
                # (2) We don't have access to display yet because display depends on config
                #     being properly loaded.
                #
                # If we start getting double errors printed from this section of code, then the
                # above problem #1 has been fixed.  Revamp this to be more like the try: except
                # in get_config_value() at that time.
                sys.stderr.write("Unhandled error:\n %s\n\n" % traceback.format_exc())
>               raise AnsibleError("Invalid settings supplied for %s: %s\n" % (config, to_native(e)), orig_exc=e)
E               ansible.errors.AnsibleError: Invalid settings supplied for log_level: Requested entry (setting: log_level ) was not defined in configuration.
E               . Requested entry (setting: log_level ) was not defined in configuration.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:604: AnsibleError
----------------------------- Captured stderr call -----------------------------
Unhandled error:
 Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py", line 592, in update_config_data
    value, origin = self.get_config_value_and_origin(config, configfile)
  File "/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py", line 558, in get_config_value_and_origin
    raise AnsibleError('Requested entry (%s) was not defined in configuration.' % to_native(_get_entry(plugin_type, plugin_name, config)))
ansible.errors.AnsibleError: Requested entry (setting: log_level ) was not defined in configuration.


___________________ test_update_config_data_with_none_input ____________________

    def test_update_config_data_with_none_input():
        config_manager = ConfigManager()
>       with pytest.raises(AnsibleOptionsError):
E       Failed: DID NOT RAISE <class 'ansible.errors.AnsibleOptionsError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py:15: Failed
___________________ test_update_config_data_with_empty_dict ____________________

self = <ansible.config.manager.ConfigManager object at 0x7f0995f7a950>
defs = {'log_level': {}}, configfile = None

    def update_config_data(self, defs=None, configfile=None):
        ''' really: update constants '''
    
        if defs is None:
            defs = self._base_defs
    
        if configfile is None:
            configfile = self._config_file
    
        if not isinstance(defs, dict):
            raise AnsibleOptionsError("Invalid configuration definition type: %s for %s" % (type(defs), defs))
    
        # update the constant for config file
        self.data.update_setting(Setting('CONFIG_FILE', configfile, '', 'string'))
    
        origin = None
        # env and config defs can have several entries, ordered in list from lowest to highest precedence
        for config in defs:
            if not isinstance(defs[config], dict):
                raise AnsibleOptionsError("Invalid configuration definition '%s': type is %s" % (to_native(config), type(defs[config])))
    
            # get value and origin
            try:
>               value, origin = self.get_config_value_and_origin(config, configfile)

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:592: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7f0995f7a950>
config = 'log_level', cfile = None, plugin_type = None, plugin_name = None
keys = None, variables = None, direct = None

    def get_config_value_and_origin(self, config, cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None):
        ''' Given a config key figure out the actual value and report on the origin of the settings '''
        if cfile is None:
            # use default config
            cfile = self._config_file
    
        # Note: sources that are lists listed in low to high precedence (last one wins)
        value = None
        origin = None
    
        defs = self.get_configuration_definitions(plugin_type, plugin_name)
        if config in defs:
    
            aliases = defs[config].get('aliases', [])
    
            # direct setting via plugin arguments, can set to None so we bypass rest of processing/defaults
            direct_aliases = []
            if direct:
                direct_aliases = [direct[alias] for alias in aliases if alias in direct]
            if direct and config in direct:
                value = direct[config]
                origin = 'Direct'
            elif direct and direct_aliases:
                value = direct_aliases[0]
                origin = 'Direct'
    
            else:
                # Use 'variable overrides' if present, highest precedence, but only present when querying running play
                if variables and defs[config].get('vars'):
                    value, origin = self._loop_entries(variables, defs[config]['vars'])
                    origin = 'var: %s' % origin
    
                # use playbook keywords if you have em
                if value is None and keys:
                    if config in keys:
                        value = keys[config]
                        keyword = config
    
                    elif aliases:
                        for alias in aliases:
                            if alias in keys:
                                value = keys[alias]
                                keyword = alias
                                break
    
                    if value is not None:
                        origin = 'keyword: %s' % keyword
    
                if value is None and 'cli' in defs[config]:
                    # avoid circular import .. until valid
                    from ansible import context
                    value, origin = self._loop_entries(context.CLIARGS, defs[config]['cli'])
                    origin = 'cli: %s' % origin
    
                # env vars are next precedence
                if value is None and defs[config].get('env'):
                    value, origin = self._loop_entries(py3compat.environ, defs[config]['env'])
                    origin = 'env: %s' % origin
    
                # try config file entries next, if we have one
                if self._parsers.get(cfile, None) is None:
                    self._parse_config_file(cfile)
    
                if value is None and cfile is not None:
                    ftype = get_config_type(cfile)
                    if ftype and defs[config].get(ftype):
                        if ftype == 'ini':
                            # load from ini config
                            try:  # FIXME: generalize _loop_entries to allow for files also, most of this code is dupe
                                for ini_entry in defs[config]['ini']:
                                    temp_value = get_ini_config_value(self._parsers[cfile], ini_entry)
                                    if temp_value is not None:
                                        value = temp_value
                                        origin = cfile
                                        if 'deprecated' in ini_entry:
                                            self.DEPRECATED.append(('[%s]%s' % (ini_entry['section'], ini_entry['key']), ini_entry['deprecated']))
                            except Exception as e:
                                sys.stderr.write("Error while loading ini config %s: %s" % (cfile, to_native(e)))
                        elif ftype == 'yaml':
                            # FIXME: implement, also , break down key from defs (. notation???)
                            origin = cfile
    
                # set default if we got here w/o a value
                if value is None:
                    if defs[config].get('required', False):
                        if not plugin_type or config not in INTERNAL_DEFS.get(plugin_type, {}):
                            raise AnsibleError("No setting was provided for required configuration %s" %
                                               to_native(_get_entry(plugin_type, plugin_name, config)))
                    else:
                        value = defs[config].get('default')
                        origin = 'default'
                        # skip typing as this is a templated default that will be resolved later in constants, which has needed vars
                        if plugin_type is None and isinstance(value, string_types) and (value.startswith('{{') and value.endswith('}}')):
                            return value, origin
    
            # ensure correct type, can raise exceptions on mismatched types
            try:
                value = ensure_type(value, defs[config].get('type'), origin=origin)
            except ValueError as e:
                if origin.startswith('env:') and value == '':
                    # this is empty env var for non string so we can set to default
                    origin = 'default'
                    value = ensure_type(defs[config].get('default'), defs[config].get('type'), origin=origin)
                else:
                    raise AnsibleOptionsError('Invalid type for configuration option %s: %s' %
                                              (to_native(_get_entry(plugin_type, plugin_name, config)), to_native(e)))
    
            # deal with restricted values
            if value is not None and 'choices' in defs[config] and defs[config]['choices'] is not None:
                invalid_choices = True  # assume the worst!
                if defs[config].get('type') == 'list':
                    # for a list type, compare all values in type are allowed
                    invalid_choices = not all(choice in defs[config]['choices'] for choice in value)
                else:
                    # these should be only the simple data types (string, int, bool, float, etc) .. ignore dicts for now
                    invalid_choices = value not in defs[config]['choices']
    
                if invalid_choices:
                    raise AnsibleOptionsError('Invalid value "%s" for configuration option "%s", valid values are: %s' %
                                              (value, to_native(_get_entry(plugin_type, plugin_name, config)), defs[config]['choices']))
    
            # deal with deprecation of the setting
            if 'deprecated' in defs[config] and origin != 'default':
                self.DEPRECATED.append((config, defs[config].get('deprecated')))
        else:
>           raise AnsibleError('Requested entry (%s) was not defined in configuration.' % to_native(_get_entry(plugin_type, plugin_name, config)))
E           ansible.errors.AnsibleError: Requested entry (setting: log_level ) was not defined in configuration.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:558: AnsibleError

During handling of the above exception, another exception occurred:

    def test_update_config_data_with_empty_dict():
        config_manager = ConfigManager()
        with pytest.raises(AnsibleOptionsError):
>           config_manager.update_config_data(defs={'log_level': {}})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7f0995f7a950>
defs = {'log_level': {}}, configfile = None

    def update_config_data(self, defs=None, configfile=None):
        ''' really: update constants '''
    
        if defs is None:
            defs = self._base_defs
    
        if configfile is None:
            configfile = self._config_file
    
        if not isinstance(defs, dict):
            raise AnsibleOptionsError("Invalid configuration definition type: %s for %s" % (type(defs), defs))
    
        # update the constant for config file
        self.data.update_setting(Setting('CONFIG_FILE', configfile, '', 'string'))
    
        origin = None
        # env and config defs can have several entries, ordered in list from lowest to highest precedence
        for config in defs:
            if not isinstance(defs[config], dict):
                raise AnsibleOptionsError("Invalid configuration definition '%s': type is %s" % (to_native(config), type(defs[config])))
    
            # get value and origin
            try:
                value, origin = self.get_config_value_and_origin(config, configfile)
            except Exception as e:
                # Printing the problem here because, in the current code:
                # (1) we can't reach the error handler for AnsibleError before we
                #     hit a different error due to lack of working config.
                # (2) We don't have access to display yet because display depends on config
                #     being properly loaded.
                #
                # If we start getting double errors printed from this section of code, then the
                # above problem #1 has been fixed.  Revamp this to be more like the try: except
                # in get_config_value() at that time.
                sys.stderr.write("Unhandled error:\n %s\n\n" % traceback.format_exc())
>               raise AnsibleError("Invalid settings supplied for %s: %s\n" % (config, to_native(e)), orig_exc=e)
E               ansible.errors.AnsibleError: Invalid settings supplied for log_level: Requested entry (setting: log_level ) was not defined in configuration.
E               . Requested entry (setting: log_level ) was not defined in configuration.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py:604: AnsibleError
----------------------------- Captured stderr call -----------------------------
Unhandled error:
 Traceback (most recent call last):
  File "/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py", line 592, in update_config_data
    value, origin = self.get_config_value_and_origin(config, configfile)
  File "/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/config/manager.py", line 558, in get_config_value_and_origin
    raise AnsibleError('Requested entry (%s) was not defined in configuration.' % to_native(_get_entry(plugin_type, plugin_name, config)))
ansible.errors.AnsibleError: Requested entry (setting: log_level ) was not defined in configuration.


--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py::test_update_config_data_with_invalid_type
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py::test_update_config_data_with_none_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_update_config_data_0.py::test_update_config_data_with_empty_dict
============================== 3 failed in 0.42s ===============================
"""