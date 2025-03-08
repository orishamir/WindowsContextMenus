from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs.registry_key import RegistryKey
from context_menu_toolkit.registry_structs.registry_value import DataType, RegistryValue

COMMAND_KEY_NAME = "command"
DEFAULT_VALUE = ""


@dataclass
class Command(IFeature):
    r"""Add a command that gets executed when clicking the context menu.

    TODO: Improve API here, allowing for easy path parameters.
          for example, there exists both %V and %1.
        %* - Replace with all parameters.
        %~ - Replace with all parameters starting with and following the second parameter.
        %0 or %1 - The first file parameter. For example "C:\Users\Eric\Desktop\New Text Document.txt".
                    Generally this should be in quotes and the applications command line parsing should
                    accept quotes to disambiguate files with spaces in the name and different command line
                    parameters (this is a security best practice and I believe mentioned in MSDN).
        %<n> (where <n> is 2-9) - Replace with the nth parameter.
        %s - Show command.
        %h - Hotkey value.
        %i - IDList stored in a shared memory handle is passed here.
        %l - Long file name form of the first parameter. Note that Win32/64 applications will be passed the
              long file name, whereas Win16 applications get the short file name. Specifying %l is preferred as
              it avoids the need to probe for the application type.
        %d - Desktop absolute parsing name of the first parameter (for items that don't have file system paths).
        %v - For verbs that are none implies all. If there is no parameter passed this is the working directory.
        %w - The working directory.

    Todo:
        Add examples

    References:
        https://gist.github.com/Prince-Mandor/c1db742bd2951989db84acfbc7b9562f?permalink_comment_id=1921453#gistcomment-1921453
        https://superuser.com/questions/136838/which-special-variables-are-available-when-writing-a-shell-command-for-a-context
    """
    executable: str
    """The full path to the executable to run."""
    arguments: list[ShellCommandPlaceholder | str] = field(default_factory=list)

    def apply_to(self, tree: RegistryKey) -> None:
        command = self._build_command_with_placeholders()

        tree.subkeys.append(
            RegistryKey(name=COMMAND_KEY_NAME, values=[
                RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=command),
            ]),
        )

    def _build_command_with_placeholders(self) -> str:
        if not self.arguments:
            return self.executable

        escaped_arguments: list[str] = [
            f'"{arg}"'
            for arg in self.arguments
        ]

        return f"{self.executable} {' '.join(escaped_arguments)}"


class ShellCommandPlaceholder(StrEnum):
    """Enum representing Windows shell command placeholders used in registry context menus.

    Notes:
        If you select multiple files/folders on right-click, each will be called separately.
        This effectively makes placeholders such as %2, %3, %~, etc. useless, and %* equivalent to %1.
        See https://stackoverflow.com/a/1822850/9100289
    """

    CURRENT_DIRECTORY = "%v"  # The working directory (if no parameter is passed)
    WORKING_DIRECTORY = "%w"  # The working directory
    # ALL_PARAMETERS = "%*"  # All selected files and directories DOES NOT WORK! .
    # ALL_AFTER_SECOND = "%~"  # All parameters starting from the second one
    FIRST_SELECTED = "%1"  # The first selected file or directory
    # SHOW_COMMAND = "%s"  # Show command
    LONG_FILE_NAME = "%l"  # Long file name form of the first parameter

    SECOND_SELECTED = "%2"  # The second selected file or directory
    THIRD_SELECTED = "%3"  # The third selected file or directory
    FOURTH_SELECTED = "%4"  # The fourth selected file or directory
    FIFTH_SELECTED = "%5"  # The fifth selected file or directory
    SIXTH_SELECTED = "%6"  # The sixth selected file or directory
    SEVENTH_SELECTED = "%7"  # The seventh selected file or directory
    EIGHTH_SELECTED = "%8"  # The eighth selected file or directory
    NINTH_SELECTED = "%9"  # The ninth selected file or directory
    HOTKEY = "%h"  # Hotkey value
    IDLIST_HANDLE = "%i"  # IDList stored in a shared memory handle
    DESKTOP_PARSING_NAME = "%d"  # Desktop absolute parsing name (for non-filesystem items)

