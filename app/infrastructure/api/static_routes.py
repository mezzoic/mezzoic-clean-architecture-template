from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

app = APIRouter()

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(os.path.join("app", "static", "favicon.ico"))