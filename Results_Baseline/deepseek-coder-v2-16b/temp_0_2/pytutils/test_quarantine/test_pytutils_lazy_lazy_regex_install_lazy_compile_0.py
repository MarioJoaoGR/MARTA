
import pytest
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile
import re

# Mocking the lazy_compile function for testing purposes
def mock_lazy_compile(*args, **kwargs):
    return "mocked_lazy_compile"

@pytest.fixture(autouse=True)
def setup():
    # Backup the original re.compile before setting it to mock_lazy_compile
    global original_re_compile
    original_re_compile = re.compile
    re.compile = mock_lazy_compile

@pytest.fixture(autouse=True)
def teardown():
    yield  # Ensure test runs are completed before resetting the mock
    # Reset re.compile to its original function after each test
    re.compile = original_re_compile

def test_install_lazy_compile():
    """Test that install_lazy_compile() sets re.compile to lazy_compile."""
    from pytutils.lazy.lazy_regex import install_lazy_compile
    install_lazy_compile()
    assert callable(re.compile) and re.compile == mock_lazy_compile

def test_reset_compile():
    """Test that reset_compile() restores re.compile to its original function."""
    from pytutils.lazy.lazy_regex import reset_compile
    install_lazy_compile()
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_install_lazy_compile ___________________________

    def test_install_lazy_compile():
        """Test that install_lazy_compile() sets re.compile to lazy_compile."""
        from pytutils.lazy.lazy_regex import install_lazy_compile
        install_lazy_compile()
>       assert callable(re.compile) and re.compile == mock_lazy_compile
E       assert (True and <function lazy_compile at 0x7f0c1342af20> == mock_lazy_compile)
E        +  where True = callable(<function lazy_compile at 0x7f0c1342af20>)
E        +    where <function lazy_compile at 0x7f0c1342af20> = re.compile
E        +  and   <function lazy_compile at 0x7f0c1342af20> = re.compile

pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_lazy_lazy_regex_install_lazy_compile_0.py::test_install_lazy_compile
========================= 1 failed, 1 passed in 0.05s ==========================
"""