from pydantic import BaseModel
from uuid import UUID
from datetime import date

class Payment(BaseModel):
    payment_id:UUID
    payment_date:date
    

    