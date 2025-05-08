'''
secHUB // backend // internal_api // internal_firemon.py
Description: API wrapper for pulling data from FireMon. Forms and sends the HTTP requests. Returns JSONified data.

Features:
    - Get changes made to firewall
'''
import httpx
from config import INTERNAL_API_BASE, INTERNAL_API_KEY

async def fetch_firewall_changes():
    url = f"{INTERNAL_API_BASE}/firewall/changes"
    headers = {"Authorization": f"Bearer {INTERNAL_API_KEY}"}

    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(url, headers=headers)
        response.raise_for_status()
        return response.json()