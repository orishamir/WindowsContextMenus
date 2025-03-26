"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
from enum import StrEnum

from context_menu_toolkit import ContextMenuBinding, MenuItemType, RegistryHandler, ContextMenu


class Resolution(StrEnum):
    HD = "720p"
    FHD = "1080p"
    QHD = "1440p"


class Encoding(StrEnum):
    AVC = "libx264"
    HEVC = "hevc"


BASE_COMMAND = 'cmd.exe /c ffmpeg -i "%1" -vf "scale=-1:{res}" -c:v libx264 -preset fast -c:a copy {output_name}'

resolution_submenus: list[ContextMenu] = []

for resolution in (Resolution.HD, Resolution.FHD):
    resolution_submenus.append(
        ContextMenu(
            display_text=(f"Convert to {resolution}"),
            command=BASE_COMMAND.format(
                    res=resolution.rstrip("p"),
                    output_name=f'"%1"-{resolution}.mp4',
                )
        )
    )


resolution_menu = ContextMenu(
    display_text=("Convert resolution..."),
    icon="wmploc.dll,-1503",
    submenus=resolution_submenus,
)

if __name__ == '__main__':
    RegistryHandler().apply_context_menu(
        resolution_menu,
        bindings=[
            ContextMenuBinding(
                MenuItemType.ALL_FILES,
            ),
        ]
    )
