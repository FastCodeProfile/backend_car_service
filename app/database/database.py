from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from app.core.config import settings
from .repositories import UserRepo, VinNumberRepo, CarServiceRepo


def create_async_engine(url: URL | str) -> AsyncEngine:
    return _create_async_engine(url=url, echo=False, pool_pre_ping=True)


engine = create_async_engine(settings.pg_dns)


class Database:
    session: AsyncSession

    user: UserRepo
    vin_number: VinNumberRepo
    car_service: CarServiceRepo

    def __init__(
        self,
        session: AsyncSession,
        user: UserRepo = None,
        vin_number: VinNumberRepo = None,
        car_service: CarServiceRepo = None,
    ):
        self.session = session
        self.user = user or UserRepo(session=session)
        self.vin_number = vin_number or VinNumberRepo(session=session)
        self.car_service = car_service or CarServiceRepo(session=session)
