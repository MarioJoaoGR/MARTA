
import pytest
from ansible.module_utils.facts.collector import resolve_requires, UnresolvedFactDep

# Test Case 5: Empty unresolved requirements list should return an empty set
def test_resolve_requires_empty_unresolved():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = []
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == set()

# Test Case 6: Unresolved requirement not in fact subsets should raise exception
def test_resolve_requires_unresolved_not_in_subsets():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3'

# Test Case 7: Resolved requirement should be added to new_names set
def test_resolve_requires_resolved():
    all_fact_subsets = {'req1': {'req1'}, 'req2': set()}
    unresolved_requires = ['req1']
    result = resolve_requires(unresolved_requires, all_fact_subsets)
    assert result == {'req1'}

# Test Case 8: Unresolved requirement should be added to failed list
def test_resolve_requires_unresolved():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3'

# Test Case 9: Multiple unresolved requirements should be added to failed list and raise exception
def test_resolve_requires_multiple_unresolved():
    all_fact_subsets = {'req1': set(), 'req2': set()}
    unresolved_requires = ['req3', 'req4']
    with pytest.raises(UnresolvedFactDep) as excinfo:
        resolve_requires(unresolved_requires, all_fact_subsets)
    assert str(excinfo.value) == 'unresolved fact dep req3,req4'
