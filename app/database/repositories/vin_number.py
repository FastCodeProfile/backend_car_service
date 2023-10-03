from sqlalchemy.ext.asyncio import AsyncSession

from .abstract import Repository
from ..models import VinNumber


class VinNumberRepo(Repository[VinNumber]):
    def __init__(self, session: AsyncSession):
        super().__init__(type_model=VinNumber, session=session)

    async def new(
        self,
        user_fk: int | None = None,
        number: str | None = None,
    ) -> VinNumber:
        new_vin_number = await self.session.merge(
            VinNumber(
                user_fk=user_fk,
                number=number,
            )
        )
        return new_vin_number
