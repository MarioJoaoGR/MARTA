
import pytest
from isort import settings
from isort.api import check_file
from pathlib import Path
import os
import subprocess

class Config:
    def __init__(self, settings_file="", settings_path="", config=None, **config_overrides):
        self._known_patterns = None
        self._section_comments = None
        self._section_comments_end = None
        self._skips = None
        self._skip_globs = None
        self._sorting_function = None

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
                warn(...)
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
                        warn(...)
                    else:
                        combined_config[section_name] = frozenset(value)
                else:
                    known_other[import_heading] = frozenset(value)
                    if maps_to_section not in combined_config.get("sections", ()) and not quiet:
                        warn(...)
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
                warn(...)

        if "directory" not in combined_config:
            combined_config["directory"] = (
                os.path.dirname(config_settings["source"])
                if config_settings.get("source", None)
                else os.getcwd()
            )

        path_root = Path(combined_config.get("directory", project_root)).resolve()
        path_root = path_root if path_root.is_dir() else path_root.parent
        if "src_paths" not in combined_config:
            combined_config["src_paths"] = (path_root / "src", path_root)
        else:
            src_paths: list[Path] = []
            for src_path in combined_config.get("src_paths", ()):
                full_paths = (
                    path_root.glob(src_path) if "*" in str(src_path) else [path_root / src_path]
                )
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
                warn(...)

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
                    unsupported_config_errors[option] = {
                        "value": source[option],
                        "source": source["source"],
                    }
        if unsupported_config_errors:
            raise UnsupportedSettings(unsupported_config_errors)

        super().__init__(sources=tuple(sources), **combined_config)

    def _check_folder_git_ls_files(self, folder: str) -> Path | None:
        env = {**os.environ, "LANG": "C.UTF-8"}
        try:
            topfolder_result = subprocess.check_output(["git", "-C", folder, "rev-parse", "--show-toplevel"], encoding="utf-8", env=env)  # nosec # skipcq: PYL-W1510
        except subprocess.CalledProcessError:
            return None

        git_folder = Path(topfolder_result.rstrip()).resolve()

        tracked_files = (
            subprocess.check_output(["git", "-C", str(git_folder), "ls-files", "-z"], encoding="utf-8", env=env)  # nosec # skipcq: PYL-W1510
            .rstrip("\0")
            .split("\0")
        )
        tracked_files_others = (
            subprocess.check_output(["git", "-C", str(git_folder), "ls-files", "-z", "--others", "--exclude-standard"], encoding="utf-8", env=env)  # nosec # skipcq: PYL-W1510
            .rstrip("\0")
            .split("\0")
        )

        self.git_ls_files[git_folder] = {str(git_folder / Path(f)) for f in tracked_files + tracked_files_others}
        return git_folder

@pytest.mark.parametrize("config", [Config()])
def test_valid_case(config):
    assert isinstance(config, Config)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:33:19: E0602: Undefined variable '_DEFAULT_SETTINGS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:38:30: E0602: Undefined variable '_get_config_data' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:38:62: E0602: Undefined variable 'CONFIG_SECTIONS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:38:115: E0602: Undefined variable 'FALLBACK_CONFIG_SECTIONS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:41:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:44:22: E0602: Undefined variable 'InvalidSettingsPath' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:47:44: E0602: Undefined variable '_find_config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:55:35: E0602: Undefined variable 'profiles' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:56:30: E0602: Undefined variable 'entry_points' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:57:20: E0602: Undefined variable 'profiles' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:59:35: E0602: Undefined variable 'profiles' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:60:22: E0602: Undefined variable 'ProfileDoesNotExist' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:62:22: E0602: Undefined variable 'profiles' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:69:41: E0602: Undefined variable 'RUNTIME_SOURCE' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:87:30: E0602: Undefined variable 'KNOWN_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:94:41: E0602: Undefined variable 'KNOWN_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:97:38: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:98:44: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:100:24: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:106:24: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:107:30: E0602: Undefined variable 'IMPORT_HEADING_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:108:40: E0602: Undefined variable 'IMPORT_HEADING_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:109:30: E0602: Undefined variable 'IMPORT_FOOTER_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:110:39: E0602: Undefined variable 'IMPORT_FOOTER_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:112:28: E0602: Undefined variable '_DEFAULT_SETTINGS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:119:26: E0602: Undefined variable 'SECTION_DEFAULTS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:124:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:150:26: E0602: Undefined variable 'entry_points' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:155:22: E0602: Undefined variable 'FormattingPluginDoesNotExist' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:161:85: E0602: Undefined variable 'DEPRECATED_SETTINGS' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:166:16: E0602: Undefined variable 'warn' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:172:39: E0602: Undefined variable 'IMPORT_HEADING_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:176:39: E0602: Undefined variable 'IMPORT_FOOTER_PREFIX' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:180:69: E0602: Undefined variable '_Config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:188:18: E0602: Undefined variable 'UnsupportedSettings' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config__check_folder_git_ls_files_1_test_valid_case.py:212:8: E1101: Instance of 'Config' has no 'git_ls_files' member (no-member)


"""