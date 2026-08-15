from windows_context_menus import Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, MenuAccessScope, RegistryHandler

BASE_COMMAND = "cmd.exe /c start chrome google.com"

some_menu = ContextMenu(
    display_text="name of the thing",
    command=BASE_COMMAND,
    condition=Condition.model_validate(  # file is .mp4, does not start with "my"
        {
            "extension": {"eq": ".mp4"},  # also possible via MenuItemType.SPECIFIC_FILE_TYPE.format(".mp4")
            "not": {"file_name": {"startswith": "my"}},
            "file_size": {"lt": 30_000_000},
        },
    ),
    submenus=[],
)


if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        some_menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
                MenuAccessScope.ALL_USERS,
            ),
        ],
    )
