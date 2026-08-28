# Module: sanic.blueprint_group
# Import the function using its provided module name.
from sanic.blueprints import BlueprintGroup
import pytest

# Test cases for the __init__ method of BlueprintGroup class
def test_blueprintgroup_init():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is None

# Test cases for the __delitem__ method of BlueprintGroup class
def test_blueprintgroup_delitem():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    assert len(bpg._blueprints) == 2
    
    # Remove a blueprint from the group by its index
    del bpg[0]
    assert len(bpg._blueprints) == 1

# Edge case: Test removing the last item in the list
def test_blueprintgroup_delitem_last():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bpg = BlueprintGroup(bp1, url_prefix="/api", version="v1")
    
    assert len(bpg._blueprints) == 1
    
    # Remove the last blueprint from the group by its index
    del bpg[0]
    assert len(bpg._blueprints) == 0

# Edge case: Test removing an invalid index should raise an error
def test_blueprintgroup_delitem_invalid():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bpg = BlueprintGroup(bp1, url_prefix="/api", version="v1")
    
    with pytest.raises(IndexError):
        del bpg[1]  # This should raise an IndexError as the index is out of range
