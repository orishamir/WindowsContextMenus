from examples.convert_video.resolution_menu import resolution_menu
from examples.convert_video.speed_menu import speed_menu
from examples.convert_video.volume_menu import volume_menu
from context_menu_toolkit import ContextMenu, Condition, ContextMenuBinding, ExplorerItemType, RegistryHandler

menu = ContextMenu(
    display_text="Convert mp4...",
    icon="wmploc.dll,-610",
    condition=Condition.model_validate(
        {"extension": {"eq": ".mp4"}},
    ),
    submenus=[speed_menu, resolution_menu, volume_menu]
)

if __name__ == '__main__':
    RegistryHandler().apply_context_menu(
        menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ]
    )
    # print("\n".join(RegistryHandler().export_reg_file(menu, bindings=[ContextMenuBinding(ExplorerItemType.ALL_FILES)])))
