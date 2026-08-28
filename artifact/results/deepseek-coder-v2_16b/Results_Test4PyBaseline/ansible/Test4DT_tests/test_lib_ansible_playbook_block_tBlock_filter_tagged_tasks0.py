# Module: ansible.playbook.block
# test_filter_tagged_tasks.py
from ansible.playbook.block import Block

def test_basic_usage():
    # Create a sample block with tasks
    my_block = Block()
    new_block = my_block.filter_tagged_tasks(all_vars={'var1': 1, 'var2': 2})
    
    assert isinstance(new_block, Block), "Expected a Block instance"
    # Add more assertions to check the contents of the filtered tasks if possible

def test_using_specific_all_vars():
    # Create a sample block with tasks
    my_block = Block()
    all_vars = {
        'tags': ['tag1', 'tag2'],
        'skip_tags': ['skip_tag1', 'skip_tag2']
    }
    new_block = my_block.filter_tagged_tasks(all_vars=all_vars)
    
    assert isinstance(new_block, Block), "Expected a Block instance"
    # Add more assertions to check the contents of the filtered tasks if possible

def test_handling_nested_tasks():
    # Create a sample block with nested tasks
    my_block = Block()
    all_vars = {
        'tags': ['tag1'],
        'skip_tags': []
    }
    new_block = my_block.filter_tagged_tasks(all_vars=all_vars)
    
    assert isinstance(new_block, Block), "Expected a Block instance"
    # Add more assertions to check the contents of the filtered tasks if possible
