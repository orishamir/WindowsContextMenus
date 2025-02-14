"""
https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers

https://learn.microsoft.com/en-us/previous-versions//ff521735(v=vs.85)
"""
import uvicorn

from src.api.make_reg_file import app

uvicorn.run(
    app=app,
)
