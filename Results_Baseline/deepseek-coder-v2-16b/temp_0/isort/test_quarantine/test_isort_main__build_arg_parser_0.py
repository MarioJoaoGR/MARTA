
import pytest
import argparse
from isort import main as isort_main

def test_build_arg_parser():
    parser = isort_main._build_arg_parser()
    
    # Check if the parser is an instance of argparse.ArgumentParser
    assert isinstance(parser, argparse.ArgumentParser)
    
    # Check if the help argument exists and has the correct help message
    help_argument = parser.add_argument_group("general options").get_argument("-h")
    assert help_argument is not None
    assert help_argument.help == "show this help message and exit"
    
    # Check if the version argument exists and has the correct help message
    version_argument = parser.add_argument_group("general options").get_argument("-V")
    assert version_argument is not None
    assert version_argument.help == "Displays the currently installed version of isort."
    
    # Check if the verbose argument exists and has the correct help message
    verbose_argument = parser.add_argument_group("general options").get_argument("-v")
    assert verbose_argument is not None
    assert verbose_argument.help == "Shows verbose output, such as when files are skipped or when a check is successful."
    
    # Check if the quiet argument exists and has the correct help message
    quiet_argument = parser.add_argument_group("general options").get_argument("-q")
    assert quiet_argument is not None
    assert quiet_argument.help == "Shows extra quiet output, only errors are outputted."
    
    # Check if the check-only argument exists and has the correct help message
    check_only_argument = parser.add_argument_group("general options").get_argument("-c")
    assert check_only_argument is not None
    assert check_only_argument.help == "Checks the file for unsorted / unformatted imports and prints them to the command line without modifying the file. Returns 0 when nothing would change and returns 1 when the file would be reformatted."
    
    # Check if the files argument exists and has the correct help message
    files_argument = parser.add_argument("files", nargs="*", help="One or more Python source files that need their imports sorted.")
    assert files_argument is not None
    assert files_argument.help == "One or more Python source files that need their imports sorted."
    
    # Check if the filter-files argument exists and has the correct help message
    filter_files_argument = parser.add_argument("--filter-files", dest="filter_files", action="store_true", help="Tells isort to filter files even when they are explicitly passed in as part of the CLI command.")
    assert filter_files_argument is not None
    assert filter_files_argument.help == "Tells isort to filter files even when they are explicitly passed in as part of the CLI command."
    
    # Check if the skip argument exists and has the correct help message
    skip_argument = parser.add_argument("-s", "--skip", action="append", help="Files that isort should skip over. You can specify multiple times for multiple files/directories.")
    assert skip_argument is not None
    assert skip_argument.help == "Files that isort should skip over. You can specify multiple times for multiple files/directories."
    
    # Check if the extend-skip argument exists and has the correct help message
    extend_skip_argument = parser.add_argument("--extend-skip", action="append", help="Extends --skip to add additional files that isort should skip over.")
    assert extend_skip_argument is not None
    assert extend_skip_argument.help == "Extends --skip to add additional files that isort should skip over."
    
    # Check if the skip-glob argument exists and has the correct help message
    skip_glob_argument = parser.add_argument("--sg", "--skip-glob", action="append", help="Files that isort should skip over.")
    assert skip_glob_argument is not None
    assert skip_glob_argument.help == "Files that isort should skip over."
    
    # Check if the extend-skip-glob argument exists and has the correct help message
    extend_skip_glob_argument = parser.add_argument("--extend-skip-glob", action="append", help="Additional files that isort should skip over (extending --skip-glob).")
    assert extend_skip_glob_argument is not None
    assert extend_skip_glob_argument.help == "Additional files that isort should skip over (extending --skip-glob)."
    
    # Check if the gitignore argument exists and has the correct help message
    gitignore_argument = parser.add_argument("--gitignore", "--skip-gitignore", action="store_true", help="Treat project as a git repository and ignore files listed in .gitignore.")
    assert gitignore_argument is not None
    assert gitignore_argument.help == "Treat project as a git repository and ignore files listed in .gitignore."
    
    # Check if the supported-extension argument exists and has the correct help message
    supported_extension_argument = parser.add_argument("--ext", "--extension", "--supported-extension", action="append", help="Specifies what extensions isort can be run against.")
    assert supported_extension_argument is not None
    assert supported_extension_argument.help == "Specifies what extensions isort can be run against."
    
    # Check if the blocked-extension argument exists and has the correct help message
    blocked_extension_argument = parser.add_argument("--blocked-extension", action="append", help="Specifies what extensions isort can never be run against.")
    assert blocked_extension_argument is not None
    assert blocked_extension_argument.help == "Specifies what extensions isort can never be run against."
    
    # Check if the dont-follow-links argument exists and has the correct help message
    dont_follow_links_argument = parser.add_argument("--dont-follow-links", dest="dont_follow_links", action="store_true", help="Tells isort not to follow symlinks that are encountered when running recursively.")
    assert dont_follow_links_argument is not None
    assert dont_follow_links_argument.help == "Tells isort not to follow symlinks that are encountered when running recursively."
    
    # Check if the filename argument exists and has the correct help message
    filename_argument = parser.add_argument("--filename", dest="filename", help="Provide the filename associated with a stream.")
    assert filename_argument is not None
    assert filename_argument.help == "Provide the filename associated with a stream."
    
    # Check if the allow-root argument exists and has the correct help message
    allow_root_argument = parser.add_argument("--allow-root", action="store_true", default=False, help="Tells isort not to treat / specially, allowing it to be run against the root dir.")
    assert allow_root_argument is not None
    assert allow_root_argument.help == "Tells isort not to treat / specially, allowing it to be run against the root dir."
    
    # Check if the add-import argument exists and has the correct help message
    add_import_argument = parser.add_argument("-a", "--add-import", action="append", help="Adds the specified import line to all files, automatically determining correct placement.")
    assert add_import_argument is not None
    assert add_import_argument.help == "Adds the specified import line to all files, automatically determining correct placement."
    
    # Check if the append-only argument exists and has the correct help message
    append_only_argument = parser.add_argument("--append", "--append-only", dest="append_only", action="store_true", help="Only adds the imports specified in --add-import if the file contains existing imports.")
    assert append_only_argument is not None
    assert append_only_argument.help == "Only adds the imports specified in --add-import if the file contains existing imports."
    
    # Check if the force-adds argument exists and has the correct help message
    force_adds_argument = parser.add_argument("--af", "--force-adds", dest="force_adds", action="store_true", help="Forces import adds even if the original file is empty.")
    assert force_adds_argument is not None
    assert force_adds_argument.help == "Forces import adds even if the original file is empty."
    
    # Check if the remove-import argument exists and has the correct help message
    remove_import_argument = parser.add_argument("--rm", "--remove-import", action="append", help="Removes the specified import from all files.")
    assert remove_import_argument is not None
    assert remove_import_argument.help == "Removes the specified import from all files."
    
    # Check if the float-to-top argument exists and has the correct help message
    float_to_top_argument = parser.add_argument("--float-to-top", dest="float_to_top", action="store_true", help="Causes all non-indented imports to float to the top of the file having its imports sorted (immediately below the top of file comment).")
    assert float_to_top_argument is not None
    assert float_to_top_argument.help == "Causes all non-indented imports to float to the top of the file having its imports sorted (immediately below the top of file comment)."
    
    # Check if the dont-float-to-top argument exists and has the correct help message
    dont_float_to_top_argument = parser.add_argument("--dont-float-to-top", dest="dont_float_to_top", action="store_true", help="Forces --float-to-top setting off.")
    assert dont_float_to_top_argument is not None
    assert dont_float_to_top_argument.help == "Forces --float-to-top setting off."
    
    # Check if the combine-as argument exists and has the correct help message
    combine_as_argument = parser.add_argument("--ca", "--combine-as", dest="combine_as_imports", action="store_true", help="Combines as imports on the same line.")
    assert combine_as_argument is not None
    assert combine_as_argument.help == "Combines as imports on the same line."
    
    # Check if the combine-star argument exists and has the correct help message
    combine_star_argument = parser.add_argument("--cs", "--combine-star", dest="combine_star", action="store_true", help="Ensures that if a star import is present, nothing else is imported from that namespace.")
    assert combine_star_argument is not None
    assert combine_star_argument.help == "Ensures that if a star import is present, nothing else is imported from that namespace."
    
    # Check if the balanced argument exists and has the correct help message
    balanced_argument = parser.add_argument("--balanced", dest="balanced_wrapping", action="store_true", help="Balances wrapping to produce the most consistent line length possible")
    assert balanced_argument is not None
    assert balanced_argument.help == "Balances wrapping to produce the most consistent line length possible"
    
    # Check if the from-first argument exists and has the correct help message
    from_first_argument = parser.add_argument("--ff", "--from-first", dest="from_first", action="store_true", help="Switches the typical ordering preference, showing from imports first then straight ones.")
    assert from_first_argument is not None
    assert from_first_argument.help == "Switches the typical ordering preference, showing from imports first then straight ones."
    
    # Check if the force-grid-wrap argument exists and has the correct help message
    force_grid_wrap_argument = parser.add_argument("--fgw", "--force-grid-wrap", nargs="?", const=2, type=int, dest="force_grid_wrap", help="Force number of from imports (defaults to 2 when passed as CLI flag without value) to be grid wrapped regardless of line length.")
    assert force_grid_wrap_argument is not None
    assert force_grid_wrap_argument.help == "Force number of from imports (defaults to 2 when passed as CLI flag without value) to be grid wrapped regardless of line length."
    
    # Check if the indent argument exists and has the correct help message
    indent_argument = parser.add_argument("--indent", type=str, help='String to place for indents defaults to "    " (4 spaces).')
    assert indent_argument is not None
    assert indent_argument.help == 'String to place for indents defaults to "    " (4 spaces).'
    
    # Check if the lines-before-imports argument exists and has the correct help message
    lines_before_imports_argument = parser.add_argument("--lbi", "--lines-before-imports", type=int)
    assert lines_before_imports_argument is not None
    
    # Check if the lines-after-imports argument exists and has the correct help message
    lines_after_imports_argument = parser.add_argument("--lai", "--lines-after-imports", type=int)
    assert lines_after_imports_argument is not None
    
    # Check if the multi-line argument exists and has the correct help message
    multi_line_argument = parser.add_argument("-m", "--multi-line", choices=list(WrapModes.__members__.keys()) + [str(mode.value) for mode in WrapModes.__members__.values()], type=str, help="Multi line output (0-grid, 1-vertical, 2-hanging, 3-vert-hanging, 4-vert-grid, 5-vert-grid-grouped, 6-deprecated-alias-for-5, 7-noqa, 8-vertical-hanging-indent-bracket, 9-vertical-prefix-from-module-import, 10-hanging-indent-with-parentheses).")
    assert multi_line_argument is not None
    assert multi_line_argument.help == "Multi line output (0-grid, 1-vertical, 2-hanging, 3-vert-hanging, 4-vert-grid, 5-vert-grid-grouped, 6-deprecated-alias-for-5, 7-noqa, 8-vertical-hanging-indent-bracket, 9-vertical-prefix-from-module-import, 10-hanging-indent-with-parentheses)."
    
    # Check if the ensure-newline-before-comments argument exists and has the correct help message
    ensure_newline_before_comments_argument = parser.add_argument("--ensure-newline-before-comments", dest="ensure_newline_before_comments", action="store_true", help="Inserts a blank line before a comment following an import.")
    assert ensure_newline_before_comments_argument is not None
    assert ensure_newline_before_comments_argument.help == "Inserts a blank line before a comment following an import."
    
    # Check if the no-inline-sort argument exists and has the correct help message
    no_inline_sort_argument = parser.add_argument("--nis", "--no-inline-sort", dest="no_inline_sort", action="store_true", help="Leaves `from` imports with multiple imports 'as-is' (e.g. `from foo import a, c ,b`).")
    assert no_inline_sort_argument is not None
    assert no_inline_sort_argument.help == "Leaves `from` imports with multiple imports 'as-is' (e.g. `from foo import a, c ,b`)."
    
    # Check if the order-by-type argument exists and has the correct help message
    order_by_type_argument = parser.add_argument("--ot", "--order-by-type", dest="order_by_type", action="store_true", help="Order imports by type, which is determined by case, in addition to alphabetically.")
    assert order_by_type_argument is not None
    assert order_by_type_argument.help == "Order imports by type, which is determined by case, in addition to alphabetically."
    
    # Check if the dont-order-by-type argument exists and has the correct help message
    dont_order_by_type_argument = parser.add_argument("--dt", "--dont-order-by-type", dest="dont_order_by_type", action="store_true", help="Don't order imports by type, which is determined by case, in addition to alphabetically.")
    assert dont_order_by_type_argument is not None
    assert dont_order_by_type_argument.help == "Don't order imports by type, which is determined by case, in addition to alphabetically."
    
    # Check if the reverse-relative argument exists and has the correct help message
    reverse_relative_argument = parser.add_argument("--rr", "--reverse-relative", dest="reverse_relative", action="store_true", help="Reverse order of relative imports.")
    assert reverse_relative_argument is not None
    assert reverse_relative_argument.help == "Reverse order of relative imports."
    
    # Check if the reverse-sort argument exists and has the correct help message
    reverse_sort_argument = parser.add_argument("--reverse-sort", dest="reverse_sort", action="store_true", help="Reverses the ordering of imports.")
    assert reverse_sort_argument is not None
    assert reverse_sort_argument.help == "Reverses the ordering of imports."
    
    # Check if the force-single-line-imports argument exists and has the correct help message
    force_single_line_imports_argument = parser.add_argument("--sl", "--force-single-line-imports", dest="force_single_line", action="store_true", help="Forces all from imports to appear on their own line")
    assert force_single_line_imports_argument is not None
    assert force_single_line_imports_argument.help == "Forces all from imports to appear on their own line"
    
    # Check if the single-line-exclusions argument exists and has the correct help message
    single_line_exclusions_argument = parser.add_argument("--nsl", "--single-line-exclusions", action="append", help="One or more modules to exclude from the single line rule.")
    assert single_line_exclusions_argument is not None
    assert single_line_exclusions_argument.help == "One or more modules to exclude from the single line rule."
    
    # Check if the trailing-comma argument exists and has the correct help message
    trailing_comma_argument = parser.add_argument("--tc", "--trailing-comma", dest="include_trailing_comma", action="store_true", help="Includes a trailing comma on multi line imports that include parentheses.")
    assert trailing_comma_argument is not None
    assert trailing_comma_argument.help == "Includes a trailing comma on multi line imports that include parentheses."
    
    # Check if the use-parentheses argument exists and has the correct help message
    use_parentheses_argument = parser.add_argument("--up", "--use-parentheses", dest="use_parentheses", action="store_true", help="Use parentheses for line continuation on length limit instead of slashes.")
    assert use_parentheses_argument is not None
    assert use_parentheses_argument.help == "Use parentheses for line continuation on length limit instead of slashes."
    
    # Check if the line-length argument exists and has the correct help message
    line_length_argument = parser.add_argument("-l", "-w", "--line-length", "--line-width", type=int, help="The max length of an import line (used for wrapping long imports).")
    assert line_length_argument is not None
    assert line_length_argument.help == "The max length of an import line (used for wrapping long imports)."
    
    # Check if the wrap-length argument exists and has the correct help message
    wrap_length_argument = parser.add_argument("--wl", "--wrap-length", type=int, help="Specifies how long lines that are wrapped should be, if not set line_length is used.")
    assert wrap_length_argument is not None
    assert wrap_length_argument.help == "Specifies how long lines that are wrapped should be, if not set line_length is used."
    
    # Check if the case-sensitive argument exists and has the correct help message
    case_sensitive_argument = parser.add_argument("--case-sensitive", dest="case_sensitive", action="store_true", help="Tells isort to include casing when sorting module names")
    assert case_sensitive_argument is not None
    assert case_sensitive_argument.help == "Tells isort to include casing when sorting module names"
    
    # Check if the remove-redundant-aliases argument exists and has the correct help message
    remove_redundant_aliases_argument = parser.add_argument("--remove-redundant-aliases", dest="remove_redundant_aliases", action="store_true", help="Tells isort to remove redundant aliases from imports, such as `import os as os`.")
    assert remove_redundant_aliases_argument is not None
    assert remove_redundant_aliases_argument.help == "Tells isort to remove redundant aliases from imports, such as `import os as os`."
    
    # Check if the honor-noqa argument exists and has the correct help message
    honor_noqa_argument = parser.add_argument("--honor-noqa", dest="honor_noqa", action="store_true", help="Tells isort to honor noqa comments to enforce skipping those comments.")
    assert honor_noqa_argument is not None
    assert honor_noqa_argument.help == "Tells isort to honor noqa comments to enforce skipping those comments."
    
    # Check if the treat-comment-as-code argument exists and has the correct help message
    treat_comment_as_code_argument = parser.add_argument("--treat-comment-as-code", action="append", help="Tells isort to treat the specified single line comment(s) as if they are code.")
    assert treat_comment_as_code_argument is not None
    assert treat_comment_as_code_argument.help == "Tells isort to treat the specified single line comment(s) as if they are code."
    
    # Check if the treat-all-comment-as-code argument exists and has the correct help message
    treat_all_comments_as_code_argument = parser.add_argument("--treat-all-comment-as-code", action="store_true", help="Tells isort to treat all single line comments as if they are code.")
    assert treat_all_comments_as_code_argument is not None
    assert treat_all_comments_as_code_argument.help == "Tells isort to treat all single line comments as if they are code."
    
    # Check if the formatter argument exists and has the correct help message
    formatter_argument = parser.add_argument("--formatter", type=str, help="Specifies the name of a formatting plugin to use when producing output.")
    assert formatter_argument is not None
    assert formatter_argument.help == "Specifies the name of a formatting plugin to use when producing output."
    
    # Check if the color argument exists and has the correct help message
    color_output_argument = parser.add_argument("--color", dest="color_output", action="store_true", help="Tells isort to use color in terminal output.")
    assert color_output_argument is not None
    assert color_output_argument.help == "Tells isort to use color in terminal output."
    
    # Check if the ext-format argument exists and has the correct help message
    ext_format_argument = parser.add_argument("--ext-format", dest="ext_format", help="Tells isort to format the given files according to an extensions formatting rules.")
    assert ext_format_argument is not None
    assert ext_format_argument.help == "Tells isort to format the given files according to an extensions formatting rules."
    
    # Check if the star-first argument exists and has the correct help message
    star_first_argument = parser.add_argument("--star-first", help="Forces star imports above others to avoid overriding directly imported variables.", dest="star_first", action="store_true")
    assert star_first_argument is not None
    assert star_first_argument.help == "Forces star imports above others to avoid overriding directly imported variables."
    
    # Check if the split-on-trailing-comma argument exists and has the correct help message
    split_on_trailing_comma_argument = parser.add_argument("--split-on-trailing-comma", action="store_true", help="Split imports list followed by a trailing comma into VERTICAL_HANGING_INDENT mode")
    assert split_on_trailing_comma_argument is not None
    assert split_on_trailing_comma_argument.help == "Split imports list followed by a trailing comma into VERTICAL_HANGING_INDENT mode"
    
    # Check if the default-section argument exists and has the correct help message
    default_section_argument = parser.add_argument("--sd", "--section-default", dest="default_section", help="Sets the default section for import options: " + str(sections.DEFAULT))
    assert default_section_argument is not None
    assert default_section_argument.help == "Sets the default section for import options: " + str(sections.DEFAULT)
    
    # Check if the only-sections argument exists and has the correct help message
    only_sections_argument = parser.add_argument("--only-sections", "--os", dest="only_sections", action="store_true", help="Causes imports to be sorted based on their sections like STDLIB, THIRDPARTY, etc. Within sections, the imports are ordered by their import style and the imports with the same style maintain their relative positions.")
    assert only_sections_argument is not None
    assert only_sections_argument.help == "Causes imports to be sorted based on their sections like STDLIB, THIRDPARTY, etc. Within sections, the imports are ordered by their import style and the imports with the same style maintain their relative positions."
    
    # Check if the no-sections argument exists and has the correct help message
    no_sections_argument = parser.add_argument("--ds", "--no-sections", dest="no_sections", action="store_true", help="Put all imports into the same section bucket")
    assert no_sections_argument is not None
    assert no_sections_argument.help == "Put all imports into the same section bucket"
    
    # Check if the force-alphabetical-sort argument exists and has the correct help message
    force_alphabetical_sort_argument = parser.add_argument("--fas", "--force-alphabetical-sort", action="store_true", dest="force_alphabetical_sort", help="Force all imports to be sorted as a single section")
    assert force_alphabetical_sort_argument is not None
    assert force_alphabetical_sort_argument.help == "Force all imports to be sorted as a single section"
    
    # Check if the force-sort-within-sections argument exists and has the correct help message
    force_sort_within_sections_argument = parser.add_argument("--fss", "--force-sort-within-sections", action="store_true", dest="force_sort_within_sections", help="Don't sort straight-style imports (like import sys) before from-style imports (like from itertools import groupby). Instead, sort the imports by module, independent of import style.")
    assert force_sort_within_sections_argument is not None
    assert force_sort_within_sections_argument.help == "Don't sort straight-style imports (like import sys) before from-style imports (like from itertools import groupby). Instead, sort the imports by module, independent of import style."
    
    # Check if the honor-case-in-force-sorted-sections argument exists and has the correct help message
    honor_case_in_force_sorted_sections_argument = parser.add_argument("--hcss", "--honor-case-in-force-sorted-sections", action="store_true", dest="honor_case_in_force_sorted_sections", help="Honor `--case-sensitive` when `--force-sort-within-sections` is being used.")
    assert honor_case_in_force_sorted_sections_argument is not None
    assert honor_case_in_force_sorted_sections_argument.help == "Honor `--case-sensitive` when `--force-sort-within-sections` is being used."
    
    # Check if the force-alphabetical-sort-within-sections argument exists and has the correct help message
    force_alphabetical_sort_within_sections_argument = parser.add_argument("--fass", "--force-alphabetical-sort-within-sections", action="store_true", dest="force_alphabetical_sort_within_sections", help="Force all imports to be sorted alphabetically within a section")
    assert force_alphabetical_sort_within_sections_argument is not None
    assert force_alphabetical_sort_within_sections_argument.help == "Force all imports to be sorted alphabetically within a section"
    
    # Check if the top argument exists and has the correct help message
    top_argument = parser.add_argument("-t", "--top", action="append", dest="force_to_top", help="Force specific imports to the top of their appropriate section.")
    assert top_argument is not None
    assert top_argument.help == "Force specific imports to the top of their appropriate section."
    
    # Check if the combine-straight-imports argument exists and has the correct help message
    combine_straight_imports_argument = parser.add_argument("--combine-straight-imports", "--csi", action="store_true", dest="combine_straight_imports", help="Combines all the bare straight imports of the same section in a single line. Won't work with sections which have 'as' imports.")
    assert combine_straight_imports_argument is not None
    assert combine_straight_imports_argument.help == "Combines all the bare straight imports of the same section in a single line. Won't work with sections which have 'as' imports."
    
    # Check if the no-lines-before argument exists and has the correct help message
    no_lines_before_argument = parser.add_argument("--nlb", "--no-lines-before", action="append", dest="no_lines_before", help="Sections which should not be split with previous by empty lines")
    assert no_lines_before_argument is not None
    assert no_lines_before_argument.help == "Sections which should not be split with previous by empty lines"
    
    # Check if the src-path argument exists and has the correct help message
    src_path_argument = parser.add_argument("--src", "--src-path", action="append", dest="src_paths", help="Add an explicitly defined source path (modules within src paths have their imports automatically categorized as first_party). Glob expansion (`*` and `**`) is supported for this option.")
    assert src_path_argument is not None
    assert src_path_argument.help == "Add an explicitly defined source path (modules within src paths have their imports automatically categorized as first_party). Glob expansion (`*` and `**`) is supported for this option."
    
    # Check if the builtin argument exists and has the correct help message
    builtin_argument = parser.add_argument("-b", "--builtin", action="append", dest="known_standard_library", help="Force isort to recognize a module as part of Python's standard library.")
    assert builtin_argument is not None
    assert builtin_argument.help == "Force isort to recognize a module as part of Python's standard library."
    
    # Check if the extra-builtin argument exists and has the correct help message
    extra_builtin_argument = parser.add_argument("--extra-builtin", action="append", dest="extra_standard_library", help="Extra modules to be included in the list of ones in Python's standard library.")
    assert extra_builtin_argument is not None
    assert extra_builtin_argument.help == "Extra modules to be included in the list of ones in Python's standard library."
    
    # Check if the future argument exists and has the correct help message
    future_argument = parser.add_argument("-f", "--future", action="append", dest="known_future_library", help="Force isort to recognize a module as part of Python's internal future compatibility libraries. WARNING: this overrides the behavior of __future__ handling and therefore can result in code that can't execute.")
    assert future_argument is not None
    assert future_argument.help == "Force isort to recognize a module as part of Python's internal future compatibility libraries. WARNING: this overrides the behavior of __future__ handling and therefore can result in code that can't execute."
    
    # Check if the thirdparty argument exists and has the correct help message
    thirdparty_argument = parser.add_argument("-o", "--thirdparty", action="append", dest="known_third_party", help="Force isort to recognize a module as being part of a third party library.")
    assert thirdparty_argument is not None
    assert thirdparty_argument.help == "Force isort to recognize a module as being part of a third party library."
    
    # Check if the project argument exists and has the correct help message
    project_argument = parser.add_argument("-p", "--project", action="append", dest="known_first_party", help="Force isort to recognize a module as being part of the current python project.")
    assert project_argument is not None
    assert project_argument.help == "Force isort to recognize a module as being part of the current python project."
    
    # Check if the known-local-folder argument exists and has the correct help message
    known_local_folder_argument = parser.add_argument("--known-local-folder", action="append", dest="known_local_folder", help="Force isort to recognize a module as being a local folder. Generally, this is reserved for relative imports (from . import module).")
    assert known_local_folder_argument is not None
    assert known_local_folder_argument.help == "Force isort to recognize a module as being a local folder. Generally, this is reserved for relative imports (from . import module)."
    
    # Check if the virtual-env argument exists and has the correct help message
    virtual_env_argument = parser.add_argument("--virtual-env", dest="virtual_env", help="Virtual environment to use for determining whether a package is third-party")
    assert virtual_env_argument is not None
    assert virtual_env_argument.help == "Virtual environment to use for determining whether a package is third-party"
    
    # Check if the conda-env argument exists and has the correct help message
    conda_env_argument = parser.add_argument("--conda-env", dest="conda_env", help="Conda environment to use for determining whether a package is third-party")
    assert conda_env_argument is not None
    assert conda_env_argument.help == "Conda environment to use for determining whether a package is third-party"
    
    # Check if the python-version argument exists and has the correct help message
    python_version_argument = parser.add_argument("--py", "--python-version", action="store", choices=(*tuple(VALID_PY_TARGETS), "auto"), help="Tells isort to set the known standard library based on the specified Python version.")
    assert python_version_argument is not None
    assert python_version_argument.help == "Tells isort to set the known standard library based on the specified Python version."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_main__build_arg_parser_0
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:13:20: E1101: Instance of '_ArgumentGroup' has no 'get_argument' member (no-member)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:18:23: E1101: Instance of '_ArgumentGroup' has no 'get_argument' member (no-member)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:23:23: E1101: Instance of '_ArgumentGroup' has no 'get_argument' member (no-member)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:28:21: E1101: Instance of '_ArgumentGroup' has no 'get_argument' member (no-member)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:33:26: E1101: Instance of '_ArgumentGroup' has no 'get_argument' member (no-member)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:166:81: E0602: Undefined variable 'WrapModes' (undefined-variable)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:166:142: E0602: Undefined variable 'WrapModes' (undefined-variable)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:281:163: E0602: Undefined variable 'sections' (undefined-variable)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:283:98: E0602: Undefined variable 'sections' (undefined-variable)
isort/Test4DT_tests/test_isort_main__build_arg_parser_0.py:376:110: E0602: Undefined variable 'VALID_PY_TARGETS' (undefined-variable)


"""