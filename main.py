"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from enum import StrEnum

from src.conditions import ExtensionType
from src.context_menu_locations import ContextMenuLocation
from src.registry_interaction import apply_context_menu
from src.context_menu import ContextMenu
from src.features import EntryName as EntryName1
from features import EntryName as EntryName2

print(EntryName1 == EntryName2)
