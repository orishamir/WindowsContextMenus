from examples.convert_video.resolution_menu import resolution_menu
from examples.convert_video.speed_menu import speed_menu
from context_menu_toolkit.conditions import ExtensionType
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_locations import ContextMenuLocation
from context_menu_toolkit.features import EntryName, Icon, ConditionFeature
from context_menu_toolkit.registry_interaction import apply_context_menu

main = ContextMenu(
    "ConvertVideo",
    [
        EntryName("Convert mp4..."),
        Icon(r"C:\Users\ori\Pictures\arrow.ico"),
        ConditionFeature(
            (ExtensionType == ".mp4")
        ),
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
    # print(
    #     "\n".join(
    #         main.export_reg(ContextMenuLocation.ALL_FILES_ADMIN),
    #     ),
    # )
