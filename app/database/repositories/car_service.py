from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import CarService


class CarServiceRepo(Repository[CarService]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=CarService, session=session)

    async def new(
        self,
        user_fk: int | None = None,
        service: str | None = None,
        price: int | None = None,
    ) -> CarService:
        new_car_service = await self.session.merge(
            CarService(
                user_fk=user_fk,
                service=service,
                price=price,
            )
        )
        return new_car_service
