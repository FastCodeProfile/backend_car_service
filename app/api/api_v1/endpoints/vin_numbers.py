from fastapi import APIRouter, Depends

from app.api import depends
from app.database import Database
from app.schemas import VinNumberScheme, VinNumberSchemeAdd, VinNumberSchemeList

router = APIRouter()


@router.get("/get", response_model=VinNumberSchemeList)
async def get(current_user=Depends(depends.get_current_user)):
    vin_numbers = [x.number for x in current_user.vin_numbers]
    return VinNumberSchemeList(list=vin_numbers)


@router.post("/new", response_model=VinNumberScheme)
async def new(vin_number: VinNumberSchemeAdd, current_user=Depends(depends.get_current_user),
              db: Database = Depends(depends.get_db)):
    new_vin_number = await db.vin_number.new(current_user.id, vin_number.number)
    await db.session.commit()
    return VinNumberScheme(**new_vin_number.__dict__)
