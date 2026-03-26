
import os
import re
import stat
from pathlib import Path
from typing import Any, Callable, Pattern
from warnings import warn
from isort.profiles import profiles, entry_points
from isort.settings import (
    _DEFAULT_SETTINGS,
    CONFIG_SECTIONS,
    FALLBACK_CONFIG_SECTIONS,
    KNOWN_PREFIX,
    IMPORT_HEADING_PREFIX,
    IMPORT_FOOTER_PREFIX,
    SECTION_DEFAULTS,
    DEPRECATED_SETTINGS,
    RUNTIME_SOURCE,
)
from isort.exceptions import (
    InvalidSettingsPath,
    ProfileDoesNotExist,
    UnsupportedSettings,
    FormattingPluginDoesNotExist,
)

class Config:
    """
    Initializes a configuration object for isort, which is used to manage Python import sorting and formatting settings. The class supports initialization from either a provided config object or by specifying file paths for configuration files. It also allows overriding settings via keyword arguments.
    
    Parameters:
        - `settings_file` (str): Path to a TOML or INI configuration file. If specified, isort will attempt to read its settings from this file.
        - `settings_path` (str): Path to a directory where isort can search for configuration files. This option is used when the configuration needs to be discovered within the project root.
        - `config` (_Config | None): An existing config object that contains initial settings which can be overridden by other parameters. If provided, this will take precedence over file-based configurations.
        - **config_overrides`: Keyword arguments for overriding specific configuration settings. Each key should match a valid isort setting name.
        
    Examples:
        >>> # Initialize from a TOML or INI configuration file specified by path
        >>> config = Config(settings_file="path/to/isort_config.toml")
        
        >>> # Initialize from an existing config object, overriding specific settings
        >>> existing_config = _Config()  # Assuming _Config is defined elsewhere
        >>> custom_config = Config(config=existing_config, quiet=True)
        
        >>> # Discover configuration files within a specified directory
        >>> project_config = Config(settings_path="path/to/project")
    
    Notes:
        - If both `settings_file` and `settings_path` are provided, `settings_file` takes precedence.
        - Configuration settings can be overridden by passing keyword arguments to the constructor.
        - The function supports TOML or INI configuration files based on their file extensions.
        - When using a custom config object, ensure that it includes all necessary settings and overrides as needed.
    """
    
    def __init__(
        self,
        settings_file: str = "",
        settings_path: str = "",
        config: _Config | None = None,
        **config_overrides: Any,
    ):
        self._known_patterns: list[tuple[Pattern[str], str]] | None = None
        self._section_comments: tuple[str, ...] | None = None
        self._section_comments_end: tuple[str, ...] | None = None
        self._skips: frozenset[str] | None = None
        self._skip_globs: frozenset[str] | None = None
        self._sorting_function: Callable[..., list[str]] | None = None

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

        # We can't use self.quiet to conditionally show warnings before super.__init__() is called
        # at the end of this method. _Config is also frozen so setting self.quiet isn't possible.
        # Therefore we extract quiet early here in a variable and use that in warning conditions.
        quiet = config_overrides.get("quiet", False)

        sources: list[dict[str, Any]] = [_DEFAULT_SETTINGS]

        config_settings: dict[str, Any]
        project_root: str
        if settings_file:
            config_settings = _get_config_data(
                settings_file,
                CONFIG_SECTIONS.get(os.path.basename(settings_file), FALLBACK_CONFIG_SECTIONS),
            )
            project_root = os.path.dirname(settings_file)
            if not config_settings and not quiet:
                warn(
                    f"A custom settings file was specified: {settings_file} but no configuration "
                    "was found inside. This can happen when [settings] is used as the config "
                    "header instead of [isort]. "
                    "See: https://pycqa.github.io/isort/docs/configuration/config_files"
                    "#custom-config-files for more information.",
                    stacklevel=2,
                )
        elif settings_path:
            if not os.path.exists(settings_path):
                raise InvalidSettingsPath(settings_path)

            settings_path = os.path.abspath(settings_path)
            project_root, config_settings = _find_config(settings_path)
        else:
            config_settings = {}
            project_root = os.getcwd()

        profile_name = config_overrides.get("profile", config_settings.get("profile", ""))
        profile: dict[str, Any] = {}
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
            # Collect all known sections beyond those that have direct entries
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
                        warn(
                            f"Can't set both {key} and {section_name} in the same config file.\n"
                            f"Default to {section_name} if unsure."
                            "\n\n"
                            "See: https://pycqa.github.io/isort/"
                            "#custom-sections-and-ordering.",
                            stacklevel=2,
                        )
                    else:
                        combined_config[section_name] = frozenset(value)
                else:
                    known_other[import_heading] = frozenset(value)
                    if maps_to_section not in combined_config.get("sections", ()) and not quiet:
                        warn(
                            f"`{key}` setting is defined, but {maps_to_section} is not"
                            " included in `sections` config option:"
                            f" {combined_config.get('sections', SECTION_DEFAULTS)}.\n\n"
                            "See: https://pycqa.github.io/isort/"
                            "#custom-sections-and-ordering.",
                            stacklevel=2,
                        )
            if key.startswith(IMPORT_HEADING_PREFIX):
                import_headings[key[len(IMPORT_HEADING_PREFIX) :].lower()] = str(value)
            if key.startswith(IMPORT_FOOTER_PREFIX):
                import_footers[key[len(IMPORT_FOOTER_PREFIX) :].lower()] = str(value)

            # Coerce all provided config values into their correct type
            default_value = _DEFAULT_SETTINGS.get(key, None)
            if default_value is None:
                continue

            combined_config[key] = type(default_value)(value)

        for section in combined_config.get("sections", ()):
            if section in SECTION_DEFAULTS:
                continue

            if section.lower() not in known_other:
                config_keys = ", ".join(known_other.keys())
                warn(
                    f"`sections` setting includes {section}, but no known_{section.lower()} "
                    "is defined. "
                    f"The following known_SECTION config options are defined: {config_keys}.",
                    stacklevel=2,
                )

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

        # Remove any config values that are used for creating config object but
        # aren't defined in dataclass
        combined_config.pop("source", None)
        combined_config.pop("sources", None)
        combined_config.pop("runtime_src_paths", None)

        deprecated_options_used = [
            option for option in combined_config if option in DEPRECATED_SETTINGS
        ]
        if deprecated_options_used:
            for deprecated_option in deprecated_options_used:
                combined_config.pop(deprecated_option)
            if not quiet:
                warn(
                    "W0503: Deprecated config options were used: "
                    f"{', '.join(deprecated_options_used)}."
                    "Please see the 5.0.0 upgrade guide: "
                    "https://pycqa.github.io/isort/docs/upgrade_guides/5.0.0.html",
                    stacklevel=2,
                )

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
        for option in set(combined_config.keys()).difference(
            getattr(_Config, "__dataclass_fields__", {}).keys()
        ):
            for source in reversed(sources):
                if option in source:
                    unsupported_config_errors[option] = {
                        "value": source[option],
                        "source": source["source"],
                    }
        if unsupported_config_errors:
            raise UnsupportedSettings(unsupported_config_errors)

        super().__init__(sources=tuple(sources), **combined_config)

    def is_supported_filetype(self, file_name: str) -> bool:
        _root, ext = os.path.splitext(file_name)
        ext = ext.lstrip(".")
        if ext in self.supported_extensions:
            return True
        if ext in self.blocked_extensions:
            return False

        # Skip editor backup files.
        if file_name.endswith("~"):
            return False

        try:
            if stat.S_ISFIFO(os.stat(file_name).st_mode):
                return False
        except OSError:
            pass

        try:
            with open(file_name, "rb") as fp:
                line = fp.readline(100)
        except OSError:
            return False
        return bool(_SHEBANG_RE.match(line))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_settings_Config_is_supported_filetype_0_test_valid_input
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:8:0: E0611: No name 'entry_points' in module 'isort.profiles' (no-name-in-module)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:59:16: E0602: Undefined variable '_Config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:92:30: E0602: Undefined variable '_get_config_data' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:111:44: E0602: Undefined variable '_find_config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:162:38: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:163:44: E0602: Undefined variable 'KNOWN_SECTION_MAPPING' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:276:20: E0602: Undefined variable '_Config' (undefined-variable)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:292:18: E1101: Instance of 'Config' has no 'supported_extensions' member (no-member)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:294:18: E1101: Instance of 'Config' has no 'blocked_extensions' member (no-member)
isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_input.py:312:20: E0602: Undefined variable '_SHEBANG_RE' (undefined-variable)


"""