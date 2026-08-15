# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "context-menu-toolkit",
# ]
#
# [tool.uv.sources]
# context-menu-toolkit = { path = "../../" }
# ///
from context_menu_toolkit import CommandPlaceholder, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

MUTE_COMMAND = (
    f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" -c:v copy -an "{CommandPlaceholder.FIRST_SELECTED}"-no_audio.mp4'
)
DOUBLE_VOLUME_COMMAND = f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" -c:v copy -af "volume=2.0" "{CommandPlaceholder.FIRST_SELECTED}"-double_volume.mp4'

volume_submenus = [
    ContextMenu(
        display_text="Mute Audio",
        command=MUTE_COMMAND,
        icon="SndVol.exe,-111",
    ),
    ContextMenu(
        display_text="Double the volume",
        command=DOUBLE_VOLUME_COMMAND,
        # icon="SndVol.exe,-111",
    ),
]


volume_menu = ContextMenu(
    display_text=("Volume options..."),
    icon=("SndVol.exe,-101"),
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
