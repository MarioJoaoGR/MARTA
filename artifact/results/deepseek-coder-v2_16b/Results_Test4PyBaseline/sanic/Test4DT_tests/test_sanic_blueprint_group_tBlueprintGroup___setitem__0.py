# Module: sanic.blueprint_group
# test_blueprint_group.py
from sanic import Sanic, Blueprint
from sanic.response import text
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("TestApp")
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

def test_blueprint_group_creation(app, bp1, bp2, bpg):
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"

def test_middleware_application(app, bp1, bp2, bpg):
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    app.blueprint(bp1)
    app.blueprint(bp2)
    app.blueprint(bpg)

    @app.route('/test')
    async def test_route(request):
        return text('Test route')

    request, response = await app.asgi_client.get("/test")
    assert response.status == 200
    assert "common middleware applied for both bp1 and bp2" in str(app.config['LOG'].info)

def test_blueprint_group_methods(bp1, bp2, bpg):
    group = Blueprint.group(bp1, bp2)
    assert isinstance(group, BlueprintGroup)
    assert len(group._blueprints) == 2
    assert group._url_prefix is None
    assert group._version is None
