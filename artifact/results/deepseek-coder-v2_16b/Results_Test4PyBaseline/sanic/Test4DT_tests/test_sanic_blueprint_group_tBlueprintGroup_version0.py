# Module: sanic.blueprint_group
# Import the function using its provided module name.
from sanic.blueprints import BlueprintGroup
import pytest

# Test cases for BlueprintGroup class
def test_init():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is None

def test_init_without_args():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is None

def test_init_with_only_blueprints():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is None

def test_version():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, version="v1")
    assert bpg.version() == "v1"

def test_version_none():
    bp1 = Blueprint('bp1', url_prefix='/bp1', version="v2")
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    assert bpg.version() == "v2"

def test_strict_slashes():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, strict_slashes=True)
    assert bpg._strict_slashes is True

def test_strict_slashes_none():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2)
    assert bpg._strict_slashes is None
