# Module: sanic.blueprint_group
# Import the BlueprintGroup class from the sanic.blueprint_group module
from sanic.blueprint_group import BlueprintGroup

def test_BlueprintGroup_creation():
    # Create some blueprints for testing
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    # Create a BlueprintGroup instance with the blueprints, url_prefix, version, and strict_slashes
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert isinstance(bpg, BlueprintGroup), "BlueprintGroup instance should be created correctly"
    assert len(bpg._blueprints) == 2, "The BlueprintGroup should contain the two blueprints"
    assert bpg._url_prefix == "/api", "The url_prefix should be '/api'"
    assert bpg._version == "v1", "The version should be 'v1'"
    assert bpg._strict_slashes is None, "Strict slashes should default to None"

def test_BlueprintGroup_middleware():
    # Create a Sanic app for testing
    from sanic import Sanic
    from sanic.response import text
    from sanic.blueprints import Blueprint, BlueprintGroup
    
    app = Sanic("MyApp")
    
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
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
    app.blueprint(bpg)
    
    # Test the middleware functionality
    assert len([m for m in app.middlewares if callable(m)]) == 2, "There should be two middlewares applied"
    assert hasattr(bp1, 'middleware'), "Blueprint bp1 should have a middleware method"
    assert hasattr(bp2, 'middleware'), "Blueprint bp2 should have a middleware method"
    assert hasattr(group, 'middleware'), "The group should have a middleware method"
    assert hasattr(bpg, 'middleware'), "The BlueprintGroup bpg should have a middleware method"
    
    # Test the recursive application of middleware in nested groups
    @bp3.middleware('request')
    async def bp3_middleware(request):
        print('applied on Blueprint : bp3 Only')
    
    @bp4.middleware('request')
    async def bp4_middleware(request):
        print('applied on Blueprint : bp4 Only')
    
    assert len([m for m in app.middlewares if callable(m)]) == 4, "There should be four middlewares applied"
