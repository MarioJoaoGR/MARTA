
import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, Optional, Tuple
from dataclasses_json.undefined import UndefinedParameterError, _CatchAllUndefinedParameters, _UndefinedParameterAction

# Define a simple dataclass with a catch-all field
@dataclass
class MyDataClass:
    a: int = 0
    b: str = "default"
    catch_all: Optional[Dict] = None



def test_handle_from_dict_with_same_name_as_catch_all():
    kvs = {'a': 1, 'b': 'value', 'catch_all': 'unexpected'}
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_from_dict(MyDataClass, kvs)