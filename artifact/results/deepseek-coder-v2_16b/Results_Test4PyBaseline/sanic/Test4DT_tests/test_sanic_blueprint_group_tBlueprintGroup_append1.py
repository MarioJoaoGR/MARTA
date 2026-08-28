
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

def test_append_with_valid_blueprint(app, bp1, bp2):
    bpg = BlueprintGroup()
    assert len(bpg._blueprints) == 0
    bpg.append(bp1)
    assert len(bpg._blueprints) == 1
    assert isinstance(bpg._blueprints[0], type(bp1))

def test_append_with_invalid_input():
    bpg = BlueprintGroup()
    with pytest.raises(TypeError):
        bpg.append("not a Blueprint")

def test_append_multiple_blueprints(app, bp1, bp2):
    bpg = BlueprintGroup()
    assert len(bpg._blueprints) == 0
    bpg.append(bp1)
    bpg.append(bp2)
    assert len(bpg._blueprints) == 2
    assert isinstance(bpg._blueprints[0], type(bp1))
    assert isinstance(bpg._blueprints[1], type(bp2))

def test_append_and_access_by_index(app, bp1):
    bpg = BlueprintGroup()
    bpg.append(bp1)
    assert len(bpg._blueprints) == 1
    retrieved_bp = bpg[0]
    assert isinstance(retrieved_bp, type(bp1))

def test_append_and_check_sanitization(app, bp1):
    bpg = BlueprintGroup()
    original_bp = bp1
    sanitized_bp = bpg._sanitize_blueprint(bp=original_bp)
    assert isinstance(sanitized_bp, type(bp1))
    bpg.append(original_bp)
    assert len(bpg._blueprints) == 1
    assert isinstance(bpg._blueprints[0], type(bp1))
