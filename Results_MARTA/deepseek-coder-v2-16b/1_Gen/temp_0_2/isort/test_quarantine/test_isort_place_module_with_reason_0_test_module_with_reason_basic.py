
from isort.place import Config, DEFAULT_CONFIG

def _forced_separate(name: str, config: Config) -> tuple[str, str] | None:
    for pattern in config.forced_separate:
        if fnmatch.fnmatch(name, pattern):
            return (f"Forced separate {pattern}", f"Matched forced_separate ({pattern}) config value.")
    return None

def _local(name: str, config: Config) -> tuple[str, str] | None:
    if name.startswith('.'):
        return ('LOCAL', 'Module name started with a dot.')
    return None

def _known_pattern(name: str, config: Config) -> tuple[str, str] | None:
    for pattern, section in config.known_patterns:
        if re.match(pattern, name):
            return (section, f"Matched configured known pattern <regex_pattern>")
    return None

def _src_path(name: str, config: Config) -> tuple[str, str] | None:
    for src_path in config.src_paths:
        if Path(src_path).joinpath(name.replace('.', os.sep)).exists():
            return (config.default_section, f"Found in one of the configured src_paths: {src_path}.")
    return None

def module_with_reason(name: str, config: Config = DEFAULT_CONFIG) -> tuple[str, str]:
    """Returns the section placement for the given module name alongside the reasoning."""
    return (
        _forced_separate(name, config)
        or _local(name, config)
        or _known_pattern(name, config)
        or _src_path(name, config)
        or (config.default_section, "Default option in Config or universal default.")
    )

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place_module_with_reason_0_test_module_with_reason_basic
isort/Test4DT_tests/test_isort_place_module_with_reason_0_test_module_with_reason_basic.py:6:11: E0602: Undefined variable 'fnmatch' (undefined-variable)
isort/Test4DT_tests/test_isort_place_module_with_reason_0_test_module_with_reason_basic.py:17:11: E0602: Undefined variable 're' (undefined-variable)
isort/Test4DT_tests/test_isort_place_module_with_reason_0_test_module_with_reason_basic.py:23:11: E0602: Undefined variable 'Path' (undefined-variable)
isort/Test4DT_tests/test_isort_place_module_with_reason_0_test_module_with_reason_basic.py:23:53: E0602: Undefined variable 'os' (undefined-variable)


"""