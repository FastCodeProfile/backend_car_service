from pydantic import BaseModel


class VinNumberScheme(BaseModel):
    number: str = "number"

    class Config:
        from_attributes = True


class VinNumberSchemeAdd(BaseModel):
    number: str = "number"


class VinNumberSchemeList(BaseModel):
    list: list
