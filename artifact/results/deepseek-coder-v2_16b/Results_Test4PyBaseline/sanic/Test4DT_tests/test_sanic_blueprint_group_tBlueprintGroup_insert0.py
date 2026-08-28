# Module: sanic.blueprint_group
# Import the function using its provided module name.
from sanic.blueprints import BlueprintGroup
import pytest

# Test cases for BlueprintGroup class
def test_basic_usage():
    from sanic import Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    
def test_with_strict_slashes():
    from sanic import Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1", strict_slashes=True)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is True
    
def test_without_url_prefix_and_version():
    from sanic import Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix is None
    assert bpg._version is None
    assert bpg._strict_slashes is None
    
def test_insert():
    from sanic import Blueprint
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    
    bpg = BlueprintGroup(bp3, bp4)
    assert len(bpg._blueprints) == 2
    
    new_bp = Blueprint('new_bp', url_prefix='/new')
    bpg.insert(0, new_bp)
    assert len(bpg._blueprints) == 3
    assert bpg._blueprints[0] == new_bp
    
def test_sanitize_blueprint():
    from sanic import Blueprint
    bp = Blueprint('test', url_prefix='/test')
    bpg = BlueprintGroup(bp, url_prefix="/api", version="v1")
    
    sanitized_bp = bpg._sanitize_blueprint(bp)
    assert sanitized_bp.url_prefix == "/api/test"
    assert sanitized_bp.version == "v1"
    assert sanitized_bp.strict_slashes is True
    
def test_middleware():
    from sanic import Blueprint, Sanic
    app = Sanic("MyApp")
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    @app.route('/')
    async def handler(request):
        return text('bp1')
    
    group = Blueprint.group(bp1, bp2)
    
    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(group)
    request, response = await app.asgi_client.get('/')
    assert response.status == 200
    assert str(response.text) == 'bp1'
