
import pytest
from unittest.mock import patch
from typesystem.composites import AllOf, Field



def test_invalid_input():
    with pytest.raises(TypeError):
        AllOf()