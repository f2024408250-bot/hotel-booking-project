from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import save_booking

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/book", response_class=HTMLResponse)
async def book_room(
    request: Request,
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...),
    special_requests: str = Form("")
):
    save_booking(
        full_name=full_name,
        email=email,
        phone=phone,
        check_in=check_in,
        check_out=check_out,
        room_type=room_type,
        guests=guests,
        special_requests=special_requests
    )
    return templates.TemplateResponse(request, "index.html", {
        "success": True,
        "name": full_name
    })
