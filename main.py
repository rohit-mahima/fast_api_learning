from fastapi import FastAPI, Response
import json
from views import user, items, payments, coock

app=FastAPI()

app.include_router(user.router)
app.include_router(items.router)
app.include_router(payments.router)
app.include_router(coock.router)


@app.get('/')
def index()-> json  :
    """
    This is the index page

    """
    response=json.dumps({'status':200,'message':'OK'})
    
    return Response(status_code=200, content=response)