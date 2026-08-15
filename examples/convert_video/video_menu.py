# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "context-menu-toolkit",
# ]
#
# [tool.uv.sources]
# context-menu-toolkit = { path = "../../" }
# ///
from context_menu_toolkit import Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

from .resolution_menu import resolution_menu
from .speed_menu import speed_menu
from .volume_menu import volume_menu

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
