
from enum import StrEnum


class ExplorerItemType(StrEnum):
    """Possible types of explorer items.

    Explorer items are types of clickable items, such as files, folders, drives, shortcuts, desktop background, etc.
    Also known as `shell` items.

    Question:
        The difference between Directory and Folder is that Folders include special folders such as "This PC" folder.
        See [Directory vs. Folder](https://superuser.com/q/169457/), [CLSID List](https://www.autohotkey.com/docs/v1/misc/CLSID-List.htm)

    Tip:
        For more advanced control of conditions see `Condition` feature, `ICondition`, and `conditions`.
    """

    ALL_FILES = "*"
    """Affect right-clicking any file."""

    SPECIFIC_FILE_TYPE = r"SystemFileAssociations\{file_type}"
    r"""Affect right-clicking a specific file extension or extension class.

    Example:
        ```python
        ContextMenuLocation(
            MenuAccessScope.ALL_USERS,
            MenuItemType.SPECIFIC_FILE_TYPE.format(file_type=".mp4"),
        ).construct_registry_path()
        # HKEY_LOCAL_MACHINE\Software\Classes\SystemFileAssociations\.mp4\shell

        ContextMenuLocation(
            MenuAccessScope.ALL_USERS,
            MenuItemType.SPECIFIC_FILE_TYPE.format(file_type="image"),
        ).construct_registry_path()
        # HKEY_LOCAL_MACHINE\Software\Classes\SystemFileAssociations\image\shell
        ```
    """

    EXTENDED_FOLDERS = "Folder"
    """Affect right-clicking all folders, including special shell folders (e.g., Libraries, This PC, Control Panel)."""

    DIRECTORY_BACKGROUND = r"Directory\Background"
    """Affect right-clicking the background in explorer."""

    DRIVES = "Drive"
    """Affect right-clicking a drive."""

    DIRECTORIES = "Directory"
    """Affect right-clicking directories, not including special shell folders such as This PC/Libraries."""

    NETWORK_FOLDERS = "Network"
    """Affect right-clicking network folders."""

    DESKTOP_BACKGROUND = "DesktopBackground"
    """Affect right-clicking the desktop background."""

    SHORTCUTS = "lnkfile"
    """Affect right-clicking a shortcut (.lnk).

    Warning:
        If both SHORTCUTS and ALL_FILES (or SPECIFIC_FILE_TYPE with .lnk) handler exists, this may cause unexpected
        behavior. See `CommandPlaceholder`s documentation for more details.
    """
