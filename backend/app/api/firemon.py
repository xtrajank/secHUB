'''
secHUB // backend // api // firemon.py
Description: API logic for handling frontend requests for firemon and sending them to internal_firemon.py to pull the data.
'''
from fastapi import APIRouter, HTTPException
import backend.app.internal_api.internal_firemon as internal_firemon

router = APIRouter()

@router.get("/firemon/changes")
async def get_firemon_changes():
    try:
        data = await internal_firemon.fetch_firewall_changes()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
