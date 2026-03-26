
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from isort.deprecated.finders import RequirementsFinder

def test_none_input():
    with pytest.raises(TypeError):
        RequirementsFinder._get_names_cached(None)
