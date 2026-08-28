
import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import build_dep_data


def test_empty_all_fact_subsets():
    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {}
    
    with pytest.raises(KeyError):
        build_dep_data(collector_names, all_fact_subsets)