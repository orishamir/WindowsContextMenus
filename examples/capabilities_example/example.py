"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit.conditions import FileName, ExtensionType, FileSize
from context_menu_toolkit.conditions.comparison_type import ComparisonType
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.features import Command, ConditionFeature
from context_menu_toolkit.features.mui_verb import MUIVerb
from context_menu_toolkit.registry_interaction import apply_context_menu


BASE_COMMAND = 'cmd.exe /c start chrome google.com'

some_menu = ContextMenu(
    "whatever",
    [
        MUIVerb("name of the thing"),
        ConditionFeature(  # file is .mp4, does not start with "my"
            ExtensionType(ComparisonType.EQUALS, ".mp4") &  # also possible via MenuItemType.SPECIFIC_FILE_TYPE.format(".mp4")
            ~FileName(ComparisonType.STARTS_WITH, "my") &
            FileSize(ComparisonType.LESS_THAN, "30MB")
        ),
        Command(BASE_COMMAND),
    ],
    [],
)


if __name__ == '__main__':
    apply_context_menu(
        some_menu,
        bindings=[
            ContextMenuBinding(MenuAccessScope.ALL_USERS, MenuItemType.ALL_FILES),
        ]
    )
