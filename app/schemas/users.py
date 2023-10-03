from pydantic import BaseModel


class UserScheme(BaseModel):
    id: int = 0
    email: str = "email"
    username: str = "username"

    class Config:
        from_attributes = True


class UserSchemeAdd(BaseModel):
    email: str = "email"
    username: str = "username"
    password: str = "password"


class UserTokenScheme(BaseModel):
    access_token: str
    token_type: str = "Bearer"

    class Config:
        populate_by_name = True
