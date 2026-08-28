# Module: sanic.blueprint_group
# test_blueprint_group.py
from sanic import Blueprint, Sanic
from sanic.response import text
from sanic.blueprints import BlueprintGroup
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("MyApp")
    return app

@pytest.fixture(scope="module")
def bp1():
    bp = Blueprint('bp1', url_prefix='/bp1')
    @bp.route('/')
    async def bp1_route(request):
        return text('bp1')
    return bp

@pytest.fixture(scope="module")
def bp2():
    bp = Blueprint('bp2', url_prefix='/bp2')
    @bp.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    return bp

@pytest.fixture(scope="module")
def bp3():
    bp = Blueprint('bp3', url_prefix='/bp3')
    @bp.route('/')
    async def bp3_route(request):
        return text('bp3')
    return bp

@pytest.fixture(scope="module")
def bp4():
    bp = Blueprint('bp4', url_prefix='/bp4')
    @bp.route('/<param>')
    async def bp4_route(request, param):
        return text(param)
    return bp

@pytest.fixture(scope="module")
def bpg():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    return bpg

def test_blueprint_group_initialization(bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is None

def test_blueprint_group_with_optional_parameters(bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1", strict_slashes=True)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert bpg._strict_slashes is True

def test_registering_grouped_blueprint(app, bp1, bp2, bpg):
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(bpg)
    request, response = await app.asgi_client.get("/api/")
    assert response.status == 200
    assert response.text == 'bp3'

def test_sanitize_blueprint(bp3):
    bpg = BlueprintGroup()
    sanitized_bp = bpg._sanitize_blueprint(bp3)
    assert sanitized_bp.url_prefix == "/bp3"
    assert sanitized_bp.version == None
    assert sanitized_bp.strict_slashes is False
