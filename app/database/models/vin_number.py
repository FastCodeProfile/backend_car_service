from typing import TYPE_CHECKING

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base

if TYPE_CHECKING:
    from .user import User


class VinNumber(Base):
    user_fk: Mapped[int] = mapped_column(sa.ForeignKey('user.id', ondelete='CASCADE'), unique=False, nullable=False)
    user: Mapped["User"] = orm.relationship(back_populates='vin_numbers', uselist=False)
    number: Mapped[str] = mapped_column(sa.String, unique=False, nullable=False)

    def __repr__(self):
        return f"VinNumber:{self.id=}"
