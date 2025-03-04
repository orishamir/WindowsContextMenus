# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

``` mermaid
---
title: Animal example
---
classDiagram
    ContextMenu *-- IFeature : Includes
    class ContextMenu{
        +name: str
        +features: list[IFeature]
        +submenus: list[ContextMenu] | None = None
        +build() -> RegistryKey
        +export_reg(location: ContextMenuLocation) -> list[str]
    }
    class IFeature{
        <<interface>>
        +apply_to(tree: RegistryKey) -> None
    }
```

## nah
::: context_menu_toolkit.context_menu_locations
    options:
        show_if_no_docstring: true

