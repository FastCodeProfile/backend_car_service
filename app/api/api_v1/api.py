from fastapi import APIRouter

from app.api.api_v1.endpoints import users, vin_numbers, car_services

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(vin_numbers.router, prefix="/vin_numbers", tags=["vin_numbers"])
api_router.include_router(car_services.router, prefix="/car_services", tags=["car_services"])
