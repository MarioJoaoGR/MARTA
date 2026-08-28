
import pytest
from ansible.parsing.mod_args import ModuleArgsParser



def test_invalid_input_type():
    task_ds = "not a dictionary"
    with pytest.raises(Exception):
        parser = ModuleArgsParser(task_ds=task_ds)