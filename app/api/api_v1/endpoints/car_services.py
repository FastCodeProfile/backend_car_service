from fastapi import APIRouter, Depends

from app.api import depends
from app.database import Database
from app.schemas import CarServiceScheme, CarServiceSchemeAdd, CarServiceSchemeList

router = APIRouter()


@router.get("/get", response_model=CarServiceSchemeList)
async def get(current_user=Depends(depends.get_current_user)):
    car_services = [{"service": x.service, "price": x.price} for x in current_user.car_services]
    return CarServiceSchemeList(list=car_services)


@router.post("/new", response_model=CarServiceScheme)
async def new(car_service: CarServiceSchemeAdd, current_user=Depends(depends.get_current_user),
              db: Database = Depends(depends.get_db)):
    new_car_service = await db.car_service.new(current_user.id, car_service.service, car_service.price)
    await db.session.commit()
    return CarServiceScheme(**new_car_service.__dict__)
