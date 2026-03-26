
import pytest
from unittest.mock import patch, MagicMock
from flutes.multiproc import StatefulPoolType, PoolState

@pytest.fixture(autouse=True)
def mock_pool():
    with patch('flutes.multiproc.StatefulPoolType') as MockPool:
        pool = MockPool.return_value
        yield pool

def test_valid_case(mock_pool):
    # Create a mock state for each worker
    states = [PoolState() for _ in range(5)]
    
    # Patch the get_states method to return our mock states
    with patch.object(mock_pool, 'get_states', return_value=states):
        # Call the get_states method and check if it returns the expected list of states
        assert mock_pool.get_states() == states
