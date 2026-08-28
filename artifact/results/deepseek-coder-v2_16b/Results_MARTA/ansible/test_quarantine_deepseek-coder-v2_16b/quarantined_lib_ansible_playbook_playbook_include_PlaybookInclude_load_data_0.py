
import pytest
from ansible.playbook import PlaybookInclude
from ansible.errors import AnsibleAssertionError, AnsibleParserError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        playbook_include = PlaybookInclude()
        ds = {'import_playbook': 'example.yml'}
        basedir = '/path/to/basedir'
    
>       new_playbook = playbook_include.load_data(ds, basedir)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/playbook_include.py:98: in load_data
    pb._load_playbook_data(file_name=playbook, variable_manager=variable_manager, vars=self.vars.copy())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.playbook.Playbook object at 0x7ffa269321d0>
file_name = '/path/to/basedir/example.yml', variable_manager = None, vars = {}

    def _load_playbook_data(self, file_name, variable_manager, vars=None):
    
        if os.path.isabs(file_name):
            self._basedir = os.path.dirname(file_name)
        else:
            self._basedir = os.path.normpath(os.path.join(self._basedir, os.path.dirname(file_name)))
    
        # set the loaders basedir
>       cur_basedir = self._loader.get_basedir()
E       AttributeError: 'NoneType' object has no attribute 'get_basedir'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/__init__.py:62: AttributeError
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        playbook_include = PlaybookInclude()
    
        with pytest.raises(TypeError):
>           playbook_include.load_data(None, None)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/playbook_include.py:64: in load_data
    new_obj = super(PlaybookInclude, self).load_data(ds, variable_manager, loader)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.playbook.playbook_include.PlaybookInclude object at 0x7ffa26932e30>
ds = None, variable_manager = None, loader = None

    def load_data(self, ds, variable_manager=None, loader=None):
        ''' walk the input datastructure and assign any values '''
    
        if ds is None:
>           raise AnsibleAssertionError('ds (%s) should not be None but it is.' % ds)
E           ansible.errors.AnsibleAssertionError: ds (None) should not be None but it is.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:251: AnsibleAssertionError
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        playbook_include = PlaybookInclude()
        ds = {'import_playbook': None}
        basedir = '/path/to/basedir'
    
        with pytest.raises(ValueError):
>           playbook_include.load_data(ds, basedir)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/playbook_include.py:64: in load_data
    new_obj = super(PlaybookInclude, self).load_data(ds, variable_manager, loader)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:269: in load_data
    ds = self.preprocess_data(ds)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/playbook_include.py:144: in preprocess_data
    self._preprocess_import(ds, new_ds, k, v)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.playbook.playbook_include.PlaybookInclude object at 0x7ffa26ddae90>
ds = {'import_playbook': None}, new_ds = {}, k = 'import_playbook', v = None

    def _preprocess_import(self, ds, new_ds, k, v):
        '''
        Splits the playbook import line up into filename and parameters
        '''
    
        if v is None:
>           raise AnsibleParserError("playbook import parameter is missing", obj=ds)
E           ansible.errors.AnsibleParserError: playbook import parameter is missing

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/playbook_include.py:163: AnsibleParserError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py::test_valid_inputs
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py::test_edge_cases
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_playbook_include_PlaybookInclude_load_data_0.py::test_invalid_inputs
============================== 3 failed in 0.46s ===============================
"""