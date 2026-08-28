
# Module: ansible.playbook.included_file
from ansible.playbook.included_file import IncludedFile
import pytest

# Test case to check if an instance of IncludedFile is created correctly with default is_role value
def test_init_with_default_is_role():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    assert included_file._filename == "config.yml"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "deploy"