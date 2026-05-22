
import pytest
from unittest.mock import patch, MagicMock
from rich import filesize

class BaseDisplay:
    def __init__(self):
        self.console = MagicMock()
    
    def _print_summary(self, is_finished: bool, observed_steps: int, time_spent: float):
        if is_finished:
            verb = 'Done'
        else:
            verb = 'Interrupted'

        total_size = filesize.decimal(observed_steps)
        avg_speed = filesize.decimal(observed_steps / time_spent)

        minutes, seconds = divmod(time_spent, 60)
        hours, minutes = divmod(int(minutes), 60)
        if hours:
            total_time = f'{hours:d}:{minutes:02d}:{seconds:0.5f}'
        else:
            total_time = f'{minutes:02d}:{seconds:0.5f}'

        self.console.print(
            f'[progress.description]{verb}. {total_size} in {total_time} ({avg_speed}/s)'
        )

@pytest.fixture
def base_display():
    return BaseDisplay()

def test_invalid_inputs(base_display):
    with pytest.raises(TypeError):  # Assuming the function should raise a TypeError for invalid inputs
        base_display._print_summary("finished", "steps", "time")
