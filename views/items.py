from fastapi import APIRouter
from fastapi import Query, Path, Body
from database.schema import items

router=APIRouter()

@router.get('/items/')
def get_items(q: str or None = Query(default=None, max_length=20, alias="item name", min_length=5,regex="^fixedquery$")) -> dict:
    results={'items':[{'item_id':'foo'},{'item_id':'bar'}]}
    if q:
        results['items'].append({'q':q})
    return results

@router.get('/items/{item_id}')
def get_item_by_id(item_id:int=Path(title="Enter the item id",include_in_schema=True)):
    return item_id

@router.post('/items')
def create_item(item:items.Items):
    return item

@router.put('/items/{item_id}')
def update_item(item_id:int, item:items.Items=Body(embed=True), importance:int=Body()):
    return item_id, item
