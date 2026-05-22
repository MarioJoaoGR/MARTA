
import pytest
from unittest.mock import patch, MagicMock
from rich import filesize

class StatusDisplay:
    def __init__(self):
        self.description = None
        self.observed = 0
        self.status = Console()

    def update(self, steps: float) -> None:
        from rich import filesize

        self.observed += steps

        observed_amount, observed_unit = filesize.decimal(
            self.observed
        ).split()
        self.status.update(
            status=f'{self.description} [progress.download]{observed_amount}/? {observed_unit}[/progress.download]'
        )

class Console:
    def update(self, status):
        pass

def test_invalid_input():
    with patch('rich.filesize.decimal', return_value='1024 bytes'):
        status_display = StatusDisplay()
        status_display.description = 'Downloading file'
        status_display.observed = 0
        status_display.status = Console()
        
        # Test with invalid input (string instead of float)
        with pytest.raises(TypeError):
            status_display.update('invalid_input')
