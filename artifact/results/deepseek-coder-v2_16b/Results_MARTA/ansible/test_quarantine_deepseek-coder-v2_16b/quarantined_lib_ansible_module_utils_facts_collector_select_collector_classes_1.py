
import pytest
from ansible.module_utils.facts.collector import ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassH, ClassI, ClassJ, ClassK, ClassL

def select_collector_classes(collector_names, all_fact_subsets):
    seen_collector_classes = set()
    selected_collector_classes = []

    for collector_name in collector_names:
        collector_classes = all_fact_subsets.get(collector_name, [])
        for collector_class in collector_classes:
            if collector_class not in seen_collector_classes:
                selected_collector_classes.append(collector_class)
                seen_collector_classes.add(collector_class)

    return selected_collector_classes

# Test Case 1: Selecting from two collectors with unique classes
def test_select_from_two_collectors():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [ClassA, ClassB],
        'collector2': [ClassC, ClassD]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {ClassA, ClassB, ClassC, ClassD}

# Test Case 2: Selecting from one collector
def test_select_from_one_collector():
    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [ClassE, ClassF],
        'collector2': [ClassG, ClassH]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert set(selected_classes) == {ClassE, ClassF}

# Test Case 3: Selecting from collectors with no classes
def test_select_from_empty_collectors():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [],
        'collector2': []
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []

# Test Case 4: Selecting from non-existent collector
def test_select_from_non_existent_collector():
    collector_names = ['non_existent_collector']
    all_fact_subsets = {
        'collector1': [ClassI, ClassJ],
        'collector2': [ClassK, ClassL]
    }
    selected_classes = select_collector_classes(collector_names, all_fact_subsets)
    assert selected_classes == []

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
_ ERROR collecting test_lib_ansible_module_utils_facts_collector_select_collector_classes_1.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_select_collector_classes_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_select_collector_classes_1.py:3: in <module>
    from ansible.module_utils.facts.collector import ClassA, ClassB, ClassC, ClassD, ClassE, ClassF, ClassG, ClassH, ClassI, ClassJ, ClassK, ClassL
E   ImportError: cannot import name 'ClassA' from 'ansible.module_utils.facts.collector' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/collector.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_select_collector_classes_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.67s ===============================
"""