"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from context_menu_toolkit import ContextMenuBinding, MenuItemType, ContextMenu, RegistryHandler


ONE_AND_HALF_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -filter:v "setpts=PTS/1.5" -filter:a "atempo=1.5" "%1"-1.5x.mp4'
FIVE_QUARTERS_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -filter:v "setpts=PTS/1.25" -filter:a "atempo=1.25" "%1"-1.25x.mp4'
THREE_QUARTERS_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -filter:v "setpts=PTS/0.75" -filter:a "atempo=0.75" "%1"-0.75x.mp4'
HALF_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -filter:v "setpts=PTS/0.5" -filter:a "atempo=0.5" "%1"-0.5x.mp4'
QUARTER_SPEED_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -filter:v "setpts=PTS/0.25" -filter:a "atempo=0.5,atempo=0.5" "%1"-0.25x.mp4'

speed_submenus = [
    ContextMenu(
        display_text="Speed up by 1.5x",
        command=ONE_AND_HALF_SPEED_COMMAND,
    ),
    ContextMenu(
        display_text="Speed up by 1.25x",
        command=FIVE_QUARTERS_SPEED_COMMAND,
    ),
    ContextMenu(
        display_text="Slow down by 0.75x",
        command=THREE_QUARTERS_SPEED_COMMAND,
    ),
    ContextMenu(
        display_text="Slow down by 0.5x",
        command=HALF_SPEED_COMMAND,
    ),
    ContextMenu(
        display_text="Slow down by 0.25x",
        command=QUARTER_SPEED_COMMAND,
    ),
]


speed_menu = ContextMenu(
    display_text=("Change speed..."),
    icon=("wmploc.dll,-29608"),
    submenus=speed_submenus,
)

if __name__ == '__main__':
    RegistryHandler().apply_context_menu(
        speed_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
            ),
        ]
    )
