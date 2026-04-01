
import pytest
from datetime import datetime, timezone
from dataclasses_json.utils import _timestamp_to_dt_aware

def test_edge_case():
    # Test with None input
    with pytest.raises(TypeError):
        assert _timestamp_to_dt_aware(None) is not None
