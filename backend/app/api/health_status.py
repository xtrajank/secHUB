'''
API logic for handling frontend requests for the system's health status reports and sending them to internal_health_status.py to pull the data.

TODO: This is an example assuming endpoints. An updated version would have the real endpoints.
'''
from fastapi import APIRouter, HTTPException
import backend.app.internal_api.internal_health_status as internal_health

router = APIRouter()

@router.get("/systemhealth")
async def get_health_data():
    try:
        data = await internal_health.fetch_health_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/systemhealth/service")
async def get_service_health_data():
    try:
        data = await internal_health.fetch_service_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/systemhealth/network")
async def get_network_health_data():
    try:
        data = await internal_health.fetch_network_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/systemhealth/security")
async def get_security_health_data():
    try:
        data = await internal_health.fetch_security_data()
        return {"status": "success", "data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))