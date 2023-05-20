"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from src.conditions import ExtensionType
from src.location import Location
from src.registry_interaction import apply_context_menu
from src.context_menu import ContextMenu
from src.features import Command, EntryName, Icon, ShiftClick, Condition

main: ContextMenu = ContextMenu(
    "SearchGoogle",
    [
        EntryName("Search in google"),
        Icon(r'C:\Program Files\Google\Chrome\Application\chrome.exe'),
        ShiftClick(),
        Command(r'"cmd.exe" /c start chrome www.google.com/search?q="%V"'),
        Condition(
            (ExtensionType != ".exe") & (ExtensionType != ".dll") & (ExtensionType != ".pdf")
        )
    ]
)


if __name__ == '__main__':
    apply_context_menu(
        main,
        [
            Location.FILE_ADMIN
        ]
    )
