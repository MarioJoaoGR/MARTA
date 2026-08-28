
import pytest
from sanic import Sanic, Blueprint
from sanic.response import text
from unittest.mock import patch

# Test for invalid inputs in BlueprintGroup initialization
def test_invalid_inputs():
    with pytest.raises(Exception):
        # Passing non-Blueprint objects should raise an Exception
        BlueprintGroup("not_a_blueprint", "another_non_blueprint")
