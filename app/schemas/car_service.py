from pydantic import BaseModel


class CarServiceScheme(BaseModel):
    price: int = "price"
    service: str = "service"

    class Config:
        from_attributes = True


class CarServiceSchemeAdd(BaseModel):
    price: int = "price"
    service: str = "service"


class CarServiceSchemeList(BaseModel):
    list: list
