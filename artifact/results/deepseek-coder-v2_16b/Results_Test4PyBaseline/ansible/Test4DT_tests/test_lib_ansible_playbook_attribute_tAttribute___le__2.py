
import pytest
from ansible.playbook.attribute import Attribute

# Test __le__ method where self.priority is less than or equal to other.priority
def test_lessthanorequal_self_less():
    attr1 = Attribute(isa='int', default=5, required=True)
    attr2 = Attribute(isa='int', default=10, required=True)
    assert attr1.__le__(attr2) == True  # This assertion is correct as per the function logic.

# Test __le__ method where self.priority is greater than other.priority
def test_lessthanorequal_self_greater():
    attr1 = Attribute(isa='int', default=15, required=True)
    attr2 = Attribute(isa='int', default=10, required=True)