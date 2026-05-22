
import pytest
from unittest.mock import patch, MagicMock
import importlib.metadata as importlib_metadata
from typing import Optional

def get_dist_name(entry_point: importlib_metadata.EntryPoint) -> Optional[str]:
    dist = getattr(entry_point, "dist", None)
    if dist is not None:  # Python 3.10+
        return dist.name

    match = entry_point.pattern.match(entry_point.value)
    if not (match and match.group('module')):
        return None

    package = match.group('module').split('.')[0]
    try:
        metadata = importlib_metadata.metadata(package)
    except importlib_metadata.PackageNotFoundError:
        return None
    else:
        return metadata.get('name')

@pytest.fixture
def valid_entry_point():
    ep = MagicMock()
    ep.dist = MagicMock()
    ep.dist.name = "valid_distribution"
    return ep

def test_valid_case(valid_entry_point):
    with patch('importlib.metadata.metadata', return_value={'name': 'valid_distribution'}):
        result = get_dist_name(valid_entry_point)
        assert result == "valid_distribution"
