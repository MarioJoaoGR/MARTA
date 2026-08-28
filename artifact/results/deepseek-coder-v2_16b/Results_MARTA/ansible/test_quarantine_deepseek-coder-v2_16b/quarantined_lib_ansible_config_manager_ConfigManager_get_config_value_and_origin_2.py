
import pytest
from ansible.config.manager import ConfigManager

@pytest.fixture(scope="module")
def config_manager():
    return ConfigManager()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

config_manager = <ansible.config.manager.ConfigManager object at 0x7fa8cac2b0a0>

    def test_valid_case(config_manager):
>       value, origin = config_manager.get_config_value_and_origin('log_level')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7fa8cac2b0a0>
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
_____________________________ test_direct_setting ______________________________

    def test_direct_setting():
        config_manager = ConfigManager()
>       value, origin = config_manager.get_config_value_and_origin('log_level', direct={'log_level': 'DEBUG'})

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.config.manager.ConfigManager object at 0x7fa8ca8942e0>
config = 'log_level', cfile = None, plugin_type = None, plugin_name = None
keys = None, variables = None, direct = {'log_level': 'DEBUG'}

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
_____________________________ test_missing_setting _____________________________

    def test_missing_setting():
        config_manager = ConfigManager()
>       with pytest.raises(AnsibleError):
E       NameError: name 'AnsibleError' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py:20: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py::test_direct_setting
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_config_manager_ConfigManager_get_config_value_and_origin_2.py::test_missing_setting
============================== 3 failed in 0.79s ===============================
"""