# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "windows_context_menus",
# ]
#
# [tool.uv.sources]
# windows_context_menus = { path = "../../" }
# ///
from windows_context_menus import CommandPlaceholder, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler
from windows_context_menus.models.icons import WindowsIcon

MUTE_COMMAND = (
    f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" -c:v copy -an "{CommandPlaceholder.FIRST_SELECTED}"-no_audio.mp4'
)
DOUBLE_VOLUME_COMMAND = f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" -c:v copy -af "volume=2.0" "{CommandPlaceholder.FIRST_SELECTED}"-double_volume.mp4'

volume_submenus = [
    ContextMenu(
        display_text="Mute Audio",
        command=MUTE_COMMAND,
        icon=WindowsIcon.MUTE,
    ),
    ContextMenu(
        display_text="Double the volume",
        command=DOUBLE_VOLUME_COMMAND,
    ),
]


volume_menu = ContextMenu(
    display_text=("Volume options..."),
    icon=WindowsIcon.SPEAKER,
    submenus=volume_submenus,
)

if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        volume_menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ],
    )
