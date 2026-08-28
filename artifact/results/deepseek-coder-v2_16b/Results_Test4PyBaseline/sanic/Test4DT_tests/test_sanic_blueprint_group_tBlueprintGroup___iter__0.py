# Module: sanic.blueprint_group
import pytest
from sanic import Blueprint, Sanic
from sanic.response import text
from sanic.blueprints import BlueprintGroup

# Fixture to create a simple Sanic app for testing
@pytest.fixture
def app():
    app = Sanic("MyApp")
    return app

# Test case for initializing a BlueprintGroup with default parameters
def test_blueprint_group_default_parameters():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)
    
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg._blueprints) == 2
    assert all(isinstance(bp, Blueprint) for bp in bpg._blueprints)

# Test case for initializing a BlueprintGroup with custom URL prefix and version
def test_blueprint_group_custom_parameters():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg._blueprints) == 2
    assert all(isinstance(bp, Blueprint) for bp in bpg._blueprints)
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"

# Test case for initializing a BlueprintGroup with strict slashes enabled
def test_blueprint_group_strict_slashes():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, strict_slashes=True)
    
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg._blueprints) == 2
    assert all(isinstance(bp, Blueprint) for bp in bpg._blueprints)
    assert bpg._strict_slashes is True

# Test case for iterating over a BlueprintGroup
def test_blueprint_group_iteration():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)
    
    assert isinstance(bpg, BlueprintGroup)
    blueprints = list(bpg)
    assert len(blueprints) == 2
    assert all(isinstance(bp, Blueprint) for bp in blueprints)

# Test case for adding a middleware to the group and checking its execution
@pytest.mark.asyncio
async def test_group_middleware(app):
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    group = Blueprint.group(bp1, bp2)
    
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(group)
    
    request, response = await app.asgi_client.get('/')
    assert response.status == 200
    assert 'bp1' in str(response.text)
    captured = capsys.readouterr()
    assert "common middleware applied for both bp1 and bp2" in captured.out
