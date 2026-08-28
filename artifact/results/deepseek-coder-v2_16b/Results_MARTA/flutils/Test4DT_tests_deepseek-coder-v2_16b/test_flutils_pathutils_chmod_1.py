
import pytest
from pathlib import Path
from flutils.pathutils import chmod

def test_chmod_single_file():
    home = str(Path.home())
    target_file = Path(f'{home}/tmp/flutils.tests.osutils.txt')
    if not target_file.exists():
        target_file.touch()
    chmod(target_file, mode_file=0o660)
    assert target_file.stat().st_mode & 0o777 == 0o660

