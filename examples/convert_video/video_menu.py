# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "windows_context_menus",
# ]
#
# [tool.uv.sources]
# windows_context_menus = { path = "../../" }
# ///
from resolution_menu import resolution_menu
from speed_menu import speed_menu
from volume_menu import volume_menu

from windows_context_menus import Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

menu = ContextMenu(
    display_text="Convert mp4...",
    icon="wmploc.dll,-610",
    condition=Condition.model_validate(
        {"extension": {"eq": ".mp4"}},
    ),
    submenus=[speed_menu, resolution_menu, volume_menu],
)

if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ],
    )
