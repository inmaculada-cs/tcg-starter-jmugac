from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


cards = [{"nombre": "David Coaguila"}, {"nombre": "Victor Garro"}]

# Esta es la vista a editar
# el id empieza en 0
@app.get("/card/{id}", response_class=HTMLResponse)
async def card(request: Request, id: int):
    return templates.TemplateResponse(
        "card.html", {"request": request, "card": cards[id]}
    )
