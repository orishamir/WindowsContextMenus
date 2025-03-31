"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit import ContextMenu, ContextMenuBinding, MenuAccessScope, MenuItemType, RegistryHandler, Condition

BASE_COMMAND = 'cmd.exe /c start chrome google.com'

some_menu = ContextMenu(
    display_text="name of the thing",
    command=BASE_COMMAND,
    condition=Condition.model_validate(  # file is .mp4, does not start with "my"
        {
            "extension": {"eq": ".mp4"},  # also possible via MenuItemType.SPECIFIC_FILE_TYPE.format(".mp4")
            "not": {"file_name": {"startswith": "my"}},
            "file_size": {"lt": 30_000_000}
        }
    ),
    submenus=[],
)


if __name__ == '__main__':
    RegistryHandler().apply_context_menu(
        some_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
                MenuAccessScope.ALL_USERS,
            ),
        ]
    )
