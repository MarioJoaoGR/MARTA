
# Module: ansible.playbook.block
# test_block.py
from ansible.playbook.block import Block
import pytest
import uuid

def generate_unique_uuid():
    return str(uuid.uuid4())

@pytest.fixture
def create_block():
    return Block()

def test_block_equality_same_uuid(create_block):
    # Create a second block with the same UUID as the first one
    other_block = Block()
    create_block._uuid = other_block._uuid  # Manually set to match for this test
    assert create_block == other_block, "Blocks with the same UUID should be equal"

def test_block_equality_different_uuids(create_block):
    # Create a second block with a different UUID
    other_block = Block()
    assert not (create_block == other_block), "Blocks with different UUIDs should not be equal"

def test_block_equality_with_uuid_set_manually(create_block):
    # Manually set the UUID of one block and compare it to another without setting its UUID
    create_block._uuid = generate_unique_uuid()  # Set a unique UUID for this block
    other_block = Block()
    assert not (create_block == other_block), "Blocks with manually set but different UUIDs should not be equal"

def test_block_equality_with_same_attributes(create_block):
    # Create another block with the same attributes except for _uuid
    other_block = Block()
    create_block._uuid = generate_unique_uuid()  # Set a unique UUID for this block
    assert not (create_block == other_block), "Blocks with different attributes, including _uuid, should not be equal"
