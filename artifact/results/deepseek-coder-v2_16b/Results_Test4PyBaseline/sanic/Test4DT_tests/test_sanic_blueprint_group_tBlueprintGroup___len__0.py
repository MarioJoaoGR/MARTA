# Module: sanic.blueprint_group
import pytest
from sanic import Sanic, Blueprint
from sanic.response import text
from sanic.blueprints import BlueprintGroup

# Fixture to create a test app with blueprints and group
@pytest.fixture
def app():
    app = Sanic("MyApp")
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    # Define middleware for individual blueprints
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    # Define routes for individual blueprints
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    
    # Define routes for BlueprintGroup blueprints
    @bp3.route('/')
    async def bp3_route(request):
        return text('bp3')
    
    @bp4.route('/<param>')
    async def bp4_route(request, param):
        return text(param)
    
    # Create a group from the blueprints and add middleware for the group
    group = Blueprint.group(bp1, bp2)
    
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    # Register the Blueprint group under the app
    app.blueprint(group)
    app.blueprint(bp3, bp4, url_prefix="/api", version="v1")
    
    return app

# Test case for checking the length of the blueprint group
def test_len_of_blueprint_group(app):
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert len(bpg) == 2

# Test case for checking the length of the blueprint group with default parameters
def test_len_of_blueprint_group_default():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)
    
    assert len(bpg) == 2

# Test case for checking the length of the blueprint group with custom URL prefix and version
def test_len_of_blueprint_group_custom():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    assert len(bpg) == 2

# Test case for checking the length of the blueprint group with strict slashes enabled
def test_len_of_blueprint_group_strict_slashes():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, strict_slashes=True)
    
    assert len(bpg) == 2
