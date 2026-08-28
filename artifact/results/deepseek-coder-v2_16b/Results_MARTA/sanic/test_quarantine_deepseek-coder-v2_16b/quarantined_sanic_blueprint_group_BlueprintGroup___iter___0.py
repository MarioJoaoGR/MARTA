
import pytest
from sanic import Sanic
from sanic.blueprint_group import BlueprintGroup, Blueprint
from sanic.response import text

# Test 1: Initialize a Blueprint Group with URL Prefix and Version
def test_initialize_blueprint_group():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    assert isinstance(bpg, BlueprintGroup)
    assert bpg._url_prefix == "/api"
    assert bpg._version == "v1"
    assert len(bpg._blueprints) == 2

# Test 2: Add Middleware to Individual Blueprints in the Group
def test_add_middleware_to_blueprint_group():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    @bp1.middleware('request')
    async def bp1_only_middleware(request):
        print('applied on Blueprint : bp1 Only')
    
    assert len(bp1._middlewares) == 1
    assert len(bpg._blueprints) == 2

# Test 3: Define Routes for Individual Blueprints in the Group
def test_define_routes_for_blueprint_group():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    @bp1.route('/')
    async def bp1_route(request):
        return text('bp1')
    
    @bp2.route('/<param>')
    async def bp2_route(request, param):
        return text(param)
    
    assert len(bp1._routes) == 1
    assert len(bp2._routes) == 1
    assert len(bpg._blueprints) == 2

# Test 4: Apply Common Middleware to the Blueprint Group
def test_apply_common_middleware_to_blueprint_group():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    @bpg.middleware('request')
    async def group_middleware(request):
        print('common middleware applied for both bp1 and bp2')
    
    assert len(bpg._middlewares) == 1
    assert len(bp1._middlewares) == 0
    assert len(bp2._middlewares) == 0

# Test 5: Register the Blueprint Group under a Sanic Application
def test_register_blueprint_group_under_sanic_app():
    app = Sanic("MyApp")
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    app.blueprint(bpg)
    
    assert len(app._blueprints) == 1
    assert isinstance(app._blueprints[0], BlueprintGroup)

# Test 6: Iterate Over Blueprint Group and Inspect Individual Blueprints
def test_iterate_over_blueprint_group():
    bp1 = Blueprint('bp1', url_prefix='/bp1')
    bp2 = Blueprint('bp2', url_prefix='/bp2')
    bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
    
    for bp in bpg:
        assert isinstance(bp, Blueprint)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
___ ERROR collecting test_sanic_blueprint_group_BlueprintGroup___iter___0.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___iter___0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___iter___0.py:4: in <module>
    from sanic.blueprint_group import BlueprintGroup, Blueprint
E   ImportError: cannot import name 'Blueprint' from 'sanic.blueprint_group' (/opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/blueprint_group.py)
=============================== warnings summary ===============================
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
  /opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13: DeprecationWarning: websockets.WebSocketCommonProtocol is deprecated
    from websockets import (  # type: ignore

../../../../pydeps/marta/websockets/legacy/__init__.py:6
  /data/pydeps/marta/websockets/legacy/__init__.py:6: DeprecationWarning: websockets.legacy is deprecated; see https://websockets.readthedocs.io/en/stable/howto/upgrade.html for upgrade instructions
    warnings.warn(  # deprecated in 14.0 - 2024-11-09

../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
../../../../../opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13
  /opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/websocket.py:13: DeprecationWarning: websockets.handshake is deprecated
    from websockets import (  # type: ignore

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___iter___0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
========================= 5 warnings, 1 error in 0.21s =========================
"""