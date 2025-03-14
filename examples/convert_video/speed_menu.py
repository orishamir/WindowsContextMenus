"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.features import DisplayText, Command
from context_menu_toolkit.features.separator import Separator
from context_menu_toolkit.registry_interaction import apply_context_menu

ONE_AND_HALF_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -filter:v "setpts=PTS/1.5" -filter:a "atempo=1.5" "%V"-1.5x.mp4'
FIVE_QUARTERS_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -filter:v "setpts=PTS/1.25" -filter:a "atempo=1.25" "%V"-1.25x.mp4'
THREE_QUARTERS_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -filter:v "setpts=PTS/0.75" -filter:a "atempo=0.75" "%V"-0.75x.mp4'
HALF_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -filter:v "setpts=PTS/0.5" -filter:a "atempo=0.5" "%V"-0.5x.mp4'
QUARTER_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -filter:v "setpts=PTS/0.25" -filter:a "atempo=0.5,atempo=0.5" "%V"-0.25x.mp4'

speed_submenus = [
    ContextMenu(
        "SpeedBy1.5x",
        [
            DisplayText("Speed up by 1.5x"),
            Command(ONE_AND_HALF_SPEED_COMMAND),
        ],
    ),
    ContextMenu(
        "SpeedBy1.25x",
        [
            DisplayText("Speed up by 1.25x"),
            Command(FIVE_QUARTERS_SPEED_COMMAND),
        ],
    ),
    ContextMenu(
        "SpeedBy0.75x",
        [
            DisplayText("Slow down by 0.75x"),
            Command(THREE_QUARTERS_SPEED_COMMAND),
        ],
    ),
    ContextMenu(
        "SpeedBy0.5x",
        [
            DisplayText("Slow down by 0.5x"),
            Command(HALF_SPEED_COMMAND),
        ],
    ),
    ContextMenu(
        "SpeedBy0.25x",
        [
            DisplayText("Slow down by 0.25x"),
            Command(QUARTER_SPEED_COMMAND),
        ]
    ),
]


speed_menu = ContextMenu(
    "ConvertSpeedMenu",
    [
        DisplayText("Change speed..."),
        # Icon(r"C:\Users\ori\Pictures\arrow.ico"),
    ],
    speed_submenus,
)

if __name__ == '__main__':
    apply_context_menu(
        speed_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
                MenuAccessScope.ALL_USERS,
            ),
        ]
    )
