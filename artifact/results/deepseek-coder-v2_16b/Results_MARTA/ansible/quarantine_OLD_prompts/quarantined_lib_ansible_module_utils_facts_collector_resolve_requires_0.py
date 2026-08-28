
import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_resolve_requires_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        unresolved_requires = ['a', 'b', 'c']
        all_fact_subsets = {frozenset({'a', 'b'}), frozenset({'c'})}
    
>       result = resolve_requires(unresolved_requires, all_fact_subsets)

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_resolve_requires_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

unresolved_requires = ['a', 'b', 'c']
all_fact_subsets = {frozenset({'a', 'b'}), frozenset({'c'})}

    def resolve_requires(unresolved_requires, all_fact_subsets):
        new_names = set()
        failed = []
        for unresolved in unresolved_requires:
            if unresolved in all_fact_subsets:
                new_names.add(unresolved)
            else:
                failed.append(unresolved)
    
        if failed:
>           raise UnresolvedFactDep('unresolved fact dep %s' % ','.join(failed))
E           ansible.module_utils.facts.collector.UnresolvedFactDep: unresolved fact dep a,b,c

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/module_utils/facts/collector.py:293: UnresolvedFactDep
________________________________ test_edge_case ________________________________

    def test_edge_case():
        unresolved_requires = []
        all_fact_subsets = {frozenset({'a', 'b'}), frozenset({'c'})}
    
>       with pytest.raises(UnresolvedFactDep):
E       Failed: DID NOT RAISE <class 'ansible.module_utils.facts.collector.UnresolvedFactDep'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_resolve_requires_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_resolve_requires_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_facts_collector_resolve_requires_0.py::test_edge_case
============================== 2 failed in 0.35s ===============================
"""