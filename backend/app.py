from fastapi import FastAPI, HTTPException, Depends
from schema import AccountCreate, AccountResponse, AccountLogin
from controller.account_controller import AccountController

app = FastAPI()

@app.post("/signup", response_model=AccountResponse)
async def signup(
    account: AccountCreate,
    controller: AccountController = Depends()
):
    response = await controller.signup(account)
    
    if not response:
        raise HTTPException(status_code=400, detail="Account Not Created")
        
    return account

@app.post("/login")
def login(credentials: AccountLogin):
    
    return {"access_token": "fake-super-secret-token", "token_type": "bearer"}

@app.post("/logout")
def logout(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Not logged in")
    
    return {"message": "Successfully logged out"}

@app.get("/health")
def health():
    return {"statusCode": 200}