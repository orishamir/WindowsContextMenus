# ContextMenus

Easily add context menus to right-click in windows.

## Quick example

Its common to download an image file, just for it to be some `.jfif` nonsense.
Or maybe you have some `.jpg` but you need a `.ico` for uploading icons?
And now you need to upload them to some thirdparty site that converts it to `.jpg` or `.ico` for you.
What if you could do that natively from your Windows Explorer?

Provided [imagemagick](https://imagemagick.org/download/) is installed:

```python3
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

from context_menu_toolkit import Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

CONVERT_IMAGE_COMMAND = 'cmd.exe /c magick "%V" "%V".{}'

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
```

Produces:  
![convert_image.png](docs/convert_image.png)

Note that I currently do not publish this package to PyPi.

For a more complicated example, see [Documentation](https://orishamir.github.io/WindowsContextMenus/)
