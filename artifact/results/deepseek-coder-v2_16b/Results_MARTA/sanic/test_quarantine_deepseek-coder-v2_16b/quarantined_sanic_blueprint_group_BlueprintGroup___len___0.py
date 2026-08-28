
import pytest
from sanic import Sanic, Blueprint, text
from sanic.blueprints import BlueprintGroup

# Test 1: Basic Usage of BlueprintGroup

# Test 2: Adding More Blueprints to the Group

# Test 3: Using Strict Slashes Configuration in BlueprintGroup
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_basic_usage _______________________________

    def test_basic_usage():
        app = Sanic("MyApp")
    
        bp1 = Blueprint('bp1', url_prefix='/bp1')
        bp2 = Blueprint('bp2', url_prefix='/bp2')
    
        @bp1.middleware('request')
        async def bp1_only_middleware(request):
            print('applied on Blueprint : bp1 Only')
    
        @bp1.route('/')
        async def bp1_route(request):
            return text('bp1')
    
        @bp2.route('/<param>')
        async def bp2_route(request, param):
            return text(param)
    
>       bpg = BlueprintGroup(bp1, bp2, url_prefix="/api", version="v1")
E       TypeError: BlueprintGroup.__init__() got multiple values for argument 'url_prefix'

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py:25: TypeError
_________________________ test_adding_more_blueprints __________________________

    def test_adding_more_blueprints():
>       app = Sanic("MyApp")

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py:32: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/app.py:180: in __init__
    self.__class__.register_app(self)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'sanic.app.Sanic'>, app = Sanic(name="MyApp")

    @classmethod
    def register_app(cls, app: "Sanic") -> None:
        """
        Register a Sanic instance
        """
        if not isinstance(app, cls):
            raise SanicException("Registered app must be an instance of Sanic")
    
        name = app.name
        if name in cls._app_registry and not cls.test_mode:
>           raise SanicException(f'Sanic app name "{name}" already in use.')
E           sanic.exceptions.SanicException: Sanic app name "MyApp" already in use.

/opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/app.py:1246: SanicException
______________________ test_strict_slashes_configuration _______________________

    def test_strict_slashes_configuration():
>       app = Sanic("MyApp")

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py:60: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/app.py:180: in __init__
    self.__class__.register_app(self)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'sanic.app.Sanic'>, app = Sanic(name="MyApp")

    @classmethod
    def register_app(cls, app: "Sanic") -> None:
        """
        Register a Sanic instance
        """
        if not isinstance(app, cls):
            raise SanicException("Registered app must be an instance of Sanic")
    
        name = app.name
        if name in cls._app_registry and not cls.test_mode:
>           raise SanicException(f'Sanic app name "{name}" already in use.')
E           sanic.exceptions.SanicException: Sanic app name "MyApp" already in use.

/opt/marta/baselines/codamosa/replication/test-apps/sanic/sanic/app.py:1246: SanicException
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
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py::test_basic_usage
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py::test_adding_more_blueprints
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_blueprint_group_BlueprintGroup___len___0.py::test_strict_slashes_configuration
======================== 3 failed, 5 warnings in 0.18s =========================
"""