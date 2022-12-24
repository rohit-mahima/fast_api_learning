from fastapi import APIRouter, Response
import json
from database.schema import users
from enum import Enum

router=APIRouter()

user=['rohit','mahima','kanchan']

class Pathoptions(str, Enum):
    mahima="mahima",
    kanchan="kanchan",
    rohit="rohit"

@router.get('/user')
def get_users(start:int, end:int)->list:
    """List of all users

    Returns:
        json: list of all users
    """
    return user[start:end]

@router.post('/user',status_code=201)
def create_user(user:users.User)-> json:
    """Create new user

    Args:
        user (users.User): User body

    Returns:
        json: created response
    """
    return Response(status_code=201, content="created")

@router.get('/user/{user_id}')
def get_user_by_id(user_id:Pathoptions)->json:
    """_summary_

    Args:
        user_id (int): _description_

    Returns:
        json: _description_
    """
    return user[user_id]

@router.put('/user/{user_id}')
def update_user(user_id:int, user:users.User)-> json:
    """_summary_

    Args:
        user_id (int): _description_
        user (users.User): _description_

    Returns:
        json: _description_
    """
    return user