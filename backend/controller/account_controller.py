from fastapi import Depends
from schema import AccountCreate
from service.account_service import AccountService
from service.database_service import DatabaseService

class AccountController:
    def __init__(
        self, 
        account_service: AccountService = Depends(),
        database_service: DatabaseService = Depends()
    ):
        self.account_service = account_service
        self.database_service = database_service

    async def signup(self, account: AccountCreate) -> bool:
        hashed_password = self.account_service.hash_password(account.password)
        is_saved = await self.database_service.ingest_new_acc(account, hashed_password)

        return is_saved