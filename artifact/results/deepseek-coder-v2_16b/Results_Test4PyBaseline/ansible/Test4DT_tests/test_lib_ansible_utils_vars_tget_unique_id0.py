
import pytest
from ansible.utils.vars import get_unique_id

# Assuming node_mac and random_int are predefined global variables with appropriate values
node_mac = "00-11-22-33-44-55"
random_int = "66778899"
cur_id = 0

def test_get_unique_id():
    # Initial call to get the first unique ID
    uid = get_unique_id()
    assert isinstance(uid, str), "Expected a string return type"