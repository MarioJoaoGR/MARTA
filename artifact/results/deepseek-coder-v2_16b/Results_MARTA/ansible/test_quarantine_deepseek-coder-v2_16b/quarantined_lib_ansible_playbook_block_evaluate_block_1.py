
import pytest
from ansible.playbook.block import evaluate_block

def test_evaluate_block_basic():
    block = {
        "block": [{"task1": {"action": "run", "status": "pending"}}],
        "rescue": [{"task2": {"action": "stop", "status": "failed"}}],
        "always": [{"task3": {"action": "cleanup", "status": "completed"}}]
    }
    
    evaluated_block = evaluate_block(block)
    assert "_parent" not in evaluated_block, f"_parent should be excluded but is present: {evaluated_block}"
    assert "tasks" in evaluated_block, "Expected 'tasks' to be included in the evaluated block."
    assert len(evaluated_block["tasks"]) == 3, f"Expected 3 tasks in 'tasks', found {len(evaluated_block['tasks'])}: {evaluated_block['tasks']}"

def test_evaluate_block_empty():
    empty_block = {}
    
    evaluated_block = evaluate_block(empty_block)
    assert "_parent" not in evaluated_block, f"_parent should be excluded but is present: {evaluated_block}"
    assert "tasks" not in evaluated_block, "'tasks' should not be included when the block is empty."

def test_evaluate_block_no_rescue_or_always():
    minimal_block = {"block": [{"task1": {"action": "run", "status": "pending"}}]}
    
    evaluated_block = evaluate_block(minimal_block)
    assert "_parent" not in evaluated_block, f"_parent should be excluded but is present: {evaluated_block}"
    assert "tasks" in evaluated_block, "Expected 'tasks' to be included when rescue and always are absent."
    assert len(evaluated_block["tasks"]) == 1, f"Expected 1 task in 'tasks', found {len(evaluated_block['tasks'])}: {evaluated_block['tasks']}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_____ ERROR collecting test_lib_ansible_playbook_block_evaluate_block_1.py _____
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_block_evaluate_block_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_block_evaluate_block_1.py:3: in <module>
    from ansible.playbook.block import evaluate_block
E   ImportError: cannot import name 'evaluate_block' from 'ansible.playbook.block' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/playbook/block.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_playbook_block_evaluate_block_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.93s ===============================
"""