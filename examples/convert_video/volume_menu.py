"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit import ContextMenu, ContextMenuBinding, MenuItemType, RegistryHandler


MUTE_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -c:v copy -an "%V"-no_audio.mp4'
DOUBLE_VOLUME_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -c:v copy -af "volume=2.0" "%1"-double_volume.mp4'

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

if __name__ == '__main__':
    RegistryHandler().apply_context_menu(
        volume_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
            ),
        ]
    )
