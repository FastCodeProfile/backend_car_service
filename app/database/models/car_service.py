"""
Прайсы услуг авто-сервисов
"""

from typing import TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .user import User


class CarService(Base):
    user_fk: Mapped[int] = mapped_column(sa.ForeignKey('user.id', ondelete='CASCADE'), unique=False, nullable=False)
    user: Mapped["User"] = orm.relationship(back_populates='car_services', uselist=False)
    price: Mapped[int] = mapped_column(sa.Integer, unique=False, nullable=False)
    service: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=False)

    def __repr__(self):
        return f"CarService:{self.id=}"
