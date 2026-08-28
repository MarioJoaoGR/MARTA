
import pytest
from your_module import _process_block, Block, Task

# Sample setup for each scenario
@pytest.fixture(params=[
    ({'action': 'run', 'name': 'Task One'}, {'action': 'build', 'name': 'Task Two', 'tags': ['important']}),
    None,
    'InvalidInput'
])
def input_data(request):
    return request.param

# Test scenario 1: test_valid_case
def test_valid_case():
    b = Block()
    task1 = Task(**{'action': 'run', 'name': 'Task One'})
    task2 = Task(**{'action': 'build', 'name': 'Task Two', 'tags': ['important']})
    b.block = [task1, task2]  # Assign the tasks to the block
    
    result = _process_block(b)
    expected_output = "Task One\tTAGS: []\nTask Two\tTAGS: [important]\n"
    assert result == expected_output

# Test scenario 2: test_edge_case
def test_edge_case():
    with pytest.raises(TypeError):
        _process_block(None)

# Test scenario 3: test_invalid_input
def test_invalid_input():
    with pytest.raises(TypeError):
        _process_block('InvalidInput')
