
import pytest
from isort.deprecated.finders import FindersManager, ForcedSeparateFinder, LocalFinder, KnownPatternFinder, PathFinder, RequirementsFinder, DefaultFinder
from unittest.mock import MagicMock

@pytest.fixture
def mock_config():
    return MagicMock()

def test_edge_cases(mock_config):
    # Test with None as finder_classes
    manager = FindersManager(config=mock_config, finder_classes=None)
    assert len(manager.finders) == 6  # Check if default finders are set

    # Test with empty list as finder_classes
    manager = FindersManager(config=mock_config, finder_classes=[])
    assert len(manager.finders) == 6  # Check if default finders are set

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___2_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

mock_config = <MagicMock id='139956682633232'>

    def test_edge_cases(mock_config):
        # Test with None as finder_classes
        manager = FindersManager(config=mock_config, finder_classes=None)
        assert len(manager.finders) == 6  # Check if default finders are set
    
        # Test with empty list as finder_classes
        manager = FindersManager(config=mock_config, finder_classes=[])
>       assert len(manager.finders) == 6  # Check if default finders are set
E       assert 0 == 6
E        +  where 0 = len(())
E        +    where () = <isort.deprecated.finders.FindersManager object at 0x7f4a34388a50>.finders

isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___2_test_edge_cases.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_deprecated_finders_FindersManager___init___2_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.14s ===============================
"""