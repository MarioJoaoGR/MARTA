
import pytest
from flutils.namedtupleutils import _to_namedtuple
from unittest.mock import patch


def test_edge_cases():
    with pytest.raises(TypeError):
        _to_namedtuple("not supported", _started=False)
