
import pytest
from ansible.plugins.filter.core import combine, merge_hash
from unittest.mock import patch


def test_combine_recursive_true():
    with patch('ansible.plugins.filter.core.merge_hash', return_value={'a': [1, 2, 3]}):
        result = combine({'a': [1, 2]}, {'a': [3]}, recursive=True)
        assert result == {'a': [1, 2, 3]}
