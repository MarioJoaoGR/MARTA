
import pytest
from enum import Enum
from random import Random
import random as random_module
from mimesis import Generic
from typing import Any, Optional

# Assuming get_random_item is defined as per the provided function documentation.
def get_random_item(enum: Any, rnd: Optional[Random] = None) -> Any:
    if rnd and isinstance(rnd, Random):
        return rnd.choice(list(enum))
    return random_module.choice(list(enum))

# Test for valid enum input
def test_valid_enum_input():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    random_color = get_random_item(Color)
    assert random_color in [Color.RED, Color.GREEN, Color.BLUE]

# Test for custom Random object input
def test_custom_random_input():
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
    
    custom_rnd = Random()
    random_color = get_random_item(Color, custom_rnd)
    assert random_color in [Color.RED, Color.GREEN, Color.BLUE]

# Test for invalid enum type input
def test_invalid_enum_input():
    generic = Generic()
    with pytest.raises(TypeError):
        random_color = get_random_item(generic.random.choice)
