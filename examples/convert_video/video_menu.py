from examples.convert_video.resolution_menu import resolution_menu
from examples.convert_video.speed_menu import speed_menu
from src.conditions import ExtensionType
from src.context_menu import ContextMenu
from src.context_menu_locations import ContextMenuLocation
from src.features import EntryName, Icon, Condition
from src.registry_interaction import apply_context_menu

main = ContextMenu(
    "ConvertVideo",
    [
        EntryName("Convert mp4..."),
        Icon(r"C:\Users\ori\Pictures\arrow.ico"),
        Condition(
            (ExtensionType == ".mp4")
        )
    ],
    submenus=[speed_menu, resolution_menu]
)

if __name__ == '__main__':
    print(
        apply_context_menu(
            main,
            ContextMenuLocation.ALL_FILES_ADMIN,
        )
    )
