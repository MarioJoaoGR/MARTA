
import pytest
from ansible.plugins.filter.core import FilterModule
from unittest.mock import patch

def test_valid_groupby_filter():
    fm = FilterModule()
    data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 30}
    ]
    with patch('ansible.plugins.filter.core.do_groupby') as mock_groupby:
        mock_groupby.return_value = [{'key': 30, 'values': [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 30}]}]
        result = fm.filters()['groupby'](data, 'age')
        assert mock_groupby.called
        assert result == [{'key': 30, 'values': [{'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 30}]}]

def test_edge_case_empty_list():
    fm = FilterModule()
    data = []
    with pytest.raises(ValueError):
        with patch('ansible.plugins.filter.core.do_groupby') as mock_groupby:
            mock_groupby.side_effect = ValueError("Cannot group by attribute in an empty list")
            fm.filters()['groupby'](data, 'age')
