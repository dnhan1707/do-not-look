from schema import AccountCreate

class DatabaseService():
    def __init__(self):
        pass

    async def ingest_new_acc(self, account: AccountCreate, hashed_password: str) -> bool:
        pass