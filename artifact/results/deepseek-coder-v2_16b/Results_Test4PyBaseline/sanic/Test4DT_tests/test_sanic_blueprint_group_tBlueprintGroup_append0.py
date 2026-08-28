# Module: sanic.blueprint_group
# test_blueprint_group.py
from sanic import Blueprint, Sanic
from sanic.response import text
from sanic.blueprints import BlueprintGroup
import pytest

@pytest.fixture
def app():
    app = Sanic("MyApp")
    return app

@pytest.fixture
def bp1(app):
    bp = Blueprint('bp1', url_prefix='/bp1')
    @bp.route('/')
    async def bp1_route(request):
        return text('bp1')
    app.blueprint(bp)
    return bp

@pytest.fixture
def bp2(app):
    bp = Blueprint('bp2', url_prefix='/bp2')
    @bp.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    app.blueprint(bp)
    return bp

@pytest.fixture
def bp3(app):
    bp = Blueprint('bp3', url_prefix='/bp3')
    @bp.route('/')
    async def bp3_route(request):
        return text('bp3')
    app.blueprint(bp)
    return bp

@pytest.fixture
def bp4(app):
    bp = Blueprint('bp4', url_prefix='/bp4')
    @bp.route('/<param>')
    async def bp4_route(request, param):
        return text(param)
    app.blueprint(bp)
    return bp

def test_blueprint_group_creation(app, bp1, bp2, bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    app.blueprint(bpg)

    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    # Register the grouped blueprint under the app
    app.blueprint(bpg)

    request, response = await app.asgi_client.get("/api/")
    assert response.status == 200
    assert "bp3" in str(response.text)

def test_group_middleware(app, bp1, bp2):
    group = Blueprint.group(bp1, bp2)
    app.blueprint(group)
    app.blueprint(BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1"))

    @group.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')

    request, response = await app.asgi_client.get("/")
    assert response.status == 200
    assert "bp1" in str(response.text)

def test_blueprint_group_with_app(app, bp1, bp2, bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    app.blueprint(bpg)

    request, response = await app.asgi_client.get("/api/")
    assert response.status == 200
    assert "bp3" in str(response.text)

    group = Blueprint.group(bp1, bp2)
    app.blueprint(group)

    request, response = await app.asgi_client.get("/")
    assert response.status == 200
    assert "bp1" in str(response.text)
