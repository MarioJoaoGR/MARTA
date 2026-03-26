
import os
from pathlib import Path
from typing import Iterable, Iterator

# Assuming this is the correct way to import Config from isort.config
try:
    from isort.config import Config
except ImportError:
    class Config:  # Mocking Config for testing purposes
        follow_links = False

        @staticmethod
        def is_skipped(path):
            return False

        @staticmethod
        def is_supported_filetype(filepath):
            return filepath.endswith('.py')

def find(
    paths: Iterable[str], config: Config, skipped: list[str], broken: list[str]
) -> Iterator[str]:
    """Fines and provides an iterator for all Python source files defined in the given paths."""
    visited_dirs: set[Path] = set()

    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(
                path, topdown=True, followlinks=config.follow_links
            ):
                base_path = Path(dirpath)
                for dirname in list(dirnames):
                    full_path = base_path / dirname
                    resolved_path = full_path.resolve()
                    if config.is_skipped(full_path):
                        skipped.append(str(full_path))
                        dirnames.remove(dirname)
                    else:
                        if resolved_path in visited_dirs:  # pragma: no cover
                            dirnames.remove(dirname)
                    visited_dirs.add(resolved_path)

                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if config.is_supported_filetype(filepath):
                        if config.is_skipped(Path(os.path.abspath(filepath))):
                            skipped.append(os.path.abspath(filepath))
                        else:
                            yield filepath
        elif not os.path.exists(path):
            broken.append(path)
        else:
            yield path

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.10s =============================
"""