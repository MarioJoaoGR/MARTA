
import pytest
from unittest.mock import patch, MagicMock
from ansible.playbook.collectionsearch import AnsibleCollectionConfig

def _ensure_default_collection(collection_list=None):
    default_collection = AnsibleCollectionConfig.default_collection

    # Will be None when used as the default
    if collection_list is None:
        collection_list = []

    # FIXME: exclude role tasks?
    if default_collection and default_collection not in collection_list:
        collection_list.insert(0, default_collection)

    # if there's something in the list, ensure that builtin or legacy is always there too
    if collection_list and 'ansible.builtin' not in collection_list and 'ansible.legacy' not in collection_list:
        collection_list.append('ansible.legacy')

    return collection_list

@pytest.fixture(autouse=True)
def mock_default_collection():
    with patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig.default_collection', 'ansible.builtin'):
        yield



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py F [ 33%]
EFEFE                                                                    [100%]

==================================== ERRORS ====================================
_______________ ERROR at teardown of test_valid_input_no_params ________________

    @pytest.fixture(autouse=True)
    def mock_default_collection():
>       with patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig.default_collection', 'ansible.builtin'):

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fd0b6b6c6a0>
exc_info = (None, None, None)

    def __exit__(self, *exc_info):
        """Undo the patch."""
        if self.is_local and self.temp_original is not DEFAULT:
            setattr(self.target, self.attribute, self.temp_original)
        else:
>           delattr(self.target, self.attribute)
E           AttributeError: can't delete attribute 'default_collection'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1577: AttributeError
_______________ ERROR at teardown of test_valid_input_empty_list _______________

    @pytest.fixture(autouse=True)
    def mock_default_collection():
>       with patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig.default_collection', 'ansible.builtin'):

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fd0b6b6f430>
exc_info = (None, None, None)

    def __exit__(self, *exc_info):
        """Undo the patch."""
        if self.is_local and self.temp_original is not DEFAULT:
            setattr(self.target, self.attribute, self.temp_original)
        else:
>           delattr(self.target, self.attribute)
E           AttributeError: can't delete attribute 'default_collection'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1577: AttributeError
_________________ ERROR at teardown of test_invalid_input_none _________________

    @pytest.fixture(autouse=True)
    def mock_default_collection():
>       with patch('ansible.playbook.collectionsearch.AnsibleCollectionConfig.default_collection', 'ansible.builtin'):

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fd0b676ba30>
exc_info = (None, None, None)

    def __exit__(self, *exc_info):
        """Undo the patch."""
        if self.is_local and self.temp_original is not DEFAULT:
            setattr(self.target, self.attribute, self.temp_original)
        else:
>           delattr(self.target, self.attribute)
E           AttributeError: can't delete attribute 'default_collection'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1577: AttributeError
=================================== FAILURES ===================================
__________________________ test_valid_input_no_params __________________________

    def test_valid_input_no_params():
        result = _ensure_default_collection()
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert ['ansible.builtin'] == ['ansible.bui...sible.legacy']
E         
E         Right contains one more item: 'ansible.legacy'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:30: AssertionError
_________________________ test_valid_input_empty_list __________________________

    def test_valid_input_empty_list():
        result = _ensure_default_collection([])
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert ['ansible.builtin'] == ['ansible.bui...sible.legacy']
E         
E         Right contains one more item: 'ansible.legacy'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:34: AssertionError
___________________________ test_invalid_input_none ____________________________

    def test_invalid_input_none():
        result = _ensure_default_collection(None)
>       assert result == ['ansible.builtin', 'ansible.legacy']
E       AssertionError: assert ['ansible.builtin'] == ['ansible.bui...sible.legacy']
E         
E         Right contains one more item: 'ansible.legacy'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py:38: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_no_params
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_empty_list
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_invalid_input_none
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_no_params
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_valid_input_empty_list
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_collectionsearch__ensure_default_collection_0.py::test_invalid_input_none
========================= 3 failed, 3 errors in 0.59s ==========================
"""