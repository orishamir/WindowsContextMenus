from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.features.ifeature import IFeature
from context_menu_toolkit.registry_structs.registry_key import RegistryKey
from context_menu_toolkit.registry_structs.registry_value import DataType, RegistryValue

COMMAND_KEY_NAME = "command"
DEFAULT_VALUE = ""


@dataclass
class Command(IFeature):
    r"""Add a command that gets executed when clicking the context menu.

    Todo:
        Add examples

    References:
        https://gist.github.com/Prince-Mandor/c1db742bd2951989db84acfbc7b9562f?permalink_comment_id=1921453#gistcomment-1921453
        https://superuser.com/questions/136838/which-special-variables-are-available-when-writing-a-shell-command-for-a-context
    """
    command: str
    """The command to run, can contain CommandPlaceholders.

    Example:
        ```python
        # convert passed file to mp4
        Command(f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" "{CommandPlaceholder.FIRST_SELECTED}".mp4')
        # start command prompt in the working directory
        Command(f'cmd.exe /d /k "{CommandPlaceholder.WORKING_DIRECTORY}"')
        ```
    """

    def apply_to(self, tree: RegistryKey) -> None:
        tree.subkeys.append(
            RegistryKey(name=COMMAND_KEY_NAME, values=[
                RegistryValue(name=DEFAULT_VALUE, type=DataType.REG_SZ, data=self.command),
            ]),
        )


class CommandPlaceholder(StrEnum):
    r"""Enum representing Windows shell command placeholders used in registry context menus.

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

    Note:
        If you select multiple files/folders on right-click, each will be called separately.
        This effectively makes placeholders such as %2, %3, %~, etc. useless, and %* equivalent to %1.
        See https://stackoverflow.com/a/1822850/, https://superuser.com/a/473602/

    Note:
        The difference between Directory and Folder is that Folders include special folders.
        In the tables below, Folder refers to virtual folders only.
        See [Directory vs. Folder](https://superuser.com/q/169457/)
    """
    # ALL_PARAMETERS = "%*"  # All selected files and directories DOES NOT WORK!.
    # ALL_AFTER_SECOND = "%~"  # All parameters starting from the second one
    # SHOW_COMMAND = "%s"  # Show command

    FIRST_SELECTED = "%1"
    r"""The first selected item.

    Value depends on the item type being clicked:

    |   Item Type             |     Placeholder Value                           |    Example                                                      |
    | :---------------------- | :---------------------------------------------- | :------------------------------------------------------------   |
    |   File                  |   The file's path (resolved if its a shortcut)  | "C:\Windows\System32\cmd.exe"                                   |
    |   Directory             |   The directory's path                          | "C:\Windows\System32\"                                          |
    |   Folder                |   "::{CLSID}" of the special shell folder[^1]   | "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" - "This PC" folder   |
    |   Drive                 |   Drive letter + ":\"                           | "C:\"                                                           |
    |   Shortcut (Link File)  |   The path of the shortcut (.lnk)[^2]           | "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk" |
    |   Directory Background  |   Error
    |   Desktop Background    |   Error

    [^1]:
        CLSIDs identify special folders. See [CLSID List](https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm)
    [^2]:
        If the context menu appears under both File and Shortcut item types, the File takes precedence.
        This means that right-clicking the shortcut would result in the __resolved___ path.
    """

    CURRENT_DIRECTORY = "%v"  # The working directory (if no parameter is passed)
    WORKING_DIRECTORY = "%w"
    r"""The containing working directory.

    Value depends on the item type being clicked:

    |   Item Type             |  Placeholder Value            |    Example                                               |
    | :---------------------- | :---------------------------- | :------------------------------------------------------- |
    |   File                  |  The file's parent path       | "C:\Windows\System32\cmd.exe"                            |
    |   Directory             |  The directory's parent path  | "C:\Windows\System32\"                                   |
    |   Shortcut (Link File)  |  The shortcut's parent path   | "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\"  |
    |   Directory Background  |  The directory path           | "C:\Windows\System32\"                                   |
    |   Desktop Background    |  The desktop path             | "C:\Users\user\Desktop"                                  |
    |   Folder                |  Error
    |   Drive                 |  Error

    """

    LONG_FILE_NAME = "%l"  # Long file name form of the first parameter
    HOTKEY = "%h"  # Hotkey value
    IDLIST_HANDLE = "%i"
    r"""IDList stored in a shared memory handle.
    I have no idea
    """

    DESKTOP_PARSING_NAME = "%d"
    r"""Desktop absolute parsing name (for non-filesystem items).

    **Unknown the difference between this and %1.**

    Value depends on the item type being clicked:

    |   Item Type             |   Placeholder Value                               |    Example                                                      |
    | :---------------------- | :------------------------------------------------ | :------------------------------------------------------------   |
    |   File                  |   The file's path (unresolved if its a shortcut)  | "C:\Windows\System32\cmd.exe"                                   |
    |   Directory             |   The directory's path                            | "C:\Windows\System32\"                                          |
    |   Folder                |   "::{CLSID}" of the special shell folder[^1]     | "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}" - "This PC" folder   |
    |   Drive                 |   Drive letter + ":\"                             | "C:\"                                                           |
    |   Shortcut (Link File)  |   The path of the shortcut (.lnk)                 | "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk" |
    |   Directory Background  |   Error (crashes explorer.exe)
    |   Desktop Background    |   Error (crashes explorer.exe)

    [^1]:
        CLSIDs identify special folders. See [CLSID List](https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm)
    """

