
import pytest
from distutils.version import StrictVersion
from flutils.packages import _build_version_info, _VersionInfo, _each_version_part


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__build_version_info_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        version = "1.2.3"
        ver_info = _build_version_info(version)
        assert isinstance(ver_info, _VersionInfo)
        assert ver_info.version == "1.2.3"
>       assert ver_info.prerelease is None
E       AttributeError: '_VersionInfo' object has no attribute 'prerelease'

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__build_version_info_1.py:11: AttributeError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        version = None
        with pytest.raises(TypeError):
>           _build_version_info(version)

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__build_version_info_1.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/packages.py:104: in _build_version_info
    for part in _each_version_part(ver_obj):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

ver_obj = <[AttributeError("'StrictVersion' object has no attribute 'version'") raised in repr()] StrictVersion object at 0x7f57bbed9f30>

    def _each_version_part(
            ver_obj: StrictVersion,
    ) -> Generator[_VersionPart, None, None]:
>       version: Tuple[int, int, int] = ver_obj.version
E       AttributeError: 'StrictVersion' object has no attribute 'version'. Did you mean: 'version_re'?

/opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/packages.py:56: AttributeError
=============================== warnings summary ===============================
test_flutils_packages__build_version_info_1.py::test_valid_input_happy_path
test_flutils_packages__build_version_info_1.py::test_edge_case_none
  /opt/marta/baselines/codamosa/replication/test-apps/flutils/flutils/packages.py:101: DeprecationWarning: distutils Version classes are deprecated. Use packaging.version instead.
    ver_obj = StrictVersion(version)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__build_version_info_1.py::test_valid_input_happy_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_packages__build_version_info_1.py::test_edge_case_none
======================== 2 failed, 2 warnings in 0.13s =========================
"""