"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.features import DisplayText, Command, Icon
from context_menu_toolkit.registry_interaction import apply_context_menu

MUTE_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -c:v copy -an "%V"-no_audio.mp4'
DOUBLE_VOLUME_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -c:v copy -af "volume=2.0" "%1"-double_volume.mp4'

volume_submenus = [
    ContextMenu(
        "MuteAudio",
        [
            DisplayText("Mute Audio"),
            Command(MUTE_COMMAND),
            Icon("SndVol.exe,-111"),
        ],
    ),
    ContextMenu(
        "DoubleVolume",
        [
            DisplayText("Double the volume"),
            Command(DOUBLE_VOLUME_COMMAND),
            # Icon("SndVol.exe,-111"),
        ],
    ),
]


volume_menu = ContextMenu(
    "VolumeMenu",
    [
        DisplayText("Volume options..."),
        Icon("SndVol.exe,-101"),
    ],
    volume_submenus,
)

if __name__ == '__main__':
    apply_context_menu(
        volume_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
                MenuAccessScope.ALL_USERS,
            ),
        ]
    )
