
import pytest
from ansible.module_utils.facts.collector import Collector
from collections import defaultdict

def build_dep_data(collector_names, all_fact_subsets):
    dep_map = defaultdict(set)
    for collector_name in collector_names:
        collector_deps = set()
        for collector in all_fact_subsets[collector_name]:
            for dep in collector.required_facts:
                collector_deps.add(dep)
        dep_map[collector_name] = collector_deps
    return dep_map

# Test cases for build_dep_data function
def test_build_dep_data_basic():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [Collector({'fact1'}), Collector({'fact2'})],
        'collector2': [Collector({'fact3'}), Collector({'fact4'})]
    }
    expected_output = {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3', 'fact4'}
    }
    assert build_dep_data(collector_names, all_fact_subsets) == expected_output

def test_build_dep_data_empty():
    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [],
        'collector2': []
    }
    expected_output = {'collector1': set()}
    assert build_dep_data(collector_names, all_fact_subsets) == expected_output

def test_build_dep_data_multiple_collectors():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [Collector({'fact1'}), Collector({'fact2'})],
        'collector2': [Collector({'fact3'}), Collector({'fact4'})]
    }
    expected_output = {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3', 'fact4'}
    }
    assert build_dep_data(collector_names, all_fact_subsets) == expected_output

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
_ ERROR collecting test_lib_ansible_module_utils_facts_collector_build_dep_data_0.py _
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_dep_data_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_dep_data_0.py:3: in <module>
    from ansible.module_utils.facts.collector import Collector
E   ImportError: cannot import name 'Collector' from 'ansible.module_utils.facts.collector' (/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/collector.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_build_dep_data_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.41s ===============================
"""