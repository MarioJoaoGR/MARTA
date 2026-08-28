
import pytest
from ansible.playbook.play import Play

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_load_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        data = {
            'hosts': ['localhost'],
            'roles': ['role1', 'role2']
        }
>       play = Play.load(data)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_load_0.py:10: 
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

self = <ansible.playbook.role.include.RoleInclude object at 0x7f92ded32cb0>
role_name = 'role1'

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
E       ansible.errors.AnsibleError: the role 'role1' was not found in ./roles:/home/joaovitorino/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles:.

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/role/definition.py:203: AnsibleError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_play_Play_load_0.py::test_valid_input
============================== 1 failed in 0.53s ===============================
"""