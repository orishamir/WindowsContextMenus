# Windows Context Menus

Create native Windows Explorer context menus declaratively in Python

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
#     "windows_context_menus",
# ]
#
# [tool.uv.sources]
# windows_context_menus = { git = "https://github.com/orishamir/WindowsContextMenus", tag = "0.1.3" }
# ///
"""Adds a context menu for converting images from and to formats."""

from windows_context_menus import CommandPlaceholder, Condition, ContextMenu, ContextMenuBinding, ExplorerItemType, RegistryHandler

CONVERT_IMAGE_COMMAND = f'cmd.exe /c magick "{CommandPlaceholder.FIRST_SELECTED}" "{CommandPlaceholder.FIRST_SELECTED}".{{}}'

convert_to_png_entry = ContextMenu(
    display_text="Convert to PNG",
    command=CONVERT_IMAGE_COMMAND.format("png"),
    condition=Condition.model_validate({"extension": {"ne": ".png"}}),
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
![convert_image.png](https://orishamir.github.io/WindowsContextMenus/convert_image.png)

For a more complicated example, see [Documentation](https://orishamir.github.io/WindowsContextMenus/)
