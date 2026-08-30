from pydantic import BaseModel

# Used for /signup
class AccountCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    password: str 

# Used for /login
class AccountLogin(BaseModel):
    phone_number: str
    password: str

# Used to send data back to the user securely (no password)
class AccountResponse(BaseModel):
    first_name: str
    last_name: str
    phone_number: str