from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from goodbyesql.config import GoodbyeSQLConfig
from typing import Annotated
from fastapi import Depends
from goodbyesql.registry import get_session
from pydantic import EmailStr

DB_Session = Annotated[AsyncSession, Depends(get_session)]


class GoodbyeSQL:
    def __init__(self, config: GoodbyeSQLConfig):
        self.config = config

    async def get_info_by_username(self, *, session: DB_Session, username: str):

        model = self.config.user_model
        field = getattr(model,self.config.username_field)

        query = select(model).where(field == username)
        result = await session.execute(query)
        user: None = result.scalar_one_or_none()
        return user


    async def get_info_by_email(self, *, session: DB_Session, email: EmailStr):

        model = self.config.user_model
        field = getattr(model, self.config.username_field)

        query = select(model).where(field == email)
        result = await session.execute(query)

        info: None = result.scalar_one_or_none()

        return info

    def check_my_library():
        print("It is working right now!")