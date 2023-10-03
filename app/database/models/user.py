from typing import TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .vin_number import VinNumber
    from .car_service import CarService


class User(Base):
    email: Mapped[str] = mapped_column(sa.String, unique=False, nullable=False)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String, unique=False, nullable=False)
    vin_numbers: Mapped[list["VinNumber"]] = orm.relationship(back_populates="user", uselist=True, lazy="joined")
    car_services: Mapped[list["CarService"]] = orm.relationship(back_populates="user", uselist=True, lazy="joined")

    def __repr__(self):
        return f"User:{self.id=}"
