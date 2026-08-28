# Module: sanic.blueprint_group
# test_blueprint_group.py
from sanic import Sanic, Blueprint
from sanic.response import text
from sanic.blueprints import BlueprintGroup
import pytest

@pytest.fixture(scope="module")
def app():
    app = Sanic("MyApp")
    yield app

@pytest.fixture(scope="module")
def bp1():
    return Blueprint('bp1', url_prefix='/bp1')

@pytest.fixture(scope="module")
def bp2():
    return Blueprint('bp2', url_prefix='/bp2')

@pytest.fixture(scope="module")
def bp3():
    return Blueprint('bp3', url_prefix='/bp3')

@pytest.fixture(scope="module")
def bp4():
    return Blueprint('bp4', url_prefix='/bp4')

@pytest.fixture(scope="module")
def bpg(bp3, bp4):
    return BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")

def test_blueprint_group_creation(bpg):
    assert isinstance(bpg, BlueprintGroup)
    assert len(bpg._blueprints) == 2
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"

def test_blueprint_group_access_by_index(bpg):
    bp = bpg[0]
    assert isinstance(bp, Blueprint)
    assert bp.name == 'bp3'
    assert bp.url_prefix == '/bp3'

def test_register_blueprints_in_app(app, bpg):
    app.blueprint(bpg)
    assert len(app.router.routes_all) == 4  # Assuming bp1, bp2, bp3, bp4 are registered

def test_add_middleware_to_group(bp1, bp2, bpg):
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    assert len(bpg._blueprints) == 2
    assert len(bp1.router.middleware['request']) == 1
    assert len(bp2.router.middleware['request']) == 0
    assert len(bpg.router.middleware['request']) == 1

def test_access_specific_blueprint_in_group(bpg):
    bp = bpg[0]
    assert isinstance(bp, Blueprint)
    assert bp.name == 'bp3'
    assert bp.url_prefix == '/bp3'
