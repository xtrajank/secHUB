'''
secHUB // backend // api // firemon.py
Description: API logic for handling frontend requests for firemon and sending them to internal_firemon.py to pull the data.

TODO: This is an example assuming endpoints. An updated version would have the real endpoints.
'''
from fastapi import APIRouter, HTTPException
import backend.app.internal_api.internal_firemon as internal_firemon

router = APIRouter()

@router.get("/firemon")
async def get_firemon_data():
    try:
        data = await internal_firemon.fetch_firewall_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/firemon/changes")
async def get_firemon_changes():
    try:
        data = await internal_firemon.fetch_firewall_changes()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/firemon/violations")
async def get_firemon_violations():
    try:
        data = await internal_firemon.fetch_firewall_violations()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
