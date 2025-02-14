"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_sdk.conditions import FileName, ExtensionType, FileSize
from context_menu_sdk.context_menu import ContextMenu
from context_menu_sdk.context_menu_locations import ContextMenuLocation
from context_menu_sdk.features import Command, ConditionFeature
from context_menu_sdk.features.mui_verb import MUIVerb
from context_menu_sdk.registry_interaction import apply_context_menu


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
