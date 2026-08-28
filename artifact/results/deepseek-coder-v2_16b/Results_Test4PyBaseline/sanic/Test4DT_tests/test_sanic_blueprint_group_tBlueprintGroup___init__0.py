# Module: sanic.blueprint_group
import pytest
from sanic import Sanic, Blueprint
from sanic.response import text
from sanic.blueprints import BlueprintGroup

# Create a test app
app = Sanic("TestApp")

@pytest.fixture(scope="module")
def event_loop():
    loop = pytest.importorskip("asyncio").get_event_loop()
    yield loop
    loop.close()

# Test cases for BlueprintGroup class
def test_blueprintgroup_creation():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is None

def test_blueprintgroup_middleware():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(bpg)
    
    request, response = await app.asgi_client.get("/api/example")
    assert response.status == 200
    assert "Example route in blueprint 1" in str(response.text)

def test_blueprintgroup_strict_slashes():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.route('/example')
    async def bp1_route(request):
        return text('Example route in blueprint 1')
    
    @bp2.route('/example')
    async def bp2_route(request):
        return text('Example route in blueprint 2')
    
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1", strict_slashes=True)
    
    app.blueprint(bpg)
    
    request, response = await app.asgi_client.get("/api/example")
    assert response.status == 200
    assert "Example route in blueprint 1" in str(response.text)

def test_blueprintgroup_versioning():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    
    @bp1.route('/example')
    async def bp1_route(request):
        return text('Example route in blueprint 1')
    
    @bp2.route('/example')
    async def bp2_route(request):
        return text('Example route in blueprint 2')
    
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    app.blueprint(bpg)
    
    request, response = await app.asgi_client.get("/api/example")
    assert response.status == 200
    assert "Example route in blueprint 1" in str(response.text)
