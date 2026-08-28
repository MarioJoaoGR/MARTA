
import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep

# Test Case 5: All requirements provided but none found in all_fact_subsets
def test_resolve_requires_none_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3', 'req4']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3,req4'

# Test Case 6: All requirements provided but some not found in all_fact_subsets
def test_resolve_requires_some_not_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req1', 'req3']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3'

# Test Case 7: No requirements provided (edge case)
def test_resolve_requires_no_requirements():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = []
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == set()  # An empty set when no requirements are provided

# Test Case 8: All requirements not found in the provided fact subsets (edge case)
def test_resolve_requires_all_not_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3', 'req4']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3,req4'
