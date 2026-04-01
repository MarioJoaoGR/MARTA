
import pytest
from unittest.mock import patch, MagicMock
import flutes.multiproc as multiproc

@pytest.fixture(autouse=True)
def mock_tqdm():
    with patch('flutes.multiproc.ProgressBarManager.Proxy') as MockTQDM:
        yield MockTQDM

class TestProgressBarManager:
    @patch('flutes.multiproc.ProgressBarManager._DummyProxy', autospec=True)
    def test_valid_inputs(self, mock_dummy_proxy):
        # Arrange
        xs = [1, 2, 3, 4]
        manager = multiproc.ProgressBarManager()
        
        # Act
        result = manager.run(xs, bar=manager.proxy)
        
        # Assert
        assert result == sum(xs)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_ProgressBarManager___init___0_test_valid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_ProgressBarManager___init___0_test_valid_inputs.py:19:17: E1101: Instance of 'ProgressBarManager' has no 'run' member; maybe '_run'? (no-member)


"""