
import pytest
from ansible.errors import AnsibleOptionsError, AnsibleLookupError
from ansible.plugins.lookup.config import LookupModule

class TestLookupModule:
    
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.lookup_module = LookupModule()
    
    def test_valid_input_with_plugin(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        results = self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert isinstance(results, list), "Expected a list of results"
    
    def test_valid_input_without_plugin(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
        
        results = self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert isinstance(results, list), "Expected a list of results"
    
    def test_invalid_input_missing_plugin_type(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=None, plugin_name=plugin_name, on_missing=on_missing)
        assert "Both plugin_type and plugin_name are required" in str(excinfo.value), "Expected an error about missing plugin type"
    
    def test_invalid_input_missing_plugin_name(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=None, on_missing=on_missing)
        assert "Both plugin_type and plugin_name are required" in str(excinfo.value), "Expected an error about missing plugin name"
    
    def test_invalid_input_non_string_terms(self):
        terms = ['setting1', 123]
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Invalid setting identifier" in str(excinfo.value), "Expected an error about non-string terms"
    
    def test_invalid_input_none_terms(self):
        terms = None
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Invalid setting identifier" in str(excinfo.value), "Expected an error about none terms"
    
    def test_invalid_input_none_variables(self):
        terms = ['setting1', 'setting2']
        variables = None
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Invalid setting identifier" in str(excinfo.value), "Expected an error about none variables"
    
    def test_invalid_input_none_kwargs(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Both plugin_type and plugin_name are required" in str(excinfo.value), "Expected an error about none kwargs"
    
    def test_invalid_input_empty_terms(self):
        terms = []
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Invalid setting identifier" in str(excinfo.value), "Expected an error about empty terms"
    
    def test_invalid_input_empty_variables(self):
        terms = ['setting1', 'setting2']
        variables = {}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Invalid setting identifier" in str(excinfo.value), "Expected an error about empty variables"
    
    def test_invalid_input_empty_kwargs(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert "Both plugin_type and plugin_name are required" in str(excinfo.value), "Expected an error about empty kwargs"
    
    def test_invalid_input_non_string_on_missing(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 123
        
        with pytest.raises(AnsibleOptionsError) as excinfo:
            self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)
        assert '"on_missing" must be a string and one of "error", "warn" or "skip"' in str(excinfo.value), "Expected an error about non-string on_missing"
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 12 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py F [  8%]
FFFFFFFFFFF                                                              [100%]

=================================== FAILURES ===================================
________________ TestLookupModule.test_valid_input_with_plugin _________________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f1134c01f60>

    def test_valid_input_with_plugin(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
>       results = self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f1133721210>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_______________ TestLookupModule.test_valid_input_without_plugin _______________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f1134be9a50>

    def test_valid_input_without_plugin(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
    
>       results = self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f1133721960>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': None, 'plugin_type': None}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
___________ TestLookupModule.test_invalid_input_missing_plugin_type ____________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f1134beb310>

    def test_invalid_input_missing_plugin_type(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=None, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f113599f940>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': None}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
___________ TestLookupModule.test_invalid_input_missing_plugin_name ____________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f113518b8b0>

    def test_invalid_input_missing_plugin_name(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=None, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:49: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333f1150>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': None, 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_____________ TestLookupModule.test_invalid_input_non_string_terms _____________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f1135259930>

    def test_invalid_input_non_string_terms(self):
        terms = ['setting1', 123]
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:60: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333d0790>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
________________ TestLookupModule.test_invalid_input_none_terms ________________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f1135621870>

    def test_invalid_input_none_terms(self):
        terms = None
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:71: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f1134c032e0>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
______________ TestLookupModule.test_invalid_input_none_variables ______________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f11355b1600>

    def test_invalid_input_none_variables(self):
        terms = ['setting1', 'setting2']
        variables = None
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:82: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333dc700>
task_keys = None, var_options = None
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_______________ TestLookupModule.test_invalid_input_none_kwargs ________________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f113594e770>

    def test_invalid_input_none_kwargs(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:93: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333f0850>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': None, 'plugin_type': None}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_______________ TestLookupModule.test_invalid_input_empty_terms ________________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f11358d38e0>

    def test_invalid_input_empty_terms(self):
        terms = []
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:104: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f1135620ca0>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_____________ TestLookupModule.test_invalid_input_empty_variables ______________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f11358d2050>

    def test_invalid_input_empty_variables(self):
        terms = ['setting1', 'setting2']
        variables = {}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:115: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333f3070>
task_keys = None, var_options = {}
direct = {'on_missing': 'error', 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
_______________ TestLookupModule.test_invalid_input_empty_kwargs _______________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f11337207f0>

    def test_invalid_input_empty_kwargs(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = None
        plugin_name = None
        on_missing = 'error'
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:126: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11334195a0>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 'error', 'plugin_name': None, 'plugin_type': None}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
__________ TestLookupModule.test_invalid_input_non_string_on_missing ___________

self = <test_lib_ansible_plugins_lookup_config_LookupModule_run_0.TestLookupModule object at 0x7f11337207c0>

    def test_invalid_input_non_string_on_missing(self):
        terms = ['setting1', 'setting2']
        variables = {'var1': 'val1'}
        plugin_type = 'lookup'
        plugin_name = 'my_plugin'
        on_missing = 123
    
        with pytest.raises(AnsibleOptionsError) as excinfo:
>           self.lookup_module.run(terms, variables=variables, plugin_type=plugin_type, plugin_name=plugin_name, on_missing=on_missing)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py:137: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/lookup/config.py:122: in run
    self.set_options(var_options=variables, direct=kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.plugins.lookup.config.LookupModule object at 0x7f11333d03d0>
task_keys = None, var_options = {'var1': 'val1'}
direct = {'on_missing': 123, 'plugin_name': 'my_plugin', 'plugin_type': 'lookup'}

    def set_options(self, task_keys=None, var_options=None, direct=None):
        '''
        Sets the _options attribute with the configuration/keyword information for this plugin
    
        :arg task_keys: Dict with playbook keywords that affect this option
        :arg var_options: Dict with either 'connection variables'
        :arg direct: Dict with 'direct assignment'
        '''
>       self._options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)
E       AttributeError: 'LookupModule' object has no attribute '_load_name'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/plugins/__init__.py:82: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_valid_input_with_plugin
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_valid_input_without_plugin
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_missing_plugin_type
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_missing_plugin_name
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_non_string_terms
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_none_terms
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_none_variables
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_none_kwargs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_empty_terms
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_empty_variables
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_empty_kwargs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_lookup_config_LookupModule_run_0.py::TestLookupModule::test_invalid_input_non_string_on_missing
============================== 12 failed in 0.64s ==============================
"""