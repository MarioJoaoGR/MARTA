# Module: sanic.blueprint_group
import pytest
from sanic import Blueprint, Sanic
from sanic.response import text
from typing import List

# Import the function from the module
from sanic.blueprints import BlueprintGroup

@pytest.fixture(scope="module")
def app():
    app = Sanic("TestApp")
    return app

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

@pytest.mark.asyncio
async def test_blueprint_group_creation(app, bp1, bp2, bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    # Check if the blueprints are correctly added to the group
    assert len(bpg._blueprints) == 2
    assert bp3 in bpg._blueprints
    assert bp4 in bpg._blueprints
    
    # Check if the URL prefix and version are set correctly
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"

@pytest.mark.asyncio
async def test_blueprint_group_methods(app, bp1, bp2):
    # Create a group from the blueprints and add middleware for the group
    group = Blueprint.group(bp1, bp2)
    
    @group.middleware('request')
    async def group_middleware(request):
        assert request is not None
        print('common middleware applied for both bp1 and bp2')
    
    # Register the Blueprint group under the app
    app.blueprint(group)
    app.blueprint(bpg)
    
    client = app.test_client
    
    # Test if the common middleware is applied
    response = await client().get('/')  # Assuming '/' is a valid endpoint for bp1 and bp2
    assert response is not None
    assert 'common middleware applied for both bp1 and bp2' in str(response.text)

@pytest.mark.asyncio
async def test_blueprint_group_blueprints_method(app, bp3, bp4):
    bpg = BlueprintGroup(bp3, bp4, url_prefix="/api", version="v1")
    
    # Check the blueprints method returns the correct list of blueprints
    blueprints_list = bpg.blueprints()
    assert len(blueprints_list) == 2
    assert bp3 in blueprints_list
    assert bp4 in blueprints_list
