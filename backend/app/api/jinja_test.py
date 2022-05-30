from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.deps.jinja import get_templates

router = APIRouter()


@router.get("/jinja_test", response_class=HTMLResponse)
async def jinja_test(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    return templates.TemplateResponse("jinja_test.html", {"request": request})
