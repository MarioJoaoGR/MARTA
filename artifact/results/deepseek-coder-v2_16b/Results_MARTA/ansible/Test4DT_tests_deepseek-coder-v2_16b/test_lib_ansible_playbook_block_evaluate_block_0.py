
import pytest
from ansible.playbook.block import evaluate_block

# Test valid input scenario
def test_valid_input():
    block = {
        "block": [{"task1": {"action": "run", "status": "pending"}}],
        "rescue": [{"task2": {"action": "stop", "status": "failed"}}],
        "always": [{"task3": {"action": "cleanup", "status": "completed"}}]
    }
    
    evaluated_block = evaluate_block(block)
    assert "_parent" not in evaluated_block
    assert "tasks" in evaluated_block
    assert len(evaluated_block["tasks"]) == 3
    assert all(task.get("status") for task in evaluated_block["tasks"])

# Test edge case scenario with None and empty lists
def test_edge_case():
    block = {
        "block": [],
        "rescue": [],
        "always": []
    }
    
    evaluated_block = evaluate_block(block)
    assert "_parent" not in evaluated_block
    assert "tasks" in evaluated_block
    assert len(evaluated_block["tasks"]) == 0

# Test invalid input scenario with missing keys
def test_invalid_input():
    block = {
        "block": [{"task1": {"action": "run"}}],
        "rescue": [],
        "always": []
    }
    
    evaluated_block = evaluate_block(block)
    assert "_parent" not in evaluated_block
    assert "tasks" in evaluated_block
    assert len(evaluated_block["tasks"]) == 1
    assert all(task.get("status") for task in evaluated_block["tasks"])
