from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from math import radians, cos, sin, asin, sqrt

def distance_between_two_points(lat1, lat2, lon1, lon2):

    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return(c * r)



def get_all(db: Session):
    adds = db.query(models.Address).all()
    return adds

def create(request: schemas.Address,db: Session):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the user_id {request.user_id} is not available")
    new_add = models.Address(
        title = request.title,
        longitude = request.longitude,
        latitude = request.latitude,
        city = request.city,
        state = request.state,
        country = request.country,
        user_id = request.user_id
    )
    db.add(new_add)
    db.commit()
    db.refresh(new_add)
    return new_add

def destroy(id:int,db: Session):
    add = db.query(models.Address).filter(models.Address.id == id)

    if not add.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")

    add.delete(synchronize_session=False)
    db.commit()
    return 'Address removed successfully'

def update(id:int, request:schemas.Address, db:Session):
    add = db.query(models.Address).filter(models.Address.id == id)

    if not add.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with id {id} not found")
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the user_id {request.user_id} is not available")
    add.update(request.dict())
    db.commit()
    return 'Address updated successfully'

def show(id:int,db:Session):
    add = db.query(models.Address).filter(models.Address.id == id).first()
    if not add:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address with the id {id} is not available")
    return add

def find_nearby_add(lat:float, long:float, distance:int, db:Session):
    add = get_all(db)
    near_add_list = []
    if not add:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Address book is empty")
    for record in add:
        print("record=========")
        print(lat, long, distance)
        print(record)
        print(record.latitude)
        print(record.longitude)
        d = distance_between_two_points(lat1 = lat, 
                                    lat2 = record.latitude,
                                    lon1 = long, 
                                    lon2 = record.longitude)
        print("distance",d)
        if distance >= d:
            near_add_list.append(record)

    if not near_add_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"There are no address available in the diatance of {distance}km to location ({lat},{long}) ")

    return near_add_list