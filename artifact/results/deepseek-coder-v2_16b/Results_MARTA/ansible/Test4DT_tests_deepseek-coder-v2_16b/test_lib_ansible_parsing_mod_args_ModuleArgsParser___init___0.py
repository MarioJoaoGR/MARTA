
import pytest
from ansible.parsing.mod_args import ModuleArgsParser


def test_invalid_task_ds():
    task_ds = "not a dictionary"
    collection_list = ['ansible.builtin']
    
    with pytest.raises(Exception) as e:
        ModuleArgsParser(task_ds=task_ds, collection_list=collection_list)
    
    assert str(e.value) == "the type of 'task_ds' should be a dict, but is a <class 'str'>"