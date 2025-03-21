from __future__ import annotations

from typing import Literal

from pydantic import BaseModel

from context_menu_toolkit.features.icon import WindowsIcon


class ContextMenu(BaseModel):
    r"""Represents a context menu.

    Attributes:
        display_text: The text that should be displayed for the context menu on right-click.
            You can also use string localization, which tells Windows to look up a string resource from a DLL (or EXE) file.
            For example `MUIVerb=@shell32.dll,-8518` -> `"Send To"`
        command: Add a command that gets executed when clicking the context menu. Use CommandPlaceholder.
        icon: An icon that will be displayed for the context menu. Can be a windows dll/exe icon, or a path on the local machine for the icon.
        shift_click: Open context menu only when shift is pressed alongside right click.
        never_default: Prevents Windows from using this context-menu item when no default app is set for the file extension.
        no_working_directory: Don't use the clicked item's working directory path when opening the context menu item.
            Normally, Windows sets the working directory to the folder containing the file/folder/etc you clicked on.
            This can sometimes lead to unintended behavior if the program being launched makes assumptions about its working directory.
            By setting NoWorkingDirectory, Windows skips setting the working directory, and the program will inherit the default working directory (often C:\Windows\System32 or whatever the default is for the parent process).[^1]
        position: Determines the general position of the context menu.
            Warning: This feature will NOT necessarily set the position.
                The way Windows determines the location is complicated,
                and Position feature merely specifies the general preference.
                For example, it may move your context menu lower down the list, but not all the way.
        separator: Adds a line separator before or after the context menu. Only works with submenus. [^2]
        has_lua_shield: Display a User Account Control (UAC) shield.
            Note: You can also use an Icon.[^3]
        disabled: Make the context menu disabled.

    References:
        [^1]: <https://superuser.com/questions/703275/whats-the-meaning-of-noworkingdirectory-string-value-in-windows-registry>
        [^2]: <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-cascading-menus-with-the-extendedsubcommandskey-registry-entry>
        [^3]: <https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#getting-dynamic-behavior-for-static-verbs-by-using-advanced-query-syntax>
    """

    display_text: str
    command: str
    icon: WindowsIcon | str | None = None
    shift_click: bool = False
    never_default: bool = False
    no_working_directory: bool | None = None
    position: Literal["Top", "Bottom"] | None = None
    separator: Literal["Before", "After"] | None = None
    has_lua_shield: bool = False
    disabled: bool = False
    submenus: list[ContextMenu] = []
