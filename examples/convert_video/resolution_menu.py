# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "windows_context_menus",
# ]
#
# [tool.uv.sources]
# windows_context_menus = { path = "../../" }
# ///

from enum import StrEnum

from examples.convert_video.volume_menu import WindowsIcon
from windows_context_menus import CommandPlaceholder, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler


class Resolution(StrEnum):
    HD = "720p"
    FHD = "1080p"
    QHD = "1440p"


class Encoding(StrEnum):
    AVC = "libx264"
    HEVC = "hevc"


BASE_COMMAND = (
    f'cmd.exe /c ffmpeg -i "{CommandPlaceholder.FIRST_SELECTED}" -vf "scale=-1:{{res}}" -c:v libx264 -preset fast -c:a copy {{output_name}}'
)

resolution_submenus: list[ContextMenu] = []

for resolution in (Resolution.HD, Resolution.FHD):
    resolution_submenus.append(
        ContextMenu(
            display_text=(f"Convert to {resolution}"),
            command=BASE_COMMAND.format(
                res=resolution.rstrip("p"),
                output_name=f'"%1"-{resolution}.mp4',
            ),
        ),
    )


resolution_menu = ContextMenu(
    display_text=("Convert resolution..."),
    icon=WindowsIcon.PICTURE_IN_PICTURE,
    submenus=resolution_submenus,
)

if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        resolution_menu,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ],
    )
