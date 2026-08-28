# Module: ansible.playbook.included_file
# Import the function from its module
from ansible.playbook.included_file import IncludedFile
import pytest

# Test Case 1: Basic Usage for a Task Configuration
def test_basic_usage():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    assert included_file._filename == "config.yml"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "deploy"
    assert not included_file._is_role
    assert included_file._hosts == []

# Test Case 2: Including Files Related to Roles
def test_role_association():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy", is_role=True)
    assert included_file._filename == "config.yml"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "deploy"
    assert included_file._is_role
    assert included_file._hosts == []

# Test Case 3: Adding a Host to the Included File
def test_add_host():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    included_file.add_host("localhost")
    assert included_file._hosts == ["localhost"]

# Test Case 4: Adding an Existing Host to the Included File (Should Raise ValueError)
def test_add_existing_host():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    included_file.add_host("localhost")
    with pytest.raises(ValueError):
        included_file.add_host("localhost")
