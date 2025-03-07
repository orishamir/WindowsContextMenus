from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum

from context_menu_toolkit.registry_structs.registry_path import RegistryPath


@dataclass
class ContextMenuBinding:
    r"""Represents a binding for a context menu.

    Bindings determines the basic conditions for a context menu
    to appear when right-clicking items.

    For example binding a context menu to files/folders/drives mean that it displays when right-clicking them.

    Tip:
        For more advanced control of conditions see `Condition` feature, `ICondition`, and `conditions`.

    Example:
        ```python
        ContextMenuBinding(
            MenuAccessScope.ALL_USERS,
            MenuItemType.ALL_FILES,
        ).construct_registry_path()
        # HKEY_LOCAL_MACHINE\Software\Classes\*\shell

        ContextMenuBinding(
            MenuAccessScope.ALL_USERS,
            MenuItemType.DESKTOP_BACKGROUND,
        ).construct_registry_path()
        # HKEY_LOCAL_MACHINE\Software\Classes\DesktopBackground\shell

        ContextMenuBinding(
            MenuAccessScope.ALL_USERS,
            MenuItemType.SPECIFIC_FILE_TYPE.format(file_type="image"),
        ).construct_registry_path()
        # HKEY_LOCAL_MACHINE\Software\Classes\DesktopBackground\shell
        ```
    """
    access_scope: MenuAccessScope
    """Bind to current user or all users"""

    menu_item_type: str | MenuItemType
    """Determines which object type the context menu is relevant for.
    For example files/folders/drives/etc..
    Should be a string. See MenuItemType for options and descriptions.
    """

    def construct_registry_path(self) -> RegistryPath:
        """Compose the registry path that match the binding."""
        self._validate_parameters_provided()

        return RegistryPath(self.access_scope) / self.menu_item_type / "shell"

    def _validate_parameters_provided(self) -> None:
        """Validate that all parameters of the chosen item type are filled.

        Example:
            MenuItemType.SPECIFIC_FILE_TYPE requires the `file_type` parameter.
        """
        try:
            # raises KeyError if the string contains unsubstituted arguments.
            # Example: "some {name} string".format() -> raises KeyError: name.
            #          "some string".format() -> does not raise anything.
            self.menu_item_type.format()
        except KeyError as e:
            missing_parameter, *_ = e.args
            raise ValueError(f'item type parameter not provided: "{missing_parameter}"') from None


class MenuAccessScope(StrEnum):
    """The access scope of the context menu.

    Either all users or current user only.
    The enum's value indicates the base registry location of that scope.
    """
    ALL_USERS = r"HKEY_LOCAL_MACHINE\Software\Classes"
    CURRENT_USER = r"HKEY_CURRENT_USER\Software\Classes"
    # HKEY_CLASS_ROOT - https://stackoverflow.com/a/55118854 should not be written to.


class MenuItemType(StrEnum):
    """Possible types of context menu item types.

    Menu items are types of clickable items, such as files, folders, drives, shortcuts, desktop background, etc.
    Also known as `shell` items.

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
    """Affect right-clicking a shortcut (.lnk)."""
