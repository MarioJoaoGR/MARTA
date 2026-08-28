
import pytest
from mimesis import Generic
from mimesis.random import Random
from enum import Enum
import random as random_module

# Define a mock for the Random class from mimesis.random
class MockRandom(Random):
    def choice(self, sequence):
        return sequence[0]  # Return the first item in the sequence

def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
    """Get random item of enum object.

    :param enum: Enum object.
    :param rnd: Custom random object.
    :return: Random item of enum.
    """
    if rnd and isinstance(rnd, MockRandom):
        return rnd.choice(list(enum))
    elif rnd and not isinstance(rnd, MockRandom):
        pytest.fail("Custom random object must be an instance of MockRandom")
    else:
        return random_module.choice(list(enum))

# Test 1: Default usage with Enum
def test_get_random_item_default():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    generic = Generic()
    rnd = MockRandom(seed=42)
    random_color = get_random_item(Color, rnd)
    assert random_color in [Color.RED, Color.GREEN, Color.BLUE]

# Test 2: Custom Random Object
def test_get_random_item_custom():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    custom_rnd = MockRandom(seed=42)
    random_color = get_random_item(Color, custom_rnd)
    assert random_color in [Color.RED, Color.GREEN, Color.BLUE]

# Test 3: Using Mimesis Generic for Custom Seeding
def test_get_random_item_mimesis():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    generic = Generic(seed=42)
    rnd = MockRandom(seed=42)
    random_color = get_random_item(Color, rnd)
    assert random_color in [Color.RED, Color.GREEN, Color.BLUE]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__________ ERROR collecting test_mimesis_random_get_random_item_0.py ___________
/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_get_random_item_0.py:13: in <module>
    def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
E   NameError: name 'Any' is not defined
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_random_get_random_item_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""