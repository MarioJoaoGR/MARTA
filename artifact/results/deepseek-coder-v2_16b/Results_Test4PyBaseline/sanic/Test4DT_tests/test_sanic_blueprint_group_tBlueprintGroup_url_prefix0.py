# Module: sanic.blueprint_group
import pytest
from sanic import Blueprint
from sanic.response import text
from sanic.blueprints import BlueprintGroup

# Create some blueprints for testing
bp1 = Blueprint('bp1', url_prefix='/bp1')
bp2 = Blueprint('bp2', url_prefix='/bp2')
bp3 = Blueprint('bp3', url_prefix='/bp3')
bp4 = Blueprint('bp4', url_prefix='/bp4')

# Define middleware and routes for individual blueprints
@bp1.middleware('request')
async def bp1_only_middleware(request):
    print('applied on Blueprint : bp1 Only')

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

# Register the Blueprint group under the app (mocked here for testing purposes)
app = type('MockSanic', (object,), {'blueprint': lambda self, bp: None})()
app.blueprint(group)
app.blueprint(BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1"))

# Test cases for BlueprintGroup class
def test_default_usage():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4)
    assert len(bpg._blueprints) == 2
    assert bpg.url_prefix() is None
    assert bpg.version is None
    assert bpg.strict_slashes is None

def test_custom_usage():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    assert len(bpg._blueprints) == 2
    assert bpg.url_prefix() == "/api"
    assert bpg.version == "v1"
    assert bpg.strict_slashes is None

def test_strict_slashes():
    bp3 = Blueprint('bp3', url_prefix='/bp3')
    bp4 = Blueprint('bp4', url_prefix='/bp4')
    bpg = BlueprintGroup(bp3, bp4, strict_slashes=True)
    assert len(bpg._blueprints) == 2
    assert bpg.strict_slashes is True

def test_middleware():
    request = type('MockRequest', (object,), {})()
    await group.middleware('request')(request)
    captured = capsys.readouterr()
    assert "common middleware applied for both bp1 and bp2" in captured.out

# Add more tests as necessary to cover different scenarios and edge cases
