from fastapi import APIRouter
from fastapi import Cookie, Header
from database.schema import users

router=APIRouter()

@router.get('/coockies',response_model=users.User)
def get_coockies(ads_id:str=Cookie(default=None,title="Store coockie"),user_agent:str=Header(default="auth_token")):
    return ads_id