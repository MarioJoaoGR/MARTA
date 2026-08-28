
import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep

# Test Case 1: All requirements are found in the provided fact subsets
def test_resolve_requires_all_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req1', 'req2']
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == {''}  # An empty set means all resolved requirements are found

# Test Case 2: Some requirements are not found in the provided fact subsets
def test_resolve_requires_some_not_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req1', 'req3']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3'

# Test Case 3: No requirements provided
def test_resolve_requires_no_requirements():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = []
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == set()  # An empty set when no requirements are provided

# Test Case 4: All requirements not found in the provided fact subsets
def test_resolve_requires_all_not_found():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3', 'req4']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3,req4'
