
import pytest
from ansible.playbook.included_file import IncludedFile

# Example call 1: Creating an instance for a specific task without role association
@pytest.fixture
def included_file():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")

# Example call 2: Creating an instance for a specific task with role association
@pytest.fixture
def included_file_with_role():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy", is_role=True)

# Test case for initialization without role association
def test_included_file_initialization_without_role(included_file):
    assert included_file._filename == "config.yml"
    assert included_file._args == {"arg1": "value1"}
    assert included_file._vars == {"var1": "value1"}
    assert included_file._task == "deploy"
    assert not included_file._is_role

# Test case for initialization with role association
def test_included_file_initialization_with_role(included_file_with_role):
    assert included_file_with_role._filename == "config.yml"
    assert included_file_with_role._args == {"arg1": "value1"}
    assert included_file_with_role._vars == {"var1": "value1"}
    assert included_file_with_role._task == "deploy"
    assert included_file_with_role._is_role

# Test case for adding a host to the included file instance
def test_add_host(included_file):
    included_file.add_host("localhost")
    assert len(included_file._hosts) == 1
    assert "localhost" in included_file._hosts

# Test case for equality check between two IncludedFile instances
@pytest.fixture
def other_included_file():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")

def test_equality(included_file, other_included_file):
    assert included_file == other_included_file
