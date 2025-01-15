"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from src.conditions import FileName, ExtensionType, FileSize
from src.context_menu import ContextMenu
from src.context_menu_locations import ContextMenuLocation
from src.features import Command, ConditionFeature
from src.features.mui_verb import MUIVerb
from src.registry_interaction import apply_context_menu


BASE_COMMAND = 'cmd.exe /c start chrome google.com'

some_menu = ContextMenu(
    "whatever",
    [
        MUIVerb("name of the thing"),
        ConditionFeature(  # file is .mp4, does not start with "P"
            (ExtensionType == ".mp4") &
            ~FileName.startswith("P") &
            (FileSize < "30MB")
        ),
        Command(BASE_COMMAND),
    ],
    [],
)
if __name__ == '__main__':
    
    print(
        apply_context_menu(
            some_menu,
            ContextMenuLocation.ALL_FILES_ADMIN,
        )
    )
