from re import template
from fastapi import APIRouter, HTTPException, status
from cryptography.fernet import Fernet
from starlette.requests import Request
from config.db import conn
from models.user import users
from schemas.userSchema import User
from fastapi.templating import Jinja2Templates

api = APIRouter()

key = Fernet.generate_key()

func = Fernet(key)

templates = Jinja2Templates(directory="templates")


@api.get("/", response_model=list[User], tags=["users"])
def get_users(req: Request):
    result = conn.execute(users.select()).fetchall()
    return templates.TemplateResponse("users-list.html", {"request": req, "users": result})


@api.post("/users", response_model=User, tags=["users"])
def create_user(user: User):
    newUser = {"name": user.name, "email": user.email}
    newUser["password"] = func.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(newUser))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@api.get("/users/{id}", response_model=User, tags=["users"])
def get_user(id: str, req: Request):
    result = conn.execute(users.select().where(users.c.id == id)).first()
    return templates.TemplateResponse("update-user.html", {"request": req, "user": result})


@api.put("/users/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name,
                 email=user.email).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()


@api.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    raise HTTPException(status_code=204, detail="User deleted successfully")

@api.get("/new-user")
def new_user(req: Request):
    return templates.TemplateResponse("new-user.html", {"request": req})
