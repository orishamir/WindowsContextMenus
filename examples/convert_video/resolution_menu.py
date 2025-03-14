"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from enum import StrEnum

from context_menu_toolkit.context_menu import ContextMenu
from context_menu_toolkit.context_menu_bindings import ContextMenuBinding, MenuAccessScope, MenuItemType
from context_menu_toolkit.features import DisplayText, Command, Icon
from context_menu_toolkit.registry_interaction import apply_context_menu


class Resolution(StrEnum):
    HD = "720p"
    FHD = "1080p"
    QHD = "1440p"


class Encoding(StrEnum):
    AVC = "libx264"
    HEVC = "hevc"


BASE_COMMAND = 'cmd.exe /c ffmpeg -i "%V" -vf "scale=-1:{res}" -c:v libx264 -preset fast -c:a copy {output_name}'

resolution_submenus = []

for resolution in (Resolution.HD, Resolution.FHD):
    resolution_submenus.append(
        ContextMenu(
            f"ConvertTo{resolution}",
            [
                DisplayText(f"Convert to {resolution}"),
                Command(
                    BASE_COMMAND.format(
                        res=resolution.rstrip("p"),
                        output_name=f'"%V"-{resolution}.mp4',
                    )
                ),
            ]
        )
    )


resolution_menu = ContextMenu(
    "ConvertResolutionMenu",
    [
        DisplayText("Convert resolution..."),
        Icon(r"C:\Users\ori\Pictures\arrow.ico"),
    ],
    resolution_submenus,
)

if __name__ == '__main__':
    apply_context_menu(
        resolution_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
                MenuAccessScope.ALL_USERS,
            ),
        ]
    )
