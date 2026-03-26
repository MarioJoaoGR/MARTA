
import os
import pytest
from isort import sorting
from isort.entry_points import entry_points
from isort.exceptions import SortingFunctionDoesNotExist, UnsupportedSettings
from isort.profiles import profiles
from isort.settings import _Config, CONFIG_SECTIONS, FALLBACK_CONFIG_SECTIONS, DEPRECATED_SETTINGS, KNOWN_PREFIX, IMPORT_HEADING_PREFIX, IMPORT_FOOTER_PREFIX, SECTION_DEFAULTS, _DEFAULT_SETTINGS
from isort.utils import Path

class Config(_Config):
    def __init__(self, settings_file="", settings_path="", config=None, **config_overrides):
        if config:
            config_vars = vars(config).copy()
            config_vars.update(config_overrides)
            config_vars["py_version"] = config_vars["py_version"].replace("py", "")
            config_vars.pop("_known_patterns")
            config_vars.pop("_section_comments")
            config_vars.pop("_section_comments_end")
            config_vars.pop("_skips")
            config_vars.pop("_skip_globs")
            config_vars.pop("_sorting_function")
            super().__init__(**config_vars)
            return

        quiet = config_overrides.get("quiet", False)
        sources = [_DEFAULT_SETTINGS]

        config_settings = {}
        project_root = ""
        if settings_file:
            config_settings = _get_config_data(settings_file, CONFIG_SECTIONS.get(os.path.basename(settings_file), FALLBACK_CONFIG_SECTIONS))
            project_root = os.path.dirname(settings_file)
            if not config_settings and not quiet:
                warn(f"A custom settings file was specified: {settings_file} but no configuration was found inside. This can happen when [settings] is used as the config header instead of [isort]. See: https://pycqa.github.io/isort/docs/configuration/config_files#custom-config-files for more information.", stacklevel=2)
        elif settings_path:
            if not os.path.exists(settings_path):
                raise InvalidSettingsPath(settings_path)

            settings_path = os.path.abspath(settings_path)
            project_root, config_settings = _find_config(settings_path)
        else:
            config_settings = {}
            project_root = os.getcwd()

        profile_name = config_overrides.get("profile", config_settings.get("profile", ""))
        profile = {}
        if profile_name:
            if profile_name not in profiles:
                for plugin in entry_points(group="isort.profiles"):
                    profiles.setdefault(plugin.name, plugin.load())

            if profile_name not in profiles:
                raise ProfileDoesNotExist(profile_name)

            profile = profiles[profile_name].copy()
            profile["source"] = f"{profile_name} profile"
            sources.append(profile)

        if config_settings:
            sources.append(config_settings)
        if config_overrides:
            config_overrides["source"] = RUNTIME_SOURCE
            sources.append(config_overrides)

        combined_config = {**profile, **config_settings, **config_overrides}
        if "indent" in combined_config:
            indent = str(combined_config["indent"])
            if indent.isdigit():
                indent = " " * int(indent)
            else:
                indent = indent.strip("'").strip('"')
                if indent.lower() == "tab":
                    indent = "\t"
            combined_config["indent"] = indent

        known_other = {}
        import_headings = {}
        import_footers = {}
        for key, value in tuple(combined_config.items()):
            if key.startswith(KNOWN_PREFIX) and key not in (
                "known_standard_library",
                "known_future_library",
                "known_third_party",
                "known_first_party",
                "known_local_folder",
            ):
                import_heading = key[len(KNOWN_PREFIX) :].lower()
                maps_to_section = import_heading.upper()
                combined_config.pop(key)
                if maps_to_section in KNOWN_SECTION_MAPPING:
                    section_name = f"known_{KNOWN_SECTION_MAPPING[maps_to_section].lower()}"
                    if section_name in combined_config and not quiet:
                        warn(f"Can't set both {key} and {section_name} in the same config file.\nDefault to {section_name} if unsure." "\n\n" "See: https://pycqa.github.io/isort/#custom-sections-and-ordering.", stacklevel=2)
                    else:
                        combined_config[section_name] = frozenset(value)
                else:
                    known_other[import_heading] = frozenset(value)
                    if maps_to_section not in combined_config.get("sections", ()) and not quiet:
                        warn(f"`{key}` setting is defined, but {maps_to_section} is not included in `sections` config option:" f"{combined_config.get('sections', SECTION_DEFAULTS)}.\n\n" "See: https://pycqa.github.io/isort/#custom-sections-and-ordering.", stacklevel=2)
            if key.startswith(IMPORT_HEADING_PREFIX):
                import_headings[key[len(IMPORT_HEADING_PREFIX) :].lower()] = str(value)
            if key.startswith(IMPORT_FOOTER_PREFIX):
                import_footers[key[len(IMPORT_FOOTER_PREFIX) :].lower()] = str(value)

            default_value = _DEFAULT_SETTINGS.get(key, None)
            if default_value is None:
                continue

            combined_config[key] = type(default_value)(value)

        for section in combined_config.get("sections", ()):
            if section in SECTION_DEFAULTS:
                continue

            if section.lower() not in known_other:
                config_keys = ", ".join(known_other.keys())
                warn(f"`sections` setting includes {section}, but no known_{section.lower()} is defined. The following known_SECTION config options are defined: {config_keys}.", stacklevel=2)

        if "directory" not in combined_config:
            combined_config["directory"] = (os.path.dirname(config_settings["source"]) if config_settings.get("source", None) else os.getcwd())

        path_root = Path(combined_config.get("directory", project_root)).resolve()
        path_root = path_root if path_root.is_dir() else path_root.parent
        if "src_paths" not in combined_config:
            combined_config["src_paths"] = (path_root / "src", path_root)
        else:
            src_paths: list[Path] = []
            for src_path in combined_config.get("src_paths", ()):
                full_paths = (path_root.glob(src_path) if "*" in str(src_path) else [path_root / src_path])
                for path in full_paths:
                    if path not in src_paths:
                        src_paths.append(path)

            combined_config["src_paths"] = tuple(src_paths)

        if "formatter" in combined_config:
            for plugin in entry_points(group="isort.formatters"):
                if plugin.name == combined_config["formatter"]:
                    combined_config["formatting_function"] = plugin.load()
                    break
            else:
                raise FormattingPluginDoesNotExist(combined_config["formatter"])

        combined_config.pop("source", None)
        combined_config.pop("sources", None)
        combined_config.pop("runtime_src_paths", None)

        deprecated_options_used = [option for option in combined_config if option in DEPRECATED_SETTINGS]
        if deprecated_options_used:
            for deprecated_option in deprecated_options_used:
                combined_config.pop(deprecated_option)
            if not quiet:
                warn(f"W0503: Deprecated config options were used: {', '.join(deprecated_options_used)}. Please see the 5.0.0 upgrade guide: https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0.html", stacklevel=2)

        if known_other:
            combined_config["known_other"] = known_other
        if import_headings:
            for import_heading_key in import_headings:
                combined_config.pop(f"{IMPORT_HEADING_PREFIX}{import_heading_key}")
            combined_config["import_headings"] = import_headings
        if import_footers:
            for import_footer_key in import_footers:
                combined_config.pop(f"{IMPORT_FOOTER_PREFIX}{import_footer_key}")
            combined_config["import_footers"] = import_footers

        unsupported_config_errors = {}
        for option in set(combined_config.keys()).difference(getattr(_Config, "__dataclass_fields__", {}).keys()):
            for source in reversed(sources):
                if option in source:
                    unsupported_config_errors[option] = {"value": source[option], "source": source["source"]}
        if unsupported_config_errors:
            raise UnsupportedSettings(unsupported_config_errors)

        super().__init__(sources=tuple(sources), **combined_config)

    def sorting_function(self) -> Callable[..., list[str]]:
        if self._sorting_function is not None:
            return self._sorting_function

        if self.sort_order == "natural":
            self._sorting_function = sorting.naturally
        elif self.sort_order == "native":
            self._sorting_function = sorted
        else:
            available_sort_orders = ["natural", "native"]
            for sort_plugin in entry_points(group="isort.sort_function"):
                available_sort_orders.append(sort_plugin.name)
                if sort_plugin.name == self.sort_order:
                    self._sorting_function = sort_plugin.load()
                    break
            else:
                raise SortingFunctionDoesNotExist(self.sort_order, available_sort_orders)

        return self._sorting_function

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_sorting_function_0_test_edge_cases
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:5:0: E0401: Unable to import 'isort.entry_points' (import-error)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:5:0: E0611: No name 'entry_points' in module 'isort' (no-name-in-module)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:32:30: E0602: Undefined variable '_get_config_data' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:35:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:38:22: E0602: Undefined variable 'InvalidSettingsPath' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:41:44: E0602: Undefined variable '_find_config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:54:22: E0602: Undefined variable 'ProfileDoesNotExist' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:63:41: E0602: Undefined variable 'RUNTIME_SOURCE' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:91:38: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:92:44: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:94:24: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:100:24: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:118:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:143:22: E0602: Undefined variable 'FormattingPluginDoesNotExist' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:154:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:177:34: E0602: Undefined variable 'Callable' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:178:11: E0203: Access to member '_sorting_function' before its definition line 182 (access-member-before-definition)
isort/Test4DT_tests/test_isort_settings_Config_sorting_function_0_test_edge_cases.py:179:19: E0203: Access to member '_sorting_function' before its definition line 182 (access-member-before-definition)


"""