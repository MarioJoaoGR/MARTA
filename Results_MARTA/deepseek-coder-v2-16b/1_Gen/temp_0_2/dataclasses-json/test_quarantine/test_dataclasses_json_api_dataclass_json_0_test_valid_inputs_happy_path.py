
import pytest
from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase, Undefined
from typing import List, Type, Optional, Union

@dataclass_json
@dataclass(frozen=True)
class Minion:
    name: str

@dataclass_json
@dataclass(frozen=True)
class Boss:
    minions: List[Minion]

def test_valid_inputs_happy_path():
    boss = Boss([Minion('evil minion'), Minion('very evil minion')])
    boss_json = """
{
    "minions": [
        {
            "name": "evil minion"
        },
        {
            "name": "very evil minion"
        }
    ]
}
""".strip()

    assert boss.to_json(indent=4) == boss_json
    assert Boss.from_json(boss_json) == boss

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_api_dataclass_json_0_test_valid_inputs_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_valid_inputs_happy_path.py:32:11: E1101: Instance of 'Boss' has no 'to_json' member (no-member)
dataclasses-json/Test4DT_tests/test_dataclasses_json_api_dataclass_json_0_test_valid_inputs_happy_path.py:33:11: E1101: Class 'Boss' has no 'from_json' member (no-member)


"""