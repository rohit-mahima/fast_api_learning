from fastapi import APIRouter
from database.schema import payments
from uuid import UUID

router=APIRouter()

@router.get('/payment')
def get_payment():
    return "payment successfull"

@router.get('/payment/{payment_id}')
def get_payment_by_id(payment_id:UUID):
    return payment_id

@router.post('/payments')
def make_payment(payment:payments.Payment):
    return payment

