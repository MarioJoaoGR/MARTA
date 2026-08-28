
import pytest
from apimd.parser import table


def test_empty_table():
    with pytest.raises(TypeError):
        table()



