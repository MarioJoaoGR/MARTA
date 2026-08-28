
import pytest
from sanic import Sanic, Blueprint, text
from sanic.blueprints import BlueprintGroup

# Fixture to create a Sanic app for testing
@pytest.fixture
def app():
    return Sanic("MyApp")

# Test case for valid initialization of BlueprintGroup with multiple blueprints

# Test case for checking if BlueprintGroup has the _blueprints attribute after initialization

# Test case to ensure that the sanitized blueprint's url_prefix is correctly set
def test_sanitize_blueprint_with_existing_values():
    bp = Blueprint('bp', url_prefix='/bp', version='existing_version')
    bpg = BlueprintGroup(url_prefix='/api', version='v1')
    sanitized_bp = bpg._sanitize_blueprint(bp)
    
    assert sanitized_bp.url_prefix == '/api/bp'

# Test case to check if the insert method adds a new blueprint at the specified index
def test_insert_method():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(url_prefix='/api', version='v1')
    
    bpg.insert(0, bp1)
    assert len(bpg._blueprints) == 1
    assert bpg._blueprints[0] == bp1
    
    bpg.insert(1, bp2)
    assert len(bpg._blueprints) == 2
    assert bpg._blueprints[1] == bp2