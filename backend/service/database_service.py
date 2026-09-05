from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from schema import AccountCreate
from models import UserAccount
from database import get_db

class DatabaseService:
    def __init__(self, db_session: AsyncSession = Depends(get_db)):
        self.db_session = db_session

    async def ingest_new_acc(self, account: AccountCreate, hashed_password: str) -> bool:
        # 1. Create the SQLAlchemy object
        new_user = UserAccount(
            first_name=account.first_name,
            last_name=account.last_name,
            phone_number=account.phone_number,
            hashed_password=hashed_password
        )

        try:
            # 2. Add it and commit the transaction
            self.db_session.add(new_user)
            await self.db_session.commit()
            return True
        except IntegrityError:
            # 3. If phone_number is a duplicate, Postgres throws an IntegrityError
            await self.db_session.rollback()
            return False