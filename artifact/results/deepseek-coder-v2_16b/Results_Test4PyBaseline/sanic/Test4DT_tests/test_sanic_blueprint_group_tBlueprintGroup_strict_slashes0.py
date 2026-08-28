# Module: sanic.blueprint_group
import pytest
from sanic import Blueprint, Sanic
from sanic.response import text
from sanic.blueprints import BlueprintGroup

# Create a sample Sanic app for testing
app = Sanic("MyApp")

@pytest.fixture(scope="module")
def setup_blueprints():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    
    @bp3.route('/')
    async def bp3_route(request):
        return text('bp3')
    
    @bp4.route('/<param>')
    async def bp4_route(request, param):
        return text(param)
    
    group = Blueprint.group(bp1, bp2)
    
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(group)
    app.blueprint(BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1"))
    
    yield group, bp1, bp2, bp3, bp4

# Test cases for BlueprintGroup class
def test_blueprint_group_creation():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is None

def test_blueprint_group_with_custom_parameters():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is None

def test_blueprint_group_with_strict_slashes():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, strict_slashes=True)
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is True

def test_blueprint_group_middleware():
    group, bp1, bp2, bp3, bp4 = setup_blueprints()
    
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    
    request = app.test_client.get('/')
    assert request is not None
    assert request.status == 200
    assert request.text == 'bp1'

def test_blueprint_group_routes():
    group, bp1, bp2, bp3, bp4 = setup_blueprints()
    
    @bp3.route('/')
    async def bp3_route(request):
        return text('bp3')
    
    @bp4.route('/<param>')
    async def bp4_route(request, param):
        return text(param)
    
    request = app.test_client.get('/api/')
    assert request is not None
    assert request.status == 200
    assert request.text == 'bp3'

def test_blueprint_group_strict_slashes():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, strict_slashes=True)
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is True
