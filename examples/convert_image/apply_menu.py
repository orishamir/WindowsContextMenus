# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "context-menu-toolkit",
# ]
#
# [tool.uv.sources]
# context-menu-toolkit = { path = "../../" }
# ///
"""Adds a context menu for converting images from and to formats."""

from context_menu_toolkit import CommandPlaceholder, Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

CONVERT_IMAGE_COMMAND = f'cmd.exe /c magick "{CommandPlaceholder.FIRST_SELECTED}" "{CommandPlaceholder.FIRST_SELECTED}".{{}}'

convert_to_png_entry = ContextMenu(
    display_text="Convert to PNG",
    command=CONVERT_IMAGE_COMMAND.format("png"),
    condition=Condition.model_validate(
        {"extension": {"ne": ".png"}},
    ),
)

convert_to_jpeg_entry = ContextMenu(
    display_text=("Convert to JPEG"),
    command=CONVERT_IMAGE_COMMAND.format("jpeg"),
    condition=Condition.model_validate({"extension": {"ne": ".jpeg"}}),
)

convert_to_ico_entry = ContextMenu(
    display_text=("Convert to ICO"),
    command=CONVERT_IMAGE_COMMAND.format("ico"),
    condition=Condition.model_validate({"extension": {"ne": ".ico"}}),
)

convert_to_bmp_entry = ContextMenu(
    display_text=("Convert to BMP"),
    command=CONVERT_IMAGE_COMMAND.format("bmp"),
    condition=Condition.model_validate({"extension": {"ne": ".bmp"}}),
)

main: ContextMenu = ContextMenu(
    display_text=("Convert to..."),
    selection_limit=1,  # This menu supports only 1 file at a time.
    condition=Condition.model_validate(
        {
            "extension": {
                "in": [
                    ".png",
                    ".jpeg",
                    ".jpg",
                    ".bmp",
                    ".ico",
                    ".webp",
                    ".avif",
                    ".jfif",
                ],
            },
        },
    ),
    submenus=[convert_to_png_entry, convert_to_ico_entry, convert_to_jpeg_entry, convert_to_bmp_entry],
)

if __name__ == "__main__":
    RegistryHandler().apply_context_menu(
        main,
        bindings=[
            ContextMenuBinding(
                ExplorerItemType.ALL_FILES,
            ),
        ],
    )
