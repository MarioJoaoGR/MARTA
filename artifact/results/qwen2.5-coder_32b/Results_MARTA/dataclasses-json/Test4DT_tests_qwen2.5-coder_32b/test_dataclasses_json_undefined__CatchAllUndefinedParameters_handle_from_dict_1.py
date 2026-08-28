
import pytest
from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

@dataclass
class MyClass(_CatchAllUndefinedParameters):
    known_param1: int
    known_param2: str
    catch_all: Optional[Dict] = field(default_factory=dict)







def test_handle_from_dict_with_conflicting_catch_all_field():
    kvs_conflict = {'known_param1': 90, 'known_param2': 'conflict_test', 'catch_all': 'not_a_dict'}
    with pytest.raises(UndefinedParameterError):
        MyClass.handle_from_dict(MyClass, kvs_conflict)