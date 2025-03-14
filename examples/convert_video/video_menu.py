from examples.convert_video.resolution_menu import resolution_menu
from examples.convert_video.speed_menu import speed_menu
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.features import DisplayText, Icon
from context_menu_toolkit.registry_interaction import apply_context_menu

main = ContextMenu(
    "ConvertVideo",
    [
        DisplayText("Convert mp4..."),
        Icon(r"C:\Users\ori\Pictures\arrow.ico"),
    ],
    submenus=[speed_menu, resolution_menu]
)

if __name__ == '__main__':
    apply_context_menu(
        main,
        bindings=[
            ContextMenuBinding(
                MenuItemType.SPECIFIC_FILE_TYPE.format(file_type=".mp4"),
                MenuAccessScope.ALL_USERS,
            ),
        ]
    )
