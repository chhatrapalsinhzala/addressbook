from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import address

router = APIRouter(
    prefix="/address",
    tags=['Addresses']
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.Address])
def all(db: Session = Depends(get_db)):
    return address.get_all(db)

#here, we are taking distance in kilomeater.
@router.get('/get-nearby-addresses', status_code=200, response_model=List[schemas.ShowAddress])
def get_near_addresses(lat:float, long:float, distance: int, db: Session = Depends(get_db)):
    return address.find_nearby_add(lat, long, distance, db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Address, db: Session = Depends(get_db)):
    return address.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db: Session = Depends(get_db)):
    return address.destroy(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Address, db: Session = Depends(get_db)):
    return address.update(id,request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowAddress)
def show(id:int, db: Session = Depends(get_db)):
    return address.show(id,db)

