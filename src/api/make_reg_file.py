from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from src.api.menu_builder import build_menu_from_config
from src.api.models import ContextMenuConfig
from src.context_menu_locations import ContextMenuLocation

app = FastAPI()


@app.post("/make-reg-file")
def make_reg(context_menu_config: ContextMenuConfig) -> PlainTextResponse:
    print(context_menu_config)

    menu = build_menu_from_config(context_menu_config)
    print(menu)

    return PlainTextResponse(
        content="\n".join(menu.export_reg(ContextMenuLocation.ALL_FILES_ADMIN)),
    )
