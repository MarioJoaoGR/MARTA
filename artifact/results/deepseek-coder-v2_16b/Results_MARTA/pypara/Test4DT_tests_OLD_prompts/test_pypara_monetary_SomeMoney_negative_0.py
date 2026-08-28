
import pytest
from unittest.mock import patch
from pypara.monetary import SomeMoney


def test_edge_case():
    money = None
    with pytest.raises(AttributeError):
        negated_money = money.negative()

@patch('pypara.monetary.SomeMoney', side_effect=TypeError)
def test_invalid_input(mock_some_money):
    with pytest.raises(TypeError):
        money = SomeMoney('USD', 'ten')