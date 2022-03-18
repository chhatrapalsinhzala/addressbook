from fastapi import FastAPI
from .schemas import Address
from .database import engine
from . import models
from .routers import user, address

app = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(address.router)
app.include_router(user.router)




