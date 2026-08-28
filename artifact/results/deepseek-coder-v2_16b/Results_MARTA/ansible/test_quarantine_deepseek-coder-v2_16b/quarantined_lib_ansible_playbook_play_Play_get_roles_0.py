
import pytest
from ansible.playbook.play import Play
from ansible.errors import AnsibleError, AnsibleAssertionError, AnsibleParserError



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        data = {
            'hosts': ['localhost'],
            'gather_facts': True,
            'roles': ['webserver', 'database']
        }
>       play = Play.load(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:138: in load
    return p.load_data(data, variable_manager=variable_manager, loader=loader)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:282: in load_data
    self._attributes[target_name] = method(name, ds[name])
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:217: in _load_roles
    role_includes = load_list_of_roles(ds, play=self, variable_manager=self._variable_manager,
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/helpers.py:342: in load_list_of_roles
    i = RoleInclude.load(role_def, play=play, current_role_path=current_role_path, variable_manager=variable_manager,
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/role/include.py:60: in load
    return ri.load_data(data, variable_manager=variable_manager, loader=loader)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:269: in load_data
    ds = self.preprocess_data(ds)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/role/definition.py:95: in preprocess_data
    (role_name, role_path) = self._load_role_path(role_name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <ansible.playbook.role.include.RoleInclude object at 0x7fde0b3e2800>
role_name = 'webserver'

    def _load_role_path(self, role_name):
        '''
        the 'role', as specified in the ds (or as a bare string), can either
        be a simple name or a full path. If it is a full path, we use the
        basename as the role name, otherwise we take the name as-given and
        append it to the default role path
        '''
    
        # create a templar class to template the dependency names, in
        # case they contain variables
        if self._variable_manager is not None:
            all_vars = self._variable_manager.get_vars(play=self._play)
        else:
            all_vars = dict()
    
        templar = Templar(loader=self._loader, variables=all_vars)
        role_name = templar.template(role_name)
    
        role_tuple = None
    
        # try to load as a collection-based role first
        if self._collection_list or AnsibleCollectionRef.is_valid_fqcr(role_name):
            role_tuple = _get_collection_role_path(role_name, self._collection_list)
    
        if role_tuple:
            # we found it, stash collection data and return the name/path tuple
            self._role_collection = role_tuple[2]
            return role_tuple[0:2]
    
        # We didn't find a collection role, look in defined role paths
        # FUTURE: refactor this to be callable from internal so we can properly order
        # ansible.legacy searches with the collections keyword
    
        # we always start the search for roles in the base directory of the playbook
        role_search_paths = [
            os.path.join(self._loader.get_basedir(), u'roles'),
        ]
    
        # also search in the configured roles path
        if C.DEFAULT_ROLES_PATH:
            role_search_paths.extend(C.DEFAULT_ROLES_PATH)
    
        # next, append the roles basedir, if it was set, so we can
        # search relative to that directory for dependent roles
        if self._role_basedir:
            role_search_paths.append(self._role_basedir)
    
        # finally as a last resort we look in the current basedir as set
        # in the loader (which should be the playbook dir itself) but without
        # the roles/ dir appended
        role_search_paths.append(self._loader.get_basedir())
    
        # now iterate through the possible paths and return the first one we find
        for path in role_search_paths:
            path = templar.template(path)
            role_path = unfrackpath(os.path.join(path, role_name))
            if self._loader.path_exists(role_path):
                return (role_name, role_path)
    
        # if not found elsewhere try to extract path from name
        role_path = unfrackpath(role_name)
        if self._loader.path_exists(role_path):
            role_name = os.path.basename(role_name)
            return (role_name, role_path)
    
        searches = (self._collection_list or []) + role_search_paths
>       raise AnsibleError("the role '%s' was not found in %s" % (role_name, ":".join(searches)), obj=self._ds)
E       ansible.errors.AnsibleError: the role 'webserver' was not found in ./roles:/home/joaovitorino/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/role/definition.py:203: AnsibleError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        data = None
        with pytest.raises(TypeError):
>           Play.load(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py:19: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:138: in load
    return p.load_data(data, variable_manager=variable_manager, loader=loader)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = , ds = None, variable_manager = None, loader = None

    def load_data(self, ds, variable_manager=None, loader=None):
        ''' walk the input datastructure and assign any values '''
    
        if ds is None:
>           raise AnsibleAssertionError('ds (%s) should not be None but it is.' % ds)
E           ansible.errors.AnsibleAssertionError: ds (None) should not be None but it is.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:251: AnsibleAssertionError
______________________________ test_invalid_input ______________________________

self = , attr = 'roles', ds = 'webserver'

    def _load_roles(self, attr, ds):
        '''
        Loads and returns a list of RoleInclude objects from the datastructure
        list of role definitions and creates the Role from those objects
        '''
    
        if ds is None:
            ds = []
    
        try:
>           role_includes = load_list_of_roles(ds, play=self, variable_manager=self._variable_manager,
                                               loader=self._loader, collection_search_list=self.collections)

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:217: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

ds = 'webserver', play = , current_role_path = None, variable_manager = None
loader = <ansible.parsing.dataloader.DataLoader object at 0x7fde0b72dff0>
collection_search_list = []

    def load_list_of_roles(ds, play, current_role_path=None, variable_manager=None, loader=None, collection_search_list=None):
        """
        Loads and returns a list of RoleInclude objects from the ds list of role definitions
        :param ds: list of roles to load
        :param play: calling Play object
        :param current_role_path: path of the owning role, if any
        :param variable_manager: varmgr to use for templating
        :param loader: loader to use for DS parsing/services
        :param collection_search_list: list of collections to search for unqualified role names
        :return:
        """
        # we import here to prevent a circular dependency with imports
        from ansible.playbook.role.include import RoleInclude
    
        if not isinstance(ds, list):
>           raise AnsibleAssertionError('ds (%s) should be a list but was a %s' % (ds, type(ds)))
E           ansible.errors.AnsibleAssertionError: ds (webserver) should be a list but was a <class 'str'>

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/helpers.py:338: AnsibleAssertionError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        data = {
            'hosts': ['localhost'],
            'gather_facts': True,
            'roles': 'webserver'  # Invalid type for roles
        }
        with pytest.raises(TypeError):
>           Play.load(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:138: in load
    return p.load_data(data, variable_manager=variable_manager, loader=loader)
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/base.py:282: in load_data
    self._attributes[target_name] = method(name, ds[name])
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = , attr = 'roles', ds = 'webserver'

    def _load_roles(self, attr, ds):
        '''
        Loads and returns a list of RoleInclude objects from the datastructure
        list of role definitions and creates the Role from those objects
        '''
    
        if ds is None:
            ds = []
    
        try:
            role_includes = load_list_of_roles(ds, play=self, variable_manager=self._variable_manager,
                                               loader=self._loader, collection_search_list=self.collections)
        except AssertionError as e:
>           raise AnsibleParserError("A malformed role declaration was encountered.", obj=self._ds, orig_exc=e)
E           ansible.errors.AnsibleParserError: A malformed role declaration was encountered.. ds (webserver) should be a list but was a <class 'str'>

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/play.py:220: AnsibleParserError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_get_roles_0.py::test_invalid_input
============================== 3 failed in 0.55s ===============================
"""