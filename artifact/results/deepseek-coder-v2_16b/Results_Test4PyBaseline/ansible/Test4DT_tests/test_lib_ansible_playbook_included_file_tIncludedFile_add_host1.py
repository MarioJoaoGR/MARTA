
# Module: ansible.playbook.included_file
from ansible.playbook.included_file import IncludedFile
import pytest

# Test Case 5: Adding a Host to an Already Existing Group (Should Raise ValueError)
def test_add_host_existing_group():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    included_file._hosts.append("localhost")  # Simulate an already existing host
    with pytest.raises(ValueError):
        included_file.add_host("localhost")

# Test Case 6: Adding a Host to the Included File When It Is Already in the List (Should Not Raise ValueError)
def test_add_host_already_in_list():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    included_file._hosts.append("localhost")  # Adding a host to simulate it being in the list
    with pytest.raises(ValueError):
        included_file.add_host("localhost")

# Test Case 7: Adding Multiple Hosts and Verifying They Are All Unique
def test_add_multiple_hosts():
    included_file = IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")
    included_file.add_host("localhost")
    included_file.add_host("127.0.0.1")
    assert len(included_file._hosts) == 2
    assert "localhost" in included_file._hosts