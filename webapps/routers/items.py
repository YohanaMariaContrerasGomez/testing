from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from models import Items, User
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
def item_home(request: Request, db:Session=Depends(get_db)):
    items = db.query(Items).all()
    return templates.TemplateResponse("item_homepage.html", {"request": request, "items": items})

@router.get("/detail/{id}")
def item_detail(request: Request, id: int, db:Session=Depends(get_db)):
    item = db.query(Items).filter(Items.id==id).first()
    user = db.query(User).filter(User.id == item.owner_id).first()
    return templates.TemplateResponse("item_detail.html", {"request": request, "item": item, "user": user})