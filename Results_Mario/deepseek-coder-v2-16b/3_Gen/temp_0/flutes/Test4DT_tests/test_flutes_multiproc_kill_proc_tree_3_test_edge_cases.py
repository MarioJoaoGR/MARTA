
import pytest
import os
from flutes.multiproc import kill_proc_tree

@pytest.mark.skip(reason="This test is disabled because it requires mocking psutil which is not allowed in this scenario.")
def test_kill_proc_tree():
    pid = os.getpid()
    with pytest.raises(AttributeError):  # We expect an AttributeError due to the FakeProcess object used in testing
        kill_proc_tree(pid)

@pytest.mark.skip(reason="This test is disabled because it requires mocking psutil which is not allowed in this scenario.")
def test_kill_proc_tree_including_parent():
    pid = os.getpid()
    with pytest.raises(AttributeError):  # We expect an AttributeError due to the FakeProcess object used in testing
        kill_proc_tree(pid, including_parent=True)
