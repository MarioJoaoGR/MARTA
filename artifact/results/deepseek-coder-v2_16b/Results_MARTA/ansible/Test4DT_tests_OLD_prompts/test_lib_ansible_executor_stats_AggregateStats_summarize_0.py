
import pytest
from unittest.mock import patch
from ansible.executor.stats import AggregateStats


def test_edge_case():
    with patch('ansible.executor.stats.AggregateStats.__init__', return_value=None):
        stats = AggregateStats()
        host = None
        with pytest.raises(AttributeError):
            summary = stats.summarize(host)
